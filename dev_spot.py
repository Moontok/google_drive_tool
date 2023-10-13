# Google Sheets API Doc: https://developers.google.com/sheets/api/reference/rest
# https://developers.google.com/resources/api-libraries/documentation/sheets/v4/python/latest/index.html

import os
import json

from googleapiclient.errors import HttpError

import google_drive_tool as gdt


def main():
    dir = os.path.dirname(os.path.realpath(__file__))
    g_info_path = os.path.join(dir, "secrets", "google_info.json")
    general_info_path = os.path.join(dir, "secrets", "info.json")
    
    with open(general_info_path) as f:
        general_info = json.load(f)

    tool = gdt.SheetTool()
    tool.setup(g_info_path)

    try:
        tool.set_spreadsheet(general_info["sheet_id"])
        
        tool.add_values_request("Sheet1!A24", [[99]])
        tool.batch_update_values()


    except HttpError as e:
        print(f"Error with communicating with Google:\n{e}")
    except KeyError as e:
        print(f"Error with key:\n{e}")


def json_pretty_dump(data: dict, file_name: str) -> None:
    """Create a pretty json file from a dict

    Args:
        data (dict): Data to be dumped
        file_name (str): Name of the file
    """

    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()