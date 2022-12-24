# Google Sheets API Doc: https://developers.google.com/sheets/api/reference/rest

__version__ = "dev"

from typing import Optional

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import Resource, build



class GoogleSheetBase:
    """Base class for Google Sheet Tools."""

    def __init__(self):
        self.service: Optional[Resource] = None
        self.sheet: Optional[Resource] = None
        self.creds: Optional[Credentials] = None

    def setup(self, service_account_file) -> None:
        """Setup the Google Sheets service connection."""

        self.authenticate(service_account_file)
        self.service = build("sheets", "v4", credentials=self.creds)
        self.sheet = self.service.spreadsheets()

    def authenticate(self, service_account_file) -> Credentials:
        """Athenticate and connect to Google services for spread sheets."""

        g_scopes: list = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]
        self.creds = Credentials.from_service_account_file(
            service_account_file, scopes=g_scopes
        )

    def get_spreadsheet_properties(self) -> dict:
        """Return the spreadsheet properties as a dict.
        Keys on returned dict:
            - "properties" - General properties of the entire spreadsheet.
            - "sheets" - Information on all current sheets in the spreadsheet.
            - "spreadsheetUrl"
        """

        return self.sheet.get(spreadsheetId=self.spreadsheet_id).execute()


class GoogleSheetReader(GoogleSheetBase):
    """Reads in the data of a sheet on a Google Spreadsheet."""

    def __init__(self):
        super().__init__()

    def read_data_from_sheet(self, spreadsheet_id, sheet_name) -> list:
        """
        Read in the data from a target sheet on a spreadsheet.
        Return it as a list.
        """

        result_of_read = (
            self.sheet.values()
            .get(spreadsheetId=spreadsheet_id, range=f"{sheet_name}")
            .execute()
        )

        values = result_of_read.get("values", [])

        return values

    def read_cell_color(self, spreadsheet_id, ranges) -> dict:
        """
        Read the color of a cell.
        Returns a dict of red, green, and blue.
        """

        cell_data = self.sheet.get(
            spreadsheetId=spreadsheet_id, ranges=ranges, includeGridData=True
        ).execute()

        return cell_data["properties"]["defaultFormat"]["backgroundColor"]


