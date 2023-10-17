# Google Sheets API Doc: https://developers.google.com/sheets/api/reference/rest
# https://developers.google.com/resources/api-libraries/documentation/sheets/v4/python/latest/index.html

import os
import json

from googleapiclient.errors import HttpError

import google_drive_tool as gdt
from google_drive_tool.chart import Chart


def main():
    dir = os.path.dirname(os.path.realpath(__file__))
    g_info_path = os.path.join(dir, "secrets", "google_info.json")
    general_info_path = os.path.join(dir, "secrets", "info.json")
    
    with open(general_info_path) as f:
        general_info = json.load(f)

    tool = gdt.SheetTool()
    tool.setup(g_info_path)
    tool.set_spreadsheet(general_info["sheet_id"])
        
    line_chart = Chart(
        tool.get_sheet_id("Sheet3"),
        (5, 5),
        tool.process_range("Sheet3!A1:A43"),
        chart_type="LINE",
        title="My Chart",
    )
    line_chart.add_axis(title="X Title", position="BOTTOM_AXIS")
    line_chart.add_axis(title="Y Title", position="LEFT_AXIS")
    line_chart.add_line_series(tool.process_range("Sheet3!B1:B43"), color=(1, 0, 0))
    line_chart.add_line_series(tool.process_range("Sheet3!C1:C43"), color=(0, 1, 0))
    line_chart.setup_chart()
    tool.add_external_request(line_chart.get_request_body())

    bar_chart = Chart(
        tool.get_sheet_id("Sheet4"),
        (5, 5),
        tool.process_range("Sheet4!A1:A6"),
        chart_type="COLUMN",
        title="My Chart",
    )
    bar_chart.add_axis(title="Flavor", position="BOTTOM_AXIS")
    bar_chart.add_axis(title="Votes", position="LEFT_AXIS")
    bar_chart.add_bar_series(tool.process_range("Sheet4!B1:B6"), color=(1, 0, 0), target_axis="LEFT_AXIS")
    bar_chart.add_bar_series(tool.process_range("Sheet4!C1:C6"), color=(0, 1, 0), target_axis="LEFT_AXIS")
    bar_chart.setup_chart()
    tool.add_external_request(bar_chart.get_request_body())

    tool.batch_update()


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