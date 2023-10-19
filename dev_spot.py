# Google Sheets API Doc: https://developers.google.com/sheets/api/reference/rest
# https://developers.google.com/resources/api-libraries/documentation/sheets/v4/python/latest/index.html

import os
import json

from googleapiclient.errors import HttpError

import google_drive_tool.sheets as st
from google_drive_tool.chart import LineChart, ColumnChart, ScatterChart, PieChart
from google_drive_tool.formatting import Color, ChartLine, chart_font_format


def main():
    dir = os.path.dirname(os.path.realpath(__file__))
    g_info_path = os.path.join(dir, "secrets", "google_info.json")
    general_info_path = os.path.join(dir, "secrets", "info.json")
    
    with open(general_info_path) as f:
        general_info = json.load(f)

    tool = st.SheetTool()
    tool.setup(g_info_path)
    tool.set_spreadsheet(general_info["sheet_id"])

    tool.resize_request("Sheet3!A:B", 200)
    tool.resize_request("Sheet3!3:3", 100)

    tool.batch_update()


def create_pie_chart(tool):
    pie_chart = PieChart()
    pie_chart.set_position(
        tool.get_sheet_id("Sheet4"),
        (4, 5),
        (600, 400),
    )
    pie_chart.set_title("This is a title")
    pie_chart.set_subtitle("This is a subtitle")
    pie_chart.set_legend()
    pie_chart.set_domain(tool.process_range("Sheet4!A1:A6"))
    pie_chart.set_pie_hole_size(0.5)
    pie_chart.add_series(
        tool.process_range("Sheet4!B1:B6")
    )
    request = pie_chart.chart_request()
    tool.add_general_request(request)


def create_line_chart(tool):
    line_chart = LineChart()
    line_chart.set_position(
        tool.get_sheet_id("Sheet4"),
        (10, 26),
        (600, 400),
    )

    # Line Chart
    line_chart.set_title("This is a title")
    line_chart.set_subtitle("This is a subtitle")
    line_chart.set_legend()
    line_chart.set_domain(tool.process_range("Sheet4!A9:A51"))
    line_chart.add_axis(title="X Label", position="BOTTOM_AXIS")
    line_chart.add_axis(title="Y Label", position="LEFT_AXIS")
    line_chart.add_series(
        tool.process_range("Sheet4!B9:B51"),
        target_axis="LEFT_AXIS",
        color=Color.RED,
    )
    line_chart.set_line_smoothing(True)
    line_chart.set_series_line_style(0, ChartLine.DOTTED, 10)
    line_chart.add_series(
        tool.process_range("Sheet4!C9:C51"),
        target_axis="LEFT_AXIS",
        color=Color.GREEN,
    )
    request = line_chart.chart_request()
    tool.add_general_request(request)

def create_column_chart(tool):
    # Column Chart
    column_chart = ColumnChart()
    column_chart.set_position(
        tool.get_sheet_id("Sheet4"),
        (10, 5),
        (600, 400),
    )
    column_chart.set_title("This is a title")
    column_chart.set_subtitle("This is a subtitle")
    column_chart.set_legend()
    column_chart.set_domain(tool.process_range("Sheet4!A1:A6"))
    column_chart.add_axis(title="X Label", position="BOTTOM_AXIS")
    column_chart.add_axis(title="Y Label", position="LEFT_AXIS")
    column_chart.add_series(
        tool.process_range("Sheet4!B1:B6"),
        target_axis="LEFT_AXIS",
        color=Color.RED,
    )
    column_chart.add_series(
        tool.process_range("Sheet4!C1:C6"),
        target_axis="LEFT_AXIS",
        color=Color.GREEN,
    )
    request = column_chart.chart_request()
    tool.add_general_request(request)

def create_scatter_chart(tool):
    # Scatter Chart
    scatter_chart = ScatterChart()
    scatter_chart.set_position(
        tool.get_sheet_id("Sheet4"),
        (4,26),
        (600, 400),
    )
    scatter_chart.set_title("This is a title")
    scatter_chart.set_subtitle("This is a subtitle")
    scatter_chart.set_legend()
    scatter_chart.set_domain(tool.process_range("Sheet4!A9:A51"))
    scatter_chart.add_axis(title="X Label", position="BOTTOM_AXIS")
    scatter_chart.add_axis(title="Y Label", position="LEFT_AXIS")
    scatter_chart.add_series(
        tool.process_range("Sheet4!B9:B51"),
        target_axis="LEFT_AXIS",
        color=Color.RED,
    )
    scatter_chart.add_series(
        tool.process_range("Sheet4!C9:C51"),
        target_axis="LEFT_AXIS",
        color=Color.GREEN,
    )
    scatter_chart.set_background_color((.9, .9, 1))
    scatter_chart.set_font_family("Consolas")
    request = scatter_chart.chart_request()
    tool.add_general_request(request)


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