class GoogleSheetUpdater(GoogleSheetBase):
    """Creates or updates a current Google Sheet."""

    def __init__(self):
        super().__init__()
        self.filename = ""
        self.spreadsheet_id = ""
        self.folder_id = ""
        self.current_sheets: dict = {}
        self.sheet_id_runner: int = 1
        self.requests = list()
        self.update_values_requests = list()

    def target_spreadsheet(self, spreadsheet_id) -> None:
        """Sets the information to an already created Google Sheet."""

        self.spreadsheet_id = spreadsheet_id

        # Update the current sheets from the sheet properties.
        self.current_sheets.clear()

        sheets_properties = self.get_spreadsheet_properties()["sheets"]

        for sheet in sheets_properties:
            title = sheet["properties"]["title"]
            id = sheet["properties"]["sheetId"]

            self.current_sheets[title] = {"id": id, "next_row": 1}

    def build_spreadsheet(self, filename, folder_id) -> dict:
        """Create a google sheet in the "parents" folder."""

        drive = build("drive", "v3", credentials=self.creds)
        file_metadata = {
            "name": filename,
            "parents": [folder_id],
            "mimeType": "application/vnd.google-apps.spreadsheet",
        }
        response = drive.files().create(body=file_metadata).execute()

        self.sheet = self.service.spreadsheets()
        self.spreadsheet_id = response["id"]
        self.current_sheets = {"Sheet1": {"id": 0, "next_row": 1}}

    def get_values_by_range(self, cell_range: str) -> Optional[dict]:
        """Returns the values of a specified range."""

        response = (
            self.sheet.values()
            .get(spreadsheetId=self.spreadsheet_id, range=cell_range)
            .execute()
        )
        return response.get("values")

    def get_next_row(self, sheet_name: str) -> int:
        """Returns the last row number that has been appended to the specified sheet."""

        return self.current_sheets[sheet_name]["next_row"]

    def set_file_and_folder_info(self, file_and_folder_info: tuple) -> None:
        """Set the filename and folder information for the sheet export."""

        self.filename = file_and_folder_info[0]
        self.folder_id = file_and_folder_info[1]

    def values_batch_update(self) -> None:
        """Batch updates all current value requests."""

        values_body = {
            "valueInputOption": "USER_ENTERED",
            "data": self.update_values_requests,
        }
        self.sheet.values().batchUpdate(
            spreadsheetId=self.spreadsheet_id, body=values_body
        ).execute()
        self.update_values_requests.clear()

    def batch_update(self) -> None:
        """Batch updates all current requests."""

        body: dict = {"requests": self.requests}
        self.sheet.batchUpdate(spreadsheetId=self.spreadsheet_id, body=body).execute()
        self.requests.clear()

    def append_values(self, value: list, range: str = "A1") -> None:
        """Append a value to the end of the target spreadsheet."""

        body: dict = {"values": value}
        self.sheet.values().append(
            spreadsheetId=self.spreadsheet_id,
            range=range,
            valueInputOption="USER_ENTERED",
            body=body,
        ).execute()

    def add_values_request(self, cell_range: str, rows: list) -> None:
        """Add values in a range."""

        processed_range: tuple = self.process_range(cell_range)
        sheet_name: str = cell_range.split("!")[0]
        # Rows start at 0 behind the scenes. +1 match spreadsheet starting at 1.
        next_row: int = (processed_range[2] + 1) + len(rows)

        # Check if you are adding to the end of the sheet.
        # next_row will be greater than current_sheet:next_row if adding to the end.
        if self.current_sheets[sheet_name]["next_row"] < next_row:
            self.current_sheets[sheet_name]["next_row"] = next_row

        self.update_values_requests.append({"range": cell_range, "values": rows})

    def change_google_sheet_title_request(self, name: str) -> None:
        "Change the name of the google sheet."

        self.requests.append(
            {
                "updateSpreadsheetProperties": {
                    "properties": {"title": f"{name}"},
                    "fields": "title",
                }
            }
        )

    def change_sheet_name_request(self, old_name: str, new_name: str) -> None:
        """Change the name of the specified sheet."""

        self.current_sheets[new_name] = self.current_sheets[old_name]
        del self.current_sheets[old_name]

        self.requests.append(
            {
                "updateSheetProperties": {
                    "properties": {
                        "sheetId": self.current_sheets[new_name]["id"],
                        "title": f"{new_name}",
                    },
                    "fields": "title",
                }
            }
        )

    def add_sheet_request(self, name: str) -> None:
        """Add a new sheet request to the Google Sheet."""

        self.current_sheets[name] = {"id": self.sheet_id_runner, "next_row": 0}
        self.sheet_id_runner += 1

        self.requests.append(
            {
                "addSheet": {
                    "properties": {
                        "sheetId": self.current_sheets[name]["id"],
                        "title": f"{name}",
                    }
                }
            }
        )

    def set_sheet_grid_properties_request(
        self, name: str, number_of_rows: int = 1000, number_of_columns: int = 26
    ):
        """Changes the rows and columns for a sheet."""

        new_grid_properties = {
            "rowCount": number_of_rows,
            "columnCount": number_of_columns,
        }

        self.requests.append(
            {
                "updateSheetProperties": {
                    "properties": {
                        "sheetId": self.current_sheets[name]["id"],
                        "gridProperties": new_grid_properties,
                    },
                    "fields": "gridProperties",
                }
            }
        )

    def resize_request(self, cell_range: str, size: int, range_as_ints=False) -> None:
        """Resize a column or row by specified number of pixels.
        Range formats:
            - Columns: "SheetName!StartColumn:EndColumn "
                - Ex. "Sheet1!A:A" will resize column A.
            - Rows: "SheetName!StartRow:EndRow"
                - Ex. "Sheet1!1:1" will resize row 1.
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
        self.requests.append(format_style)

    def align_and_wrap_cells_range_request(
        self,
        cell_range: str,
        horizontal: str = "LEFT",
        vertical: str = "BOTTOM",
        wrapping: str = "CLIP",
        range_as_ints=False,
    ) -> None:
        """Align and wrap cells in the provided range based on alignment provided.
        Alignment:
            - Horizontal: LEFT, CENTER, RIGHT
            - Vertical: TOP, MIDDLE, BOTTOM
        Wrapping: OVERFLOW_CELL, CLIP, WRAP
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
        self.requests.append(format_style)

    def merge_cells_range_request(
        self, cell_range: str, merge_type: str = "MERGE_ALL", range_as_ints=False
    ) -> None:
        """Merge cells in the provided range based on merge type.
        Merge Types: MERGE_ALL, MERGE_COLUMNS, MERGE_ROWS
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
        self.requests.append(format_style)

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
        """Set the font for a range of cells."""

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
        self.requests.append(format_style)

    def fill_range_request(
        self, cell_range: str, fill_color: tuple = (1, 1, 1), range_as_ints=False
    ) -> None:
        """Set the background fill for a range of cells.
        Amount of (Red, Green, Blue)
            - Red: 0.0 - 1.0
            - Green: 0.0 - 1.0
            - Blue:  0.0 - 1.0
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
        self.requests.append(format_style)

    def set_outer_border_range_request(
        self,
        cell_range: str,
        type: str = "SOLID",
        color: tuple = (0, 0, 0),
        range_as_ints=False,
    ) -> None:
        """Set the outer border for a range of cells.
        Border types:
            - DOTTED
            - DASHED
            - SOLID
            - SOLID_MEDIUM
            - SOLID_THICK
            - NONE
            - DOUBLE
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
        self.requests.append(border_format)

    def set_bottom_border_range_request(
        self,
        cell_range: str,
        type: str = "SOLID",
        color: tuple = (0, 0, 0),
        range_as_ints=False,
    ) -> None:
        """Set the bottom border for a range of cells.
        Border types:
            - DOTTED
            - DASHED
            - SOLID
            - SOLID_MEDIUM
            - SOLID_THICK
            - NONE
            - DOUBLE
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
        self.requests.append(border_format)

    def process_range(self, cell_range: str) -> tuple:
        """
        Process the range into sheet_id and starting and ending cell.
        cell_range format: 'SheetName!A1:AZ100'
        """

        range_parts: list = cell_range.split("!")
        sheet_id: int = self.current_sheets[range_parts[0]]["id"]
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
        """
        Process the range into sheet_id and starting and ending cell as ints.
        cell_range format: 'sheet_id,start_column,start_row,end_column,end_row'
        """

        cell_range = cell_range.split(",")
        sheet_id: int = self.current_sheets[cell_range[0]]["id"]

        return (
            sheet_id,
            int(cell_range[1]),
            int(cell_range[2]),
            int(cell_range[3]),
            int(cell_range[4]),
        )

    def process_cell_pair(self, pair: str) -> list:
        """Determine the numerical value for the cell location."""

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

        return [base_columns[alpha_chars], int(num_chars)]

    def clear_spreadsheet_values(self, sheet_name: str) -> None:
        """Clear the values on current targeted spreadsheet."""

        self.sheet.values().clear(
            spreadsheetId=self.spreadsheet_id, range=sheet_name
        ).execute()

    def clear_spreadsheet_colors(self, sheet_name: str) -> None:
        """Clear the colors on the current targeted spreadsheet."""

        sheet_props = self.get_spreadsheet_properties()
        last_row = sheet_props["sheets"][0]["properties"]["gridProperties"]["rowCount"]
        last_column = sheet_props["sheets"][0]["properties"]["gridProperties"][
            "columnCount"
        ]
        self.fill_range_request(
            f"{sheet_name},0,0,{last_column},{last_row}", (1, 1, 1), range_as_ints=True
        )

    def reset_spreadsheet_font(self, sheet_name: str) -> None:
        """Resets all cell fonts to base on targeted spreadsheet.
        Base Font: Arial, 10, Non-bold/italic/strike.
        """

        sheet_props = self.get_spreadsheet_properties()
        last_row = sheet_props["sheets"][0]["properties"]["gridProperties"]["rowCount"]
        last_column = sheet_props["sheets"][0]["properties"]["gridProperties"][
            "columnCount"
        ]
        self.format_font_range_request(
            f"{sheet_name},0,0,{last_column},{last_row}", range_as_ints=True
        )


if __name__ == "__main__":
    print("This is a module...")
