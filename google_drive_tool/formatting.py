class Color:
    """A class to represent a color in RGB for easy
    predefined color selection.
    """

    RED = (1, 0, 0)
    GREEN = (0, 1, 0)
    BLUE = (0, 0, 1)
    BLACK = (0, 0, 0)
    WHITE = (1, 1, 1)
    YELLOW = (1, 1, 0)
    PURPLE = (1, 0, 1)
    CYAN = (0, 1, 1)
    ORANGE = (1, 0.5, 0)
    PINK = (1, 0.5, 0.5)
    GRAY = (0.5, 0.5, 0.5)
    BROWN = (0.5, 0.25, 0)
    LIME = (0.5, 1, 0)
    TEAL = (0, 0.5, 0.5)

class BorderLine:
    """A class to represent the line of a border."""

    NONE = "NONE"
    SOLID = "SOLID"
    DASHED = "DASHED"
    DOTTED = "DOTTED"
    SOLID_MEDIUM = "SOLID_MEDIUM"
    SOLID_THICK = "SOLID_THICK"
    DOUBLE = "DOUBLE"

class ChartLine:
    """A class to represent a line in a chart."""

    INVISIBLE = "INVISIBLE"
    SOLID = "SOLID"
    DOTTED = "DOTTED"
    MEDIUM_DASHED = "MEDIUM_DASHED"
    MEDIUM_DASHED_DOTTED = "MEDIUM_DASHED_DOTTED"
    LONG_DASHED = "LONG_DASHED"
    LONG_DASHED_DOTTED = "LONG_DASHED_DOTTED"



def format_color(color: tuple) -> dict:
    """Format a color.
    
    Args:
        color: A tuple of 3 floats between 0 and 1.
        
        Returns:
            A dict with the color formatted for the API.
    """

    return {
        "red": color[0],
        "green": color[1],
        "blue": color[2],
    }
    

def format_range(range: tuple) -> dict:
    """Format a range.
    
    Args:
        range: A tuple of 5 integers.
        
    Returns:
        A dict with the range formatted for the API.
    """

    return {
        "sheetId": range[0],
        "startColumnIndex": range[1],
        "startRowIndex": range[2],
        "endColumnIndex": range[3],
        "endRowIndex": range[4],
    }


def cell_font_format(
    font_family: str="Arial",
    font_size: int=10,
    color: tuple=Color.BLACK,
    bold: bool=False,
    italic: bool=False,
    strikethrough: bool=False,
    underline: bool=False,
) -> dict:
    """Format a font."""

    return {
        "fontFamily": font_family,
        "fontSize": font_size,
        "bold": bold,
        "italic": italic,
        "strikethrough": strikethrough,
        "underline": underline,
        "foregroundColorStyle": {
            "rgbColor": format_color(color),
        },
    }

def chart_font_format(
    font_family: str="Arial",
    font_size: int=10,
    color: tuple=Color.BLACK,
    bold: bool=False,
    italic: bool=False,
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