# Google Sheets API Doc: https://developers.google.com/sheets/api/reference/rest

__version__ = "dev"

from typing import Optional

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import Resource, build
from googleapiclient.errors import HttpError


class SheetBase:
    """Base class for Google Sheets API. The base class is 
    used to setup the Google Sheets API and authenticate the service account.
    """

    def __init__(self):
        self._service: Optional[Resource] = None
        self._sheet: Optional[Resource] = None
        self._creds: Optional[Credentials] = None

    def setup(self, service_account_file) -> None:
        """Setup the Google Sheets API

        Args:
            service_account_file (str): Path to the service account file
        """

        self.authenticate(service_account_file)
        self._service = build("sheets", "v4", credentials=self._creds)
        self._sheet = self._service.spreadsheets()

    def authenticate(self, service_account_file: str) -> Credentials:
        """Authenticate the Google Sheets API

        Args:
            service_account_file (str): Path to the service account file

        Returns:
            Credentials: Credentials of the service account
        """

        g_scopes: list = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]
        self._creds = Credentials.from_service_account_file(
            service_account_file, scopes=g_scopes
        )

    def get_spreadsheet_properties(self) -> dict:
        """Get the properties of a spreadsheet

        Args:
            spreadsheet_id (str): ID of the spreadsheet

        Returns:
            dict: Properties of the spreadsheet
            Keys: "properties", "sheets", "spreadsheetUrl"
        """

        return self._sheet.get(spreadsheetId=self.spreadsheet_id).execute()


class SheetReader(SheetBase):
    """Class for reading data from a spreadsheet."""

    def __init__(self):
        super().__init__()

    def get_sheet_values(self, spreadsheet_id: str, range: str) -> list:
        """Get the values of a spreadsheet

        Args:
            spreadsheet_id (str): ID of the spreadsheet
            range (str): Range of the spreadsheet. Ex: Sheet1!A1:B2 or Sheet1

        Returns:
            list: Values of the spreadsheet with major dimension of rows
        """

        results = (
            self._sheet.values().get(spreadsheetId=spreadsheet_id, range=range).execute()
        )

        return results.get("values", [])

    def get_cell_color(self, spreadsheet_id: str, range: str) -> dict:
        """Get the color of a cell

        Args:
            spreadsheet_id (str): ID of the spreadsheet
            range (str): Range of the spreadsheet. Ex: Sheet1!A1:B2 or Sheet1

        Returns:
            dict: Color of the cell. Ex: {'red': 0.0, 'green': 0.0, 'blue': 0.0}
        """

        results = self._sheet.get(
            spreadsheetId=spreadsheet_id,
            ranges=range,
            fields="sheets/data/rowData/values/effectiveFormat/backgroundColor",
        ).execute()

        return results["sheets"][0]["data"][0]["rowData"][0]["values"][0][
            "effectiveFormat"
        ]["backgroundColor"]


