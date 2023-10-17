# Google Sheets API Doc: https://developers.google.com/sheets/api/reference/rest
# https://developers.google.com/resources/api-libraries/documentation/sheets/v4/python/latest/index.html

import os
import json

from googleapiclient.errors import HttpError

import google_drive_tool as gdt
from google_drive_tool.chart import Chart, create_font
from google_drive_tool.formatting import Color


def main():
    dir = os.path.dirname(os.path.realpath(__file__))
    g_info_path = os.path.join(dir, "secrets", "google_info.json")
    general_info_path = os.path.join(dir, "secrets", "info.json")
    
    with open(general_info_path) as f:
        general_info = json.load(f)

    tool = gdt.SheetTool()
    tool.setup(g_info_path)
    tool.set_spreadsheet(general_info["sheet_id"])

    line_chart = Chart()
    font = create_font(
        bold=True,
        font_size=14,
        font_family="Consolas",
    )
    line_chart.set_position(
        tool.get_sheet_id("Sheet4"),
        (4, 5),
        (600, 400),
    )
    line_chart.set_spec("LINE")
    line_chart.set_title("This is a title")
    line_chart.set_title_font(font)
    line_chart.set_subtitle("This is a subtitle")
    line_chart.set_subtitle_font(font)
    line_chart.set_legend()
    line_chart.set_domain(tool.process_range("Sheet4!A9:A51"))
    line_chart.add_axis(title="X Label", position="BOTTOM_AXIS")
    line_chart.add_axis(title="Y Label", position="LEFT_AXIS")
    line_chart.add_series(
        tool.process_range("Sheet4!B9:B51"),
        target_axis="LEFT_AXIS",
        color=Color.RED,
    )
    line_chart.add_series(
        tool.process_range("Sheet4!C9:C51"),
        target_axis="LEFT_AXIS",
        color=Color.GREEN,
    )
    request = line_chart.chart_request()
    tool.add_external_request(request)
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