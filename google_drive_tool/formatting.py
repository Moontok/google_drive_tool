class Color():
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