class SheetUpdater(SheetBase):
    """Class that writes data to a spreadsheet. Can target a current
    spreadsheet or create a new spreadsheet.
    """

    def __init__(self):
        super().__init__()
        self._filename = ""
        self._spreadsheet_id = ""
        self._folder_id = ""
        self._current_sheets: dict = {}
        self._sheet_id_runner: int = 1
        self._requests = list()
        self._update_values_requests = list()

    def set_spreadsheet(self, spreadsheet_id: str) -> None:
        """Set the current spreadsheet

        Args:
            spreadsheet_id (str): ID of the spreadsheet
        """

        self._spreadsheet_id = spreadsheet_id

        # Update the current sheets from the sheet properties.
        self._current_sheets.clear()

        sheets_properties = self.get_spreadsheet_properties()["sheets"]

        for sheet in sheets_properties:
            title = sheet["properties"]["title"]
            id = sheet["properties"]["sheetId"]

            self._current_sheets[title] = {"id": id, "next_row": 1}

    def create_spreadsheet(self, filename: str, folder_id: str) -> None:
        """Create a new spreadsheet

        Args:
            title (str): Title of the spreadsheet
            folder_id (str): ID of the folder to place the spreadsheet in
        """

        drive_service = build("drive", "v3", credentials=self._creds)

        file_metadata = {
            "name": filename,
            "parents": [folder_id],
            "mimeType": "application/vnd.google-apps.spreadsheet",
        }

        response = drive_service.files().create(body=file_metadata).execute()
        self._spreadsheet_id = response["id"]
        self._current_sheets = {"Sheet1": {"id": 0, "next_row": 1}}

    def get_values_by_range(self, cell_range: str) -> Optional[dict]:
        """Returns the values of a specified range.
        
        Args:
            cell_range (str): Range of the sheet. Ex: Sheet1!A1:B2 or Sheet1
            
        Returns:
            Optional[dict]: Values of the specified range
        """

        response = (
            self._sheet.values()
            .get(spreadsheetId=self._spreadsheet_id, range=cell_range)
            .execute()
        )
        return response.get("values")

    def get_next_row(self, sheet_name: str) -> int:
        """Returns the last row number that has been appended to the specified sheet.
        
        Args:
            sheet_name (str): Name of the sheet to check
        
        Returns:
            int: Last row number that has been appended to the specified sheet
        """

        return self._current_sheets[sheet_name]["next_row"]

    def set_file_and_folder_info(self, file_and_folder_info: tuple) -> None:
        """Set the filename and folder information for the sheet export.
        
        Args:
            file_and_folder_info (tuple): Filename and folder ID. Ex: ("filename", "folder_id")
        """

        self._filename = file_and_folder_info[0]
        self._folder_id = file_and_folder_info[1]

    def values_batch_update(self) -> None:
        """Batch updates all current value requests.
        This will execute all update_values_requests in the order they were added
        and then clear the update_values_requests pool.
        """

        try:
            values_body = {
                "valueInputOption": "USER_ENTERED",
                "data": self._update_values_requests,
            }
            self._sheet.values().batchUpdate(
                spreadsheetId=self._spreadsheet_id, body=values_body
            ).execute()
            self._update_values_requests.clear()
        except HttpError as e:
            raise e

    def batch_update(self) -> None:
        """Batch updates all current requests.
        This will execute all requests in the order they were added
        and then clear the requests pool.
        """

        try:
            body: dict = {"requests": self._requests}
            self._sheet.batchUpdate(spreadsheetId=self._spreadsheet_id, body=body).execute()
            self._requests.clear()
        except HttpError as e:
            raise e

    def append_value(self, value: list, range: str = "A1") -> None:
        """Append a value to the end of the target spreadsheet.
        This is not batched and will be executed immediately.
        
        Args:
            value (list): Value to append
            range (str, optional): Range of the sheet. Defaults to "A1".
        """

        try:
            body: dict = {"values": value}
            self._sheet.values().append(
                spreadsheetId=self._spreadsheet_id,
                range=range,
                valueInputOption="USER_ENTERED",
                body=body,
            ).execute()
        except HttpError as e:
            raise e

    def add_values_request(self, cell_range: str, rows_of_values: list) -> None:
        """Add values in a range.
        Adds the request to update_values_request pool.
        This will update when the next values_batch_update is called.
        
        Args:
            cell_range (str): Range of the sheet. Ex: Sheet1!A1:B2 or Sheet1
            rows_of_values (list): List of rows to add to the sheet
        """

        processed_range: tuple = self.process_range(cell_range)
        sheet_name: str = cell_range.split("!")[0]
        # Rows start at 0 behind the scenes. +1 match spreadsheet starting at 1.
        next_row: int = (processed_range[2] + 1) + len(rows_of_values)

        # Check if you are adding to the end of the sheet.
        # next_row will be greater than current_sheet:next_row if adding to the end.
        if self._current_sheets[sheet_name]["next_row"] < next_row:
            self._current_sheets[sheet_name]["next_row"] = next_row

        self._update_values_requests.append({"range": cell_range, "values": rows_of_values})

    def change_google_sheet_title_request(self, name: str) -> None:
        """Change the name of the google sheet.
        Adds the request to requests pool.
        This will update when the next batch_update is called.

        Args:
            name (str): New name of the sheet
        """

        self._requests.append(
            {
                "updateSpreadsheetProperties": {
                    "properties": {"title": f"{name}"},
                    "fields": "title",
                }
            }
        )

    def change_sheet_name_request(self, old_name: str, new_name: str) -> None:
        """Change the name of the specified sheet.
        Adds the request to requests pool.
        This will update when the next batch_update is called.
        
        Args:
            old_name (str): Name of the sheet to change
            new_name (str): New name of the sheet
        """

        self._current_sheets[new_name] = self._current_sheets[old_name]
        del self._current_sheets[old_name]

        self._requests.append(
            {
                "updateSheetProperties": {
                    "properties": {
                        "sheetId": self._current_sheets[new_name]["id"],
                        "title": f"{new_name}",
                    },
                    "fields": "title",
                }
            }
        )

    def add_sheet_request(self, name: str) -> None:
        """Add a new sheet request to the Google Sheet.
        Adds the request to requests pool.
        This will update when the next batch_update is called.
        
        Args:
            name (str): Name of the sheet to add    
        """

        self._current_sheets[name] = {"id": self._sheet_id_runner, "next_row": 0}
        self._sheet_id_runner += 1

        self._requests.append(
            {
                "addSheet": {
                    "properties": {
                        "sheetId": self._current_sheets[name]["id"],
                        "title": f"{name}",
                    }
                }
            }
        )

    def set_sheet_grid_properties_request(
        self, name: str, number_of_rows: int = 1000, number_of_columns: int = 26, hideGridlines: bool=False
    ) -> None:
        """Changes the rows and columns for a sheet.
        Adds the request to requests pool.
        This will update when the next batch_update is called.
        
        Args:
            name (str): Name of the sheet to change
            number_of_rows (int, optional): Number of rows to set. Defaults to 1000.
            number_of_columns (int, optional): Number of columns to set. Defaults to 26.
            hideGridlines (bool, optional): Hide the gridlines. Defaults to False.
        """

        new_grid_properties = {
            "rowCount": number_of_rows,
            "columnCount": number_of_columns,
            "hideGridlines": hideGridlines,
        }

        self._requests.append(
            {
                "updateSheetProperties": {
                    "properties": {
                        "sheetId": self._current_sheets[name]["id"],
                        "gridProperties": new_grid_properties,
                    },
                    "fields": "gridProperties",
                }
            }
        )

    def resize_request(self, cell_range: str, size: int, range_as_ints=False) -> None:
        """Resize a column or row by specified number of pixels.
        Adds the request to requests pool.
        This will update when the next batch_update is called.

        Range formats:
            - Columns: "SheetName!StartColumn:EndColumn "
                - Ex. "Sheet1!A:A" will resize column A.
            - Rows: "SheetName!StartRow:EndRow"
                - Ex. "Sheet1!1:1" will resize row 1.

        Args:
            cell_range (str): Range of the sheet. Ex. "Sheet1!A:A" or "Sheet1!1:1"
            size (int): Size to resize the column or row.
            range_as_ints (bool, optional): Process the range as integers. Defaults to False.
        """

        if range_as_ints:
            processed_range = self.process_range_as_ints(cell_range)
        else:
            processed_range = self.process_range(cell_range)

        dimension: str = ""
        start_index: int = 0
        end_index: int = 0

        if processed_range[2] < 0:
            dimension = "COLUMNS"
            start_index = processed_range[1]
            end_index = processed_range[3]
        else:
            dimension = "ROWS"
            start_index = processed_range[2]
            end_index = processed_range[4]

        format_style = {
            "updateDimensionProperties": {
                "properties": {"pixelSize": size},
                "fields": "pixelSize",
                "range": {
                    "sheetId": processed_range[0],
                    "dimension": dimension,
                    "startIndex": start_index,
                    "endIndex": end_index,
                },
            }
        }
        self._requests.append(format_style)

    def align_and_wrap_cells_range_request(
        self,
        cell_range: str,
        horizontal: str = "LEFT",
        vertical: str = "BOTTOM",
        wrapping: str = "CLIP",
        range_as_ints=False,
    ) -> None:
        """Align and wrap cells in the provided range based on alignment provided.
        Adds the request to requests pool.
        This will update when the next batch_update is called.

        Alignment:
            - Horizontal: LEFT, CENTER, RIGHT
            - Vertical: TOP, MIDDLE, BOTTOM
        Wrapping:
            - OVERFLOW_CELL
            - CLIP
            - WRAP

        Args:
            cell_range (str): Range of the sheet. Ex: Sheet1!A1:B2 or Sheet1
            horizontal (str, optional): Horizontal alignment. Defaults to "LEFT".
            vertical (str, optional): Vertical alignment. Defaults to "BOTTOM".
            wrapping (str, optional): Wrapping strategy. Defaults to "CLIP".
            range_as_ints (bool, optional): Process the range as integers. Defaults to False.
        """

        if range_as_ints:
            processed_range = self.process_range_as_ints(cell_range)
        else:
            processed_range = self.process_range(cell_range)

        format_style = {
            "repeatCell": {
                "range": {
                    "sheetId": processed_range[0],
                    "startColumnIndex": processed_range[1],
                    "startRowIndex": processed_range[2],
                    "endColumnIndex": processed_range[3],
                    "endRowIndex": processed_range[4],
                },
                "cell": {
                    "userEnteredFormat": {
                        "horizontalAlignment": horizontal,
                        "verticalAlignment": vertical,
                        "wrapStrategy": wrapping,
                    }
                },
                "fields": "userEnteredFormat(horizontalAlignment, verticalAlignment, wrapStrategy)",
            }
        }
        self._requests.append(format_style)

    def merge_cells_range_request(
        self, cell_range: str, merge_type: str = "MERGE_ALL", range_as_ints=False
    ) -> None:
        """Merge cells in the provided range based on merge type.
        Adds the request to requests pool.
        This will update when the next batch_update is called.

        Merge Types:
            - MERGE_ALL
            - MERGE_COLUMNS
            - MERGE_ROWS

        Args:
            cell_range (str): Range of the sheet. Ex: Sheet1!A1:B2 or Sheet1
            merge_type (str, optional): Type of merge. Defaults to "MERGE_ALL".
            range_as_ints (bool, optional): Process the range as integers. Defaults to False.
        """

        if range_as_ints:
            processed_range = self.process_range_as_ints(cell_range)
        else:
            processed_range = self.process_range(cell_range)

        format_style = {
            "mergeCells": {
                "range": {
                    "sheetId": processed_range[0],
                    "startColumnIndex": processed_range[1],
                    "startRowIndex": processed_range[2],
                    "endColumnIndex": processed_range[3],
                    "endRowIndex": processed_range[4],
                },
                "mergeType": merge_type,
            }
        }
        self._requests.append(format_style)

    def format_font_range_request(
        self,
        cell_range: str,
        font_family: str = "Arial",
        font_size: int = 10,
        bold: bool = False,
        italic: bool = False,
        strikethrough: bool = False,
        underline: bool = False,
        text_color: tuple = (0, 0, 0),
        range_as_ints=False,
    ) -> None:
        """Set the font for a range of cells.
        Adds the request to requests pool.
        This will update when the next batch_update is called.
        
        Args:
            cell_range (str): Range of the sheet. Ex: Sheet1!A1:B2 or Sheet1
            font_family (str, optional): Font family. Defaults to "Arial".
            font_size (int, optional): Font size. Defaults to 10.
            bold (bool, optional): Bold text. Defaults to False.
            italic (bool, optional): Italic text. Defaults to False.
            strikethrough (bool, optional): Strikethrough text. Defaults to False.
            underline (bool, optional): Underline text. Defaults to False.
            text_color (tuple, optional): Color of the text (Red, Green, Blue). Defaults to (0, 0, 0).
            range_as_ints (bool, optional): Process the range as integers. Defaults to False.
        """

        if range_as_ints:
            processed_range = self.process_range_as_ints(cell_range)
        else:
            processed_range = self.process_range(cell_range)

        format_style = {
            "repeatCell": {
                "range": {
                    "sheetId": processed_range[0],
                    "startColumnIndex": processed_range[1],
                    "startRowIndex": processed_range[2],
                    "endColumnIndex": processed_range[3],
                    "endRowIndex": processed_range[4],
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {
                            "foregroundColor": {
                                "red": text_color[0],
                                "green": text_color[1],
                                "blue": text_color[2],
                            },
                            "font_family": font_family,
                            "fontSize": font_size,
                            "bold": bold,
                            "italic": italic,
                            "strikethrough": strikethrough,
                            "underline": underline,
                        }
                    }
                },
                "fields": "userEnteredFormat(textFormat)",
            }
        }
        self._requests.append(format_style)

    def fill_range_request(
        self, cell_range: str, fill_color: tuple = (1, 1, 1), range_as_ints=False
    ) -> None:
        """Set the background fill for a range of cells.
        Adds the request to requests pool.
        This will update when the next batch_update is called.

        Args:
            cell_range (str): Range of the sheet. Ex: Sheet1!A1:B2 or Sheet1
            fill_color (tuple, optional): Color of the fill (Red, Green, Blue). Defaults to (1, 1, 1).
            range_as_ints (bool, optional): Process the range as integers. Defaults to False.
        """

        if range_as_ints:
            processed_range = self.process_range_as_ints(cell_range)
        else:
            processed_range = self.process_range(cell_range)

        format_style = {
            "repeatCell": {
                "range": {
                    "sheetId": processed_range[0],
                    "startColumnIndex": processed_range[1],
                    "startRowIndex": processed_range[2],
                    "endColumnIndex": processed_range[3],
                    "endRowIndex": processed_range[4],
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {
                            "red": fill_color[0],
                            "green": fill_color[1],
                            "blue": fill_color[2],
                        }
                    }
                },
                "fields": "userEnteredFormat(backgroundColor)",
            }
        }
        self._requests.append(format_style)

    def set_outer_border_range_request(
        self,
        cell_range: str,
        type: str = "SOLID",
        color: tuple = (0, 0, 0),
        range_as_ints=False,
    ) -> None:
        """Set the outer border for a range of cells.
        Adds the request to requests pool.
        This will update when the next batch_update is called.

        Border types:
            - DOTTED
            - DASHED
            - SOLID
            - SOLID_MEDIUM
            - SOLID_THICK
            - NONE
            - DOUBLE

        Args:
            cell_range (str): Range of the sheet. Ex: Sheet1!A1:B2 or Sheet1
            type (str, optional): Type of border. Defaults to "SOLID".
            color (tuple, optional): Color of the border. Defaults to (0, 0, 0).
            range_as_ints (bool, optional): Process the range as integers. Defaults to False.
        """

        if range_as_ints:
            processed_range = self.process_range_as_ints(cell_range)
        else:
            processed_range = self.process_range(cell_range)

        border_format = {
            "updateBorders": {
                "range": {
                    "sheetId": processed_range[0],
                    "startColumnIndex": processed_range[1],
                    "startRowIndex": processed_range[2],
                    "endColumnIndex": processed_range[3],
                    "endRowIndex": processed_range[4],
                },
                "top": {
                    "style": type,
                    "color": {"red": color[0], "green": color[1], "blue": color[2]},
                },
                "bottom": {
                    "style": type,
                    "color": {"red": color[0], "green": color[1], "blue": color[2]},
                },
                "left": {
                    "style": type,
                    "color": {"red": color[0], "green": color[1], "blue": color[2]},
                },
                "right": {
                    "style": type,
                    "color": {"red": color[0], "green": color[1], "blue": color[2]},
                },
            }
        }
        self._requests.append(border_format)

    def set_bottom_border_range_request(
        self,
        cell_range: str,
        type: str = "SOLID",
        color: tuple = (0, 0, 0),
        range_as_ints=False,
    ) -> None:
        """Set the bottom border for a range of cells.
        Adds the request to requests pool.
        This will update when the next batch_update is called.

        Border types:
            - DOTTED
            - DASHED
            - SOLID
            - SOLID_MEDIUM
            - SOLID_THICK
            - NONE
            - DOUBLE

        Args:
            cell_range (str): Range of the sheet. Ex: Sheet1!A1:B2 or Sheet1
            type (str, optional): Type of border. Defaults to "SOLID".
            color (tuple, optional): Color of the border. Defaults to (0, 0, 0).
            range_as_ints (bool, optional): Process the range as integers. Defaults to False.
        """

        if range_as_ints:
            processed_range = self.process_range_as_ints(cell_range)
        else:
            processed_range = self.process_range(cell_range)

        border_format = {
            "updateBorders": {
                "range": {
                    "sheetId": processed_range[0],
                    "startColumnIndex": processed_range[1],
                    "startRowIndex": processed_range[2],
                    "endColumnIndex": processed_range[3],
                    "endRowIndex": processed_range[4],
                },
                "bottom": {
                    "style": type,
                    "color": {"red": color[0], "green": color[1], "blue": color[2]},
                },
            }
        }
        self._requests.append(border_format)

    def process_range(self, cell_range: str) -> tuple:
        """
        Process the range into sheet_id and starting and ending cell.
        Adds the request to requests pool.
        This will update when the next batch_update is called.

        Args:
            cell_range (str): Range of the sheet. Ex: Sheet1!A1:B2 or Sheet1

        Returns:
            tuple: Processed range. Ex: (1, 0, 0, 1, 1)
        """

        range_parts: list = cell_range.split("!")
        sheet_id: int = self._current_sheets[range_parts[0]]["id"]
        start_pair = list()
        end_pair = list()
        range_pair_values: list = range_parts[1].split(":")

        if len(range_pair_values) > 1:
            start_pair: list = self.process_cell_pair(range_pair_values[0])
            end_pair: list = self.process_cell_pair(range_pair_values[1])
        else:
            start_pair: list = self.process_cell_pair(range_pair_values[0])
            end_pair: list = [-1, -1]

        return (
            sheet_id,
            start_pair[0],
            start_pair[1] - 1,
            end_pair[0] + 1,
            end_pair[1],
        )

    def process_range_as_ints(self, cell_range: str) -> tuple:
        """Process the range as integers. Some parts of the API require
        the range to be integers instead of letters and numbers.
        
        Args:
            cell_range (str): Range of the sheet. Ex: "1,2,3,4"
        
        Returns:
            tuple: Processed range as integers. Ex: (1,2,3,4,5)
        """

        cell_range = cell_range.split(",")
        sheet_id: int = self._current_sheets[cell_range[0]]["id"]

        return (
            sheet_id,
            int(cell_range[1]),
            int(cell_range[2]),
            int(cell_range[3]),
            int(cell_range[4]),
        )

############ LOOK INTO THIS ###############################
    def process_cell_pair(self, pair: str) -> list:
        """Determine the cell pair

        Args:
            pair (str): Cell pair. Ex: A1 or 1

        Returns:
            list: Processed cell pair. Ex: [0, 1]
        """

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        number_columns = 52
        base_columns = {}

        # Map column letters to numerical value.
        for x in range(number_columns):
            if x // 26 == 0:
                base_columns[letters[x]] = x
            elif x // 26 == 1:
                base_columns[f"A{letters[x % 26]}"] = x

        alpha_chars = ""
        num_chars = ""
        for char in pair:
            if char.isalpha():
                alpha_chars += char
            else:
                num_chars += char
        
        if num_chars == "":
            return [base_columns[alpha_chars], -1]
        if alpha_chars == "":
            return [0, int(num_chars)]
        
        return [base_columns[alpha_chars], int(num_chars)]

    def clear_sheet_values(self, cell_range: str) -> None:
        """Clear the values of a sheet.
        This is not batched and will be executed immediately.

        Args:
            range (str): Range of the sheet. Ex: Sheet1!A1:B2 or Sheet1
        """

        try:
            self._sheet.values().clear(
                spreadsheetId=self._spreadsheet_id, range=cell_range
            ).execute()
        except HttpError as e:
            raise e

    def clear_sheet_colors(self, sheet_name: str) -> None:
        """Clear the color of a sheet by calling fill_range_request and setting to white.
        Adds the request to requests pool.
        This will update when the next batch_update is called.
        
        Args:
            sheet_name (str): Name of the sheet to clear
        """

        sheet_props = self.get_spreadsheet_properties()
        last_row = sheet_props["sheets"][0]["properties"]["gridProperties"]["rowCount"]
        last_column = sheet_props["sheets"][0]["properties"]["gridProperties"][
            "columnCount"
        ]
        self.fill_range_request(
            f"{sheet_name},0,0,{last_column},{last_row}", (1, 1, 1), range_as_ints=True
        )

    def reset_sheet_font(self, sheet_name: str) -> None:
        """Reset the font of a sheet by calling format_font_range_request and setting to default.
        Adds the request to requests pool.
        This will update when the next batch_update is called.
        
        Args:
            sheet_name (str): Name of the sheet to reset
        """

        sheet_props: dict = self.get_spreadsheet_properties()
        last_row = sheet_props["sheets"][0]["properties"]["gridProperties"]["rowCount"]
        last_column = sheet_props["sheets"][0]["properties"]["gridProperties"][
            "columnCount"
        ]
        self.format_font_range_request(
            f"{sheet_name},0,0,{last_column},{last_row}", range_as_ints=True
        )


if __name__ == "__main__":
    print("This is a module...")
