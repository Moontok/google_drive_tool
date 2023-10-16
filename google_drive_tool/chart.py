
class Chart:
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
        
        # Not Set
        self.chart_body = {}
        self.chart_type = "basicChart"
        self.axis_list = []
        self.series = []

    def setup_chart(self) -> dict:
        """Setup the chart."""

        self.chart_body =  {
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
                                "rgbColor": {
                                    "red": self.__color[0],
                                    "green": self.__color[1],
                                    "blue": self.__color[2],
                                },
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
                                "rgbColor": {
                                    "red": self.__color[0],
                                    "green": self.__color[1],
                                    "blue": self.__color[2],
                                },
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
                            "rgbColor": {
                                "red": self.__bg_color[0],
                                "green": self.__bg_color[1],
                                "blue": self.__bg_color[2],
                            },
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
    ):
        """Set the chart types
        """

        return {
            "chartType": self.__chart_type,
            "legendPosition": legend_position if has_legend else "NO_LEGEND",    
            "axis": [
                self.axis_list
            ],
            "domains": [
                {
                    "domain": {
                        "sourceRange": {
                            "sources": [
                                {
                                    "sheetId": domain_range[0],
                                    "startColumnIndex": domain_range[1],
                                    "startRowIndex": domain_range[2],
                                    "endColumnIndex": domain_range[3],
                                    "endRowIndex":  domain_range[4],
                                },
                            ],
                        },
                    },
                },
            ],
            "series": self.series,
            "headerCount": num_of_headers,
        }


    def add_axis(
            self,
            position: str = "BOTTOM_AXIS",
            title: str = "X Axis Title",
            alignment: str = "CENTER",
            font: str = "Arial",
            isBold: bool = False,
            isItalic: bool = False,
            color: tuple = (0, 0, 0),
    ):
        """Add an axis. Need an X and Y axis for a line chart.

        Args:
            position (str, optional): The position of the axis. Defaults to "BOTTOM_AXIS".
            title (str, optional): The title of the axis. Defaults to "X Axis Title".
            alignment (str, optional): The alignment of the title. Defaults to "CENTER".
            font (str, optional): The font of the title. Defaults to "Arial".
            isBold (bool, optional): Whether the title is bold. Defaults to False.
            isItalic (bool, optional): Whether the title is italic. Defaults to False.
            color (tuple, optional): The color of the title. Defaults to (0, 0, 0).

        Returns:
            dict: The axis
        """

        self.axis_list.append(
            {
                "position": position,
                "title": title,
                "titleTextPosition": {
                    "horizontalAlignment": alignment,
                },
                "format": {
                    "fontFamily": font,
                    "fontSize": self.__font_size,
                    "italic": isItalic,
                    "bold": isBold,
                    "foregroundColorStyle": {
                        "rgbColor": {
                            "red": color[0],
                            "green": color[1],
                            "blue": color[2],
                        },
                    },
                },
            }
        )

    def add_series(
            self,
            series_name: str,
            range: tuple = tuple(),
            target_axis: str = "LEFT_AXIS",
            color: tuple = (0, 0, 0),
            line_width: int = 3,
            line_style: str = "SOLID",
        ):
        """Add a series to the chart.

        Args:
            range (tuple, optional): The range of the series. Defaults to tuple().
            target_axis (str, optional): The axis the series is on. Defaults to "LEFT_AXIS".
            color (tuple, optional): The color of the series. Defaults to (0, 0, 0).
            line_width (int, optional): The width of the line. Defaults to 3.
            line_style (str, optional): The style of the line. Defaults to "SOLID".
        """

        self.series.append(
            { 
                "targetAxis": target_axis,
                "lineStyle": {
                    "width": line_width,
                    "type": line_style,
                },
                "colorStyle": {
                    "rgbColor": {
                        "red": color[0],
                        "green": color[1],
                        "blue": color[2],
                    },
                },
                "series": {
                    "sourceRange": {
                        "sources": [
                            {
                                "sheetId": range[0],
                                "startColumnIndex": range[1],
                                "startRowIndex": range[2],
                                "endColumnIndex": range[3],
                                "endRowIndex": range[4],
                            },
                        ],
                    },
                },
            }
        )

    def get_request_body(self) -> dict:
        """Get the request body for the chart.
        
        Returns:
            dict: The request body
        """
        return self.chart_body