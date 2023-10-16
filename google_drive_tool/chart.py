class Chart:
    """A chart for a Google Sheet."""

    def __init__(
        self,
        sheet_id: int,
        anchor_cell: tuple,
        domain_range: tuple,
        chart_type: str,
        width: int = 600,
        height: int = 371,
        font: str = "Arial",
        alt_text: str = "A chart.",
        title: str = "The Title",
        alignment: str = "CENTER",
        color: tuple = (0, 0, 0),
        font_size: int = 10,
        bold: bool = False,
        italic: bool = False,
        bg_color: tuple = (1, 1, 1),
        subtitle: str = "",
        subtitle_font_size: int = 10,
        subtitle_bold: bool = False,
        subtitle_italic: bool = False,
        has_legend: bool = True,
        legend_position: str = "BOTTOM_LEGEND",
    ):
        # Values passed in
        self.__sheet_id = sheet_id
        self.__anchor_cell = anchor_cell
        self.__domain_range = domain_range
        self.__chart_type = chart_type
        self.__width = width
        self.__height = height
        self.__font = font
        self.__alt_text = alt_text
        self.__title = title
        self.__alignment = alignment
        self.__color = color
        self.__font_size = font_size
        self.__bold = bold
        self.__italic = italic
        self.__bg_color = bg_color
        self.__subtitle = subtitle
        self.__subtitle_font_size = subtitle_font_size
        self.__subtitle_bold = subtitle_bold
        self.__subtitle_italic = subtitle_italic
        self.__has_legend = has_legend
        self.__legend_position = legend_position
        self.__chart_body = {}
        self.__axis_list = []
        self.__series = []
        self.__chart_style = "basicChart"

    def setup_chart(self) -> None:
        """Setup the chart."""

        self.__chart_body = {
            "addChart": {
                "chart": {
                    "position": {
                        "overlayPosition": {
                            "widthPixels": self.__width,
                            "heightPixels": self.__height,
                            "anchorCell": {
                                "sheetId": self.__sheet_id,
                                "columnIndex": self.__anchor_cell[0],
                                "rowIndex": self.__anchor_cell[1],
                            },
                        },
                    },
                    "spec": {
                        "fontName": self.__font,
                        "altText": self.__alt_text,
                        "title": self.__title,
                        "titleTextFormat": {
                            "foregroundColorStyle": {
                                "rgbColor": {self._format_color(self.__color)},
                            },
                            "fontFamily": self.__font,
                            "fontSize": self.__font_size,
                            "bold": self.__bold,
                            "italic": self.__italic,
                        },
                        "titleTextPosition": {
                            "horizontalAlignment": self.__alignment,
                        },
                        "subtitle": self.__subtitle if self.__subtitle != "" else "",
                        "subtitleTextFormat": {
                            "foregroundColorStyle": {
                                "rgbColor": {self._format_color(self.__color)},
                            },
                            "fontFamily": self.__font,
                            "fontSize": self.__subtitle_font_size,
                            "bold": self.__subtitle_bold,
                            "italic": self.__subtitle_italic,
                        },
                        "subtitleTextPosition": {
                            "horizontalAlignment": self.__alignment,
                        },
                        "backgroundColorStyle": {
                            "rgbColor": {self._format_color(self.__bg_color)},
                        },
                        "basicChart": self._setup_chart_part(
                            domain_range=self.__domain_range,
                            has_legend=self.__has_legend,
                            legend_position=self.__legend_position,
                        ),
                    },
                },
            }
        }

    def _setup_chart_part(
        self,
        domain_range: tuple = tuple(),
        has_legend: bool = True,
        legend_position: str = "BOTTOM_LEGEND",
        num_of_headers: int = 1,
    ) -> dict:
        """Set the chart parts.

        Args:
            domain_range (tuple, optional): The range of the domain. Defaults to tuple().
            has_legend (bool, optional): Whether the chart has a legend. Defaults to True.
            legend_position (str, optional): The position of the legend. Defaults to "BOTTOM_LEGEND".
            num_of_headers (int, optional): The number of headers. Defaults to 1.

        Returns:
            dict: The chart parts
        """

        return {
            "chartType": self.__chart_style,
            "legendPosition": legend_position if has_legend else "NO_LEGEND",
            "axis": [self.__axis_list],
            "domains": [
                {
                    "domain": {
                        "sourceRange": {
                            "sources": [{self._format_range(domain_range)}],
                        },
                    },
                },
            ],
            "series": self.__series,
            "headerCount": num_of_headers,
        }

    def add_axis(
        self,
        position: str = "BOTTOM_AXIS",
        title: str = "X Axis Title",
        alignment: str = "CENTER",
        font: str = "Arial",
        is_bold: bool = False,
        is_italic: bool = False,
        color: tuple = (0, 0, 0),
    ) -> None:
        """Add an axis. Need an X and Y axis for a line chart.

        Args:
            position (str, optional): The position of the axis. Defaults to "BOTTOM_AXIS".
            title (str, optional): The title of the axis. Defaults to "X Axis Title".
            alignment (str, optional): The alignment of the title. Defaults to "CENTER".
            font (str, optional): The font of the title. Defaults to "Arial".
            is_bold (bool, optional): Whether the title is bold. Defaults to False.
            is_italic (bool, optional): Whether the title is italic. Defaults to False.
            color (tuple, optional): The color of the title. Defaults to (0, 0, 0).

        Returns:
            dict: The axis
        """

        self.__axis_list.append(
            {
                "position": position,
                "title": title,
                "titleTextPosition": {
                    "horizontalAlignment": alignment,
                },
                "format": {
                    "fontFamily": font,
                    "fontSize": self.__font_size,
                    "italic": is_italic,
                    "bold": is_bold,
                    "foregroundColorStyle": {
                        "rgbColor": {self._format_color(color)},
                    },
                },
            }
        )

    def add_series(
        self,
        range: tuple = tuple(),
        target_axis: str = "LEFT_AXIS",
        color: tuple = (0, 0, 0),
        line_width: int = 3,
        line_style: str = "SOLID",
    ) -> None:
        """Add a series to the chart.

        Args:
            range (tuple, optional): The range of the series. Defaults to tuple().
            target_axis (str, optional): The axis the series is on. Defaults to "LEFT_AXIS".
            color (tuple, optional): The color of the series. Defaults to (0, 0, 0).
            line_width (int, optional): The width of the line. Defaults to 3.
            line_style (str, optional): The style of the line. Defaults to "SOLID".
        """

        self.__series.append(
            {
                "targetAxis": target_axis,
                "lineStyle": {
                    "width": line_width,
                    "type": line_style,
                },
                "colorStyle": {
                    "rgbColor": {self._format_color(color)},
                },
                "series": {
                    "sourceRange": {
                        "sources": [{self._format_range(range)}],
                    },
                },
            }
        )

    def _format_color(self, color: tuple) -> dict:
        """Format a color.

        Args:
            color (tuple): The color to format

        Returns:
            dict: The formatted color
        """

        return {
            "red": color[0],
            "green": color[1],
            "blue": color[2],
        }

    def _format_range(self, range: tuple) -> dict:
        """Format a range.

        Args:
            range (tuple): The range to format

        Returns:
            dict: The formatted range
        """

        return {
            "sheetId": range[0],
            "startColumnIndex": range[1],
            "startRowIndex": range[2],
            "endColumnIndex": range[3],
            "endRowIndex": range[4],
        }

    def get_request_body(self) -> dict:
        """Get the request body for the chart.

        Returns:
            dict: The request body
        """
        return self.__chart_body
