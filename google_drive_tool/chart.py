from google_drive_tool.formatting import Color, format_color, format_range, chart_font_format
    

class Chart:
    """A base chart for a Google Sheet.
    Not to be used directly.
    """

    def __init__(self, chart_type: str="NONE"):
        self.__chart: dict = {
            "position": None,
            "spec": {
                "basicChart": {
                    "chartType": chart_type,
                    "axis": [],
                    "domains": [],
                    "series": [],
                    "legendPosition": "NO_LEGEND",
                },
                "altText": "A Chart.",
            },
        }

    def set_chart_id(self, chart_id: int):
        self.__chart["chartId"] = chart_id

    def set_title(self, title: str, alignment: str="CENTER"):
        self.__chart["spec"]["title"] = title
        self.__chart["spec"]["titleTextPosition"] = {
            "horizontalAlignment": alignment,
        }

    def set_title_font(self, font: dict):
        self.__chart["spec"]["titleTextFormat"] = font

    def set_subtitle(self, subtitle: str, alignment: str="CENTER"):
        self.__chart["spec"]["subtitle"] = subtitle
        self.__chart["spec"]["subtitleTextPosition"] = {
            "horizontalAlignment": alignment,
        }

    def set_subtitle_font(self, font: dict):
        self.__chart["spec"]["subtitleTextFormat"] = font

    def set_alt_text(self, alt_text: str):
        self.__chart["spec"]["altText"] = alt_text

    def set_legend(self, position: str="BOTTOM_LEGEND"):
        self.__chart["spec"]["basicChart"]["legendPosition"] = position

    def set_background_color(self, color: tuple):
        self.__chart["spec"]["backgroundColor"] = format_color(color)

    def set_font_family(self, font_family: str):
        self.__chart["spec"]["fontName"] = font_family

    def set_position(
        self,
        sheet_id: int,
        anchor_cell: tuple,
        size: tuple,
    ):
        self.__chart["position"] = {
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
    
    def set_domain(
        self,
        domain_range: tuple,
        header_count: int=1,
    ):
        self.__chart["spec"]["basicChart"]["domains"].append(
            {
                "domain": {
                    "sourceRange": {
                        "sources": [format_range(domain_range)],
                    },
                },
            },
        )

        self.__chart["spec"]["basicChart"]["headerCount"] = header_count

    def add_series(
        self,
        series_range: tuple,
        target_axis: str="LEFT_AXIS",
        color: tuple=Color.BLACK,
    ):
        self.__chart["spec"]["basicChart"]["series"].append(
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
        self.__chart["spec"]["basicChart"]["axis"].append(            
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
        self.__chart["spec"]["basicChart"]["axis"][location]["viewWindowOptions"] = {
            "viewWindowMin": min,
            "viewWindowMax": max,
        }

    def set_axis_font(self, location: int, font: dict):
        self.__chart["spec"]["basicChart"]["axis"][location]["format"] = font

    def add_border(
        self,
        color: tuple=Color.BLACK,
    ):
        self.__chart["border"] = {
            "colorStyle": format_color(color),
        }

    def chart_request(self) -> dict:
        if not self.__chart["position"]:
            raise ValueError("Chart position not set")
        if not self.__chart["spec"]["basicChart"]:
            raise ValueError("Chart type not set")
        if len(self.__chart["spec"]["basicChart"]["domains"]) == 0:
            raise ValueError("Chart domain not set")
        if len(self.__chart["spec"]["basicChart"]["series"]) == 0:
            raise ValueError("Chart series not set")
        if len(self.__chart["spec"]["basicChart"]["axis"]) == 0:
            raise ValueError("Chart axis not set")
        
        return {
            "addChart": {
                "chart": self.__chart
            }
        }
    

class LineChart(Chart):
    def __init__(self):
        super().__init__("LINE")

    def set_series_line_style(
        self,
        location: int,
        line_style: str,
        line_width: int,
    ):
        self._Chart__chart["spec"]["basicChart"]["series"][location]["lineStyle"] = {
            "width": line_width,
            "type": line_style,
        }

    def set_line_smoothing(self, smoothing: bool):
        self._Chart__chart["spec"]["basicChart"]["lineSmoothing"] = smoothing

        
class ScatterChart(Chart):
    def __init__(self):
        super().__init__("SCATTER")

    def add_trendline(
        self,
        trendline_type: str="LINEAR",
        color: tuple=Color.BLACK,
    ):
        self._Chart__chart["spec"]["basicChart"]["series"][0]["trendline"] = [{
            "type": trendline_type,
        }]


class ColumnChart(Chart):
    def __init__(self):
        super().__init__("COLUMN")