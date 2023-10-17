
class Chart:
    pass

class LineChart(Chart):
    pass

class BarChart(Chart):
    pass

def get_font_json(
        font_family: str = "Arial",
        font_size: int = 10,
        bold: bool = False,
        italic: bool = False,
        color: tuple = (0, 0, 0),
    ):

        return{
            "fontFamily": font_family,
            "fontSize": font_size,
            "bold": bold,
            "italic": italic,
            "foregroundColorStyle": {
                "rgbColor": _format_color(color),
            },
        }

def get_axis_json(
    position: str = "BOTTOM_AXIS",
    title: str = "X Axis Title",
    alignment: str = "CENTER",
    font: dict = None,

):

    return {
        "position": position,
        "title": title,
        "titleTextPosition": {
            "horizontalAlignment": alignment,
        },
        "format": font if font else get_font_json(),
    }

def get_series_json(
    series_type: str = "LINE",
    range: tuple = tuple(),
    target_axis: str = "LEFT_AXIS",
    color: tuple = (0, 0, 0),
    line_width: int = None,
    line_style: str = None,
):
    series_json = {
            "targetAxis": target_axis,
            "colorStyle": {
                "rgbColor": _format_color(color),
            },
            "series": {
                "sourceRange": {
                    "sources": [_format_range(range)],
                },
            },
        }

    if series_type == "LINE":
        series_json["lineStyle"] = {
            "width": line_width,
            "type": line_style,
        }
    
    return series_json

def _format_range(range: tuple) -> dict:
    """Format a range."""

    return {
        "sheetId": range[0],
        "startColumnIndex": range[1],
        "startRowIndex": range[2],
        "endColumnIndex": range[3],
        "endRowIndex": range[4],
    }

def _format_color(color: tuple) -> dict:
    """Format a color."""

    return {
        "red": color[0],
        "green": color[1],
        "blue": color[2],
    }