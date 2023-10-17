from google_drive_tool.formatting import Color, format_color, format_range
    

class Chart:
    """A base chart for a Google Sheet.
    Not to be used directly.
    """

    def __init__(self):
        self.__chart = {
            "position": None,
            "spec": {
                "basicChart": None
            },
        }

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

    def set_legend(self, position: str="BOTTOM_LEGEND"):
        self.__chart["spec"]["basicChart"]["legendPosition"] = position

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

    def set_spec(
        self,
        chart_type: str,
        header_count: int=1,
    ):
        self.__chart["spec"]["basicChart"] = {
            "chartType": chart_type,
            "axis": [],
            "domains": [],
            "series": [],
            "headerCount": header_count,
            "legendPosition": "NO_LEGEND",
        }
    
    def set_domain(
        self,
        domain_range: tuple,
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
        font: dict=None,

    ):
        self.__chart["spec"]["basicChart"]["axis"].append(            
            {
                "position": position,
                "title": title,
                "titleTextPosition": {
                    "horizontalAlignment": alignment,
                },
                "format": font if font else create_font(),
            }
        )

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


def create_font(
    font_family: str="Arial",
    font_size: int=10,
    bold: bool=False,
    italic: bool=False,
    color: tuple=Color.BLACK,
) -> dict:
    """Format a font."""

    return {
        "fontFamily": font_family,
        "fontSize": font_size,
        "bold": bold,
        "italic": italic,
        "foregroundColorStyle": {
            "rgbColor": format_color(color),
        },
    }