from google_drive_tool.formatting import Color, format_color, format_range


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

    def set_chart_id(self, chart_id: int) -> None:
        """Set the chart ID for the chart. Use this if you want
        to update an existing chart. If you don't set this, a new
        chart will be created randomly by Google.

        Args:
            chart_id (int): The chart ID."""

        self._chart["chartId"] = chart_id

    def set_title(self, title: str, alignment: str = "CENTER") -> None:
        """Set the title of the chart.
        Alignment options:
            - "CENTER"
            - "LEFT"
            - "RIGHT"

        Args:
            title (str): The title of the chart.
            alignment (str, optional): The alignment of the title.
                Defaults to "CENTER".
        """

        self._chart["spec"]["title"] = title
        self._chart["spec"]["titleTextPosition"] = {
            "horizontalAlignment": alignment,
        }

    def set_title_font(self, font: dict) -> None:
        """Set the font of the chart title.

        Args:
            font (dict): The font of the title.
        """

        self._chart["spec"]["titleTextFormat"] = font

    def set_subtitle(self, subtitle: str, alignment: str = "CENTER") -> None:
        """Set the subtitle of the chart.
        Alignment options:
            - "CENTER"
            - "LEFT"
            - "RIGHT"

        Args:
            subtitle (str): The subtitle of the chart.
            alignment (str, optional): The alignment of the subtitle.
                Defaults to "CENTER".
        """

        self._chart["spec"]["subtitle"] = subtitle
        self._chart["spec"]["subtitleTextPosition"] = {
            "horizontalAlignment": alignment,
        }

    def set_subtitle_font(self, font: dict) -> None:
        """Set the font of the chart subtitle.

        Args:
            font (dict): The font of the subtitle.
        """

        self._chart["spec"]["subtitleTextFormat"] = font

    def set_alt_text(self, alt_text: str) -> None:
        """Set the text that will be displayed if the chart cannot be
        loaded or a screen reader is used.

        Args:
            alt_text (str): The alt text.
        """

        self._chart["spec"]["altText"] = alt_text

    def set_legend(self, position: str = "BOTTOM_LEGEND") -> None:
        """Set the position of the chart legend.
        Position options:
            - "BOTTOM_LEGEND"
            - "LEFT_LEGEND"
            - "RIGHT_LEGEND"
            - "TOP_LEGEND"
            - "NO_LEGEND"

        Args:
            position (str, optional): The position of the legend.
                Defaults to "BOTTOM_LEGEND".
        """

        self._chart["spec"][self._chart_type]["legendPosition"] = position

    def set_background_color(self, color: tuple) -> None:
        """Set the background color of the chart.

        Args:
            color (tuple): The color of the background. Ex. (1, 1, 1) or Color.WHITE
        """

        self._chart["spec"]["backgroundColorStyle"] = {"rgbColor": format_color(color)}

    def set_font_family(self, font_family: str) -> None:
        """Set the default font family of the chart. This will be used
        for all text in the chart unless otherwise specified.

        Args:
            font_family (str): The font family. Ex. "Consolas"
        """

        self._chart["spec"]["fontName"] = font_family

    def set_position(
        self,
        sheet_id: int,
        anchor_cell: tuple,
        size: tuple,
    ) -> None:
        """Set the position of the chart. This will anchor the chart to a cell
        and set the size of the chart.

        Args:
            sheet_id (int): The ID of the sheet the chart will be on.
            anchor_cell (tuple): The cell the chart will be anchored to. Ex. (1, 1)
            size (tuple): The size of the chart. Ex. (600, 400)
        """

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
        color: tuple = Color.BLACK,
    ) -> None:
        """Add a border to the chart.

        Args:
            color (tuple, optional): The color of the border. Defaults to Color.BLACK.
        """

        self._chart["border"] = {
            "colorStyle": format_color(color),
        }

    def chart_request(self) -> dict:
        """Get the chart request to be used in a batch update request.

        Raises:
            ValueError: If the chart position, type, domain, series, or axis is not set.

        Returns:
            dict: The chart request.
        """

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

        return {"addChart": {"chart": self._chart}}


