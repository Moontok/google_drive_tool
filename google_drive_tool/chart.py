from google_drive_tool.formatting import Color, format_color, format_range, chart_font_format
    

class Chart:
    """A base chart for a Google Sheet.
    Not to be used directly.
    """

    def __init__(self, chart_type: str):
        self._chart_type: str = chart_type
        self._chart: dict = {
            "position": None,
            "spec": {
                chart_type: {},
                "altText": "A Chart.",
            },
        }

    def set_chart_id(self, chart_id: int):
        self._chart["chartId"] = chart_id

    def set_title(self, title: str, alignment: str="CENTER"):
        self._chart["spec"]["title"] = title
        self._chart["spec"]["titleTextPosition"] = {
            "horizontalAlignment": alignment,
        }

    def set_title_font(self, font: dict):
        self._chart["spec"]["titleTextFormat"] = font

    def set_subtitle(self, subtitle: str, alignment: str="CENTER"):
        self._chart["spec"]["subtitle"] = subtitle
        self._chart["spec"]["subtitleTextPosition"] = {
            "horizontalAlignment": alignment,
        }

    def set_subtitle_font(self, font: dict):
        self._chart["spec"]["subtitleTextFormat"] = font

    def set_alt_text(self, alt_text: str):
        self._chart["spec"]["altText"] = alt_text

    def set_legend(self, position: str="BOTTOM_LEGEND"):
        self._chart["spec"][self._chart_type]["legendPosition"] = position

    def set_background_color(self, color: tuple):
        self._chart["spec"]["backgroundColorStyle"] = {
            "rgbColor": format_color(color)
        }

    def set_font_family(self, font_family: str):
        self._chart["spec"]["fontName"] = font_family

    def set_position(
        self,
        sheet_id: int,
        anchor_cell: tuple,
        size: tuple,
    ):
        self._chart["position"] = {
            "overlayPosition": {
                "anchorCell": {
                    "sheetId": sheet_id,
                    "columnIndex": anchor_cell[0],
                    "rowIndex": anchor_cell[1],
                },
                "widthPixels": size[0],
                "heightPixels": size[1],
            },
        }

    def add_border(
        self,
        color: tuple=Color.BLACK,
    ):
        self._chart["border"] = {
            "colorStyle": format_color(color),
        }

    def chart_request(self) -> dict:
        if not self._chart["position"]:
            raise ValueError("Chart position not set")
        if not self._chart["spec"][self._chart_type]:
            raise ValueError("Chart type not set")
        if self._chart_type == "basicChart":
            if len(self._chart["spec"][self._chart_type]["domains"]) == 0:
                raise ValueError("Chart domain not set")
            if len(self._chart["spec"][self._chart_type]["series"]) == 0:
                raise ValueError("Chart series not set")
            if len(self._chart["spec"][self._chart_type]["axis"]) == 0:
                raise ValueError("Chart axis not set")
        
        return {
            "addChart": {
                "chart": self._chart
            }
        }


class BasicChart(Chart):
    def __init__(self, basic_chart_type: str):
        super().__init__("basicChart")
        self._chart["spec"]["basicChart"] = {
            "chartType": basic_chart_type,
            "axis": [],
            "domains": [],
            "series": [],
            "legendPosition": "NO_LEGEND",
        }
    
    def set_domain(
        self,
        domain_range: tuple,
        header_count: int=1,
    ):
        self._chart["spec"][self._chart_type]["domains"].append(
            {
                "domain": {
                    "sourceRange": {
                        "sources": [format_range(domain_range)],
                    },
                },
            },
        )

        self._chart["spec"][self._chart_type]["headerCount"] = header_count

    def add_series(
        self,
        series_range: tuple,
        target_axis: str="LEFT_AXIS",
        color: tuple=Color.BLACK,
    ):
        self._chart["spec"][self._chart_type]["series"].append(
            {
                "series": {
                    "sourceRange": {
                        "sources": [format_range(series_range)],
                    },
                },
                "targetAxis": target_axis,
                "colorStyle": {
                    "rgbColor": format_color(color),
                },
            },
        )

    def add_axis(
        self,
        position: str="BOTTOM_AXIS",
        title: str="X Axis Title",
        alignment: str="CENTER",

    ):
        self._chart["spec"][self._chart_type]["axis"].append(            
            {
                "position": position,
                "title": title,
                "titleTextPosition": {
                    "horizontalAlignment": alignment,
                },
            }
        )

    def set_axis_view_window(
        self,
        location: int,
        min: int,
        max: int,
    ):
        self._chart["spec"][self._chart_type]["axis"][location]["viewWindowOptions"] = {
            "viewWindowMin": min,
            "viewWindowMax": max,
        }

    def set_axis_font(self, location: int, font: dict):
        self._chart["spec"][self._chart_type]["axis"][location]["format"] = font


class LineChart(BasicChart):
    def __init__(self):
        super().__init__("LINE")

    def set_series_line_style(
        self,
        location: int,
        line_style: str,
        line_width: int,
    ):
        self._chart["spec"]["basicChart"]["series"][location]["lineStyle"] = {
            "width": line_width,
            "type": line_style,
        }

    def set_line_smoothing(self, smoothing: bool):
        self._chart["spec"]["basicChart"]["lineSmoothing"] = smoothing

        
class ScatterChart(BasicChart):
    def __init__(self):
        super().__init__("SCATTER")


class ColumnChart(BasicChart):
    def __init__(self):
        super().__init__("COLUMN")


class PieChart(Chart):
    def __init__(self):
        super().__init__("pieChart")
    
    def set_domain(
        self,
        domain_range: tuple,
    ):
        self._chart["spec"]["pieChart"]["domain"] =  {
            "sourceRange": {
                "sources": [format_range(domain_range)],
            },
        }

    def add_series(
        self,
        series_range: tuple,
    ):
        self._chart["spec"]["pieChart"]["series"] = {
            "sourceRange": {
                "sources": [format_range(series_range)],
            },
        }

    def set_pie_hole_size(self, size: float):
        self._chart["spec"]["pieChart"]["pieHole"] = size