class BasicChart(Chart):
    """A basic chart for a Google Sheet that the ColumnChart, LineChart, and ScatterChart inherit from.
    Not to be used directly.
    """

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
        header_count: int = 1,
    ) -> None:
        """Set the domain of the chart. The domain is the range of cells that
        contain the labels for the chart.

        Args:
            domain_range (tuple): The range of cells that contain the labels or the independent variable (x) for the chart. Ex. ("Sheet1!A1:A6")
            header_count (int, optional): The number of rows that contain the labels. Defaults to 1.
        """

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
        target_axis: str = "LEFT_AXIS",
        color: tuple = Color.BLACK,
    ) -> None:
        """Add a series to the chart. A series is a range of cells that contain the data
        for the chart related to the domain. More than one series can be added to a chart.
        Target axis options:
            - "LEFT_AXIS"
            - "RIGHT_AXIS"
            - "TOP_AXIS"
            - "BOTTOM_AXIS"

        Args:
            series_range (tuple): The range of cells that contain the data or the dependent variable (y) for the chart. Ex. ("Sheet1!B1:B6")
            target_axis (str, optional): The axis the series will be on. Defaults to "LEFT_AXIS".
            color (tuple, optional): The color of the series. Defaults to Color.BLACK.
        """

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
        position: str = "BOTTOM_AXIS",
        title: str = "X Axis Title",
        alignment: str = "CENTER",
    ) -> None:
        """Add an axis to the chart. An axis is the x or y axis of the chart.
        Position options:
            - "BOTTOM_AXIS"
            - "LEFT_AXIS"
            - "RIGHT_AXIS"
            - "TOP_AXIS"
        Alignment options:
            - "CENTER"
            - "LEFT"
            - "RIGHT"

        Args:
            position (str, optional): The position of the axis. Defaults to "BOTTOM_AXIS".
            title (str, optional): The title of the axis. Defaults to "X Axis Title".
            alignment (str, optional): The alignment of the title. Defaults to "CENTER".
        """

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
    ) -> None:
        """Set the view window of an axis. The view window is the range of values
        that will be displayed on the axis. This will allow you to zoom in or out
        on the data.

        Args:
            location (int): The location of the axis. Generally 0 for the x axis and 1 for the y axis.
            min (int): The minimum value of the view window.
            max (int): The maximum value of the view window.
        """

        self._chart["spec"][self._chart_type]["axis"][location]["viewWindowOptions"] = {
            "viewWindowMin": min,
            "viewWindowMax": max,
        }

    def set_axis_font(self, location: int, font: dict) -> None:
        """Set the font of an axis.

        Args:
            location (int): The location of the axis. Generally 0 for the x axis and 1 for the y axis.
            font (dict): The font of the axis.
        """

        self._chart["spec"][self._chart_type]["axis"][location]["format"] = font


class LineChart(BasicChart):
    """A line chart for a Google Sheet.

    Required parts to set:
        - domain
        - series (one or more)
        - axis (x and y)
    """

    def __init__(self):
        super().__init__("LINE")

    def set_series_line_style(
        self,
        location: int,
        line_style: str,
        line_width: int,
    ) -> None:
        """Set the line style of a series.
        Line styles:
            - ChartLine.INVISIBLE or "INVISIBLE"
            - ChartLine.SOLID or "SOLID"
            - ChartLine.DOTTED or "DOTTED"
            - ChartLine.MEDIUM_DASHED or "MEDIUM_DASHED"
            - ChartLine.MEDIUM_DASHED_DOTTED or "MEDIUM_DASHED_DOTTED"
            - ChartLine.LONG_DASHED or "LONG_DASHED"
            - ChartLine.LONG_DASHED_DOTTED or "LONG_DASHED_DOTTED"

        Args:
            location (int): The location of the series. Generally 0 for the first series, 1 for the second series, etc.
            line_style (str): The style of the line. Ex. "DOTTED"
            line_width (int): The width of the line. Ex. 1
        """

        self._chart["spec"]["basicChart"]["series"][location]["lineStyle"] = {
            "width": line_width,
            "type": line_style,
        }

    def set_line_smoothing(self, smoothing: bool) -> None:
        """Set the line smoothing of the chart. This will smooth the lines
        between the data points.

        Args:
            smoothing (bool): True to smooth the lines, False to not smooth the lines.
        """

        self._chart["spec"]["basicChart"]["lineSmoothing"] = smoothing


class ScatterChart(BasicChart):
    """A scatter chart for a Google Sheet. This is the same as a line chart
    except the lines are not connected.

    Required parts to set:
        - domain
        - series (one or more)
        - axis (x and y)
    """

    def __init__(self):
        super().__init__("SCATTER")


class ColumnChart(BasicChart):
    """A column chart for a Google Sheet. Or referred to as a bar chart. This
    can handle multiple series.

    Required parts to set:
        - domain
        - series (one or more)
        - axis (x and y)
    """

    def __init__(self):
        super().__init__("COLUMN")


class PieChart(Chart):
    """A pie chart for a Google Sheet.

    Required parts to set:
        - domain (one column)
        - series (one column)
    """

    def __init__(self):
        super().__init__("pieChart")

    def set_domain(
        self,
        domain_range: tuple,
    ) -> None:
        """Set the domain of the chart. The domain is the range of cells that
        contain the labels or slices for the chart.

        Args:
            domain_range (tuple): The range of cells that contain the labels or slices for the chart. Ex. ("Sheet1!A1:A6")
        """

        self._chart["spec"]["pieChart"]["domain"] = {
            "sourceRange": {
                "sources": [format_range(domain_range)],
            },
        }

    def add_series(
        self,
        series_range: tuple,
    ) -> None:
        """Add a series to the chart. A series is a range of cells that contain the data
        for the chart related to the domain. Only one series can be added to a chart.

        Args:
            series_range (tuple): The range of cells that contain the data for the chart. Ex. ("Sheet1!B1:B6")
        """

        self._chart["spec"]["pieChart"]["series"] = {
            "sourceRange": {
                "sources": [format_range(series_range)],
            },
        }

    def set_pie_hole_size(self, size: float) -> None:
        """Set the size of the hole in the pie chart. This will create a donut chart.

        Args:
            size (float): The size of the hole. Ex. 0.5
        """

        self._chart["spec"]["pieChart"]["pieHole"] = size
