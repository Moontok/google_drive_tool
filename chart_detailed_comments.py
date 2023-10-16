{
    "addChart": {  # Adds a chart to a sheet in the spreadsheet. # Adds a chart.
        "chart": {  # A chart embedded in a sheet. # The chart that should be added to the spreadsheet, including the position
            # where it should be placed. The chartId
            # field is optional; if one is not set, an id will be randomly generated. (It
            # is an error to specify the ID of an embedded object that already exists.)
            "chartId": 42,  # The ID of the chart.
            "position": {  # The position of an embedded object such as a chart. # The position of the chart.
                "newSheet": True
                or False,  # If true, the embedded object is put on a new sheet whose ID
                # is chosen for you. Used only when writing.
                "sheetId": 42,  # The sheet this is on. Set only if the embedded object
                # is on its own sheet. Must be non-negative.
                "overlayPosition": {  # The location an object is overlaid on top of a grid. # The position at which the object is overlaid on top of a grid.
                    "widthPixels": 42,  # The width of the object, in pixels. Defaults to 600.
                    "offsetYPixels": 42,  # The vertical offset, in pixels, that the object is offset
                    # from the anchor cell.
                    "offsetXPixels": 42,  # The horizontal offset, in pixels, that the object is offset
                    # from the anchor cell.
                    "heightPixels": 42,  # The height of the object, in pixels. Defaults to 371.
                    "anchorCell": {  # A coordinate in a sheet. # The cell the object is anchored to.
                        # All indexes are zero-based.
                        "rowIndex": 42,  # The row index of the coordinate.
                        "columnIndex": 42,  # The column index of the coordinate.
                        "sheetId": 42,  # The sheet this coordinate is on.
                    },
                },
            },
            "spec": {  # The specifications of a chart. # The specification of the chart.
                "fontName": "A String",  # The name of the font to use by default for all chart text (e.g. title,
                # axis labels, legend).  If a font is specified for a specific part of the
                # chart it will override this font name.
                "altText": "A String",  # The alternative text that describes the chart.  This is often used
                # for accessibility.
                "subtitle": "A String",  # The subtitle of the chart.
                "subtitleTextFormat": {  # The format of a run of text in a cell. # The subtitle text format.
                    # Strikethrough and underline are not supported.
                    # Absent values indicate that the field isn't specified.
                    "foregroundColor": {  # Represents a color in the RGBA color space. 
                        "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                        "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                        "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                        "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                    },
                    "bold": True or False,  # True if the text is bold.
                    "foregroundColorStyle": {  # A color value. # The foreground color of the text.
                        # If foreground_color is also set, this field takes precedence.
                        "themeColor": "A String",  # Theme color.
                        "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed
                            # RGB color.
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                    },
                    "strikethrough": True or False,  # True if the text has a strikethrough.
                    "fontFamily": "A String",  # The font family.
                    "fontSize": 42,  # The size of the font.
                    "italic": True or False,  # True if the text is italicized.
                    "underline": True or False,  # True if the text is underlined.
                },
                "title": "A String",  # The title of the chart.
                "titleTextFormat": {  # The format of a run of text in a cell. # The title text format.
                    # Strikethrough and underline are not supported.
                    # Absent values indicate that the field isn't specified.
                    "foregroundColor": {  # Represents a color in the RGBA color space. 
                        "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                        "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. 
                        "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                        "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                    },
                    "bold": True or False,  # True if the text is bold.
                    "foregroundColorStyle": {  # A color value. # The foreground color of the text.
                        # If foreground_color is also set, this field takes precedence.
                        "themeColor": "A String",  # Theme color.
                        "rgbColor": {  # Represents a color in the RGBA color space.
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                    },
                    "strikethrough": True
                    or False,  # True if the text has a strikethrough.
                    "fontFamily": "A String",  # The font family.
                    "fontSize": 42,  # The size of the font.
                    "italic": True or False,  # True if the text is italicized.
                    "underline": True or False,  # True if the text is underlined.
                },
                "treemapChart": {  # A <a href="/chart/interactive/docs/gallery/treemap">Treemap chart</a>. # A treemap chart specification.
                    "sizeData": {  # The data included in a domain or series. # The data that determines the size of each treemap data cell. This data is
                        # expected to be numeric. The cells corresponding to non-numeric or missing
                        # data will not be rendered. If color_data is not specified, this data
                        # is used to determine data cell background colors as well.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "headerColor": {  # Represents a color in the RGBA color space.
                        "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                        "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                        "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                        "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                    },
                    "hideTooltips": True or False,  # True to hide tooltips.
                    "parentLabels": {  # The data included in a domain or series. # The data the contains the treemap cells' parent labels.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "labels": {  # The data included in a domain or series. # The data that contains the treemap cell labels.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "colorData": {  # The data included in a domain or series. # The data that determines the background color of each treemap data cell.
                        # This field is optional. If not specified, size_data is used to
                        # determine background colors. If specified, the data is expected to be
                        # numeric. color_scale will determine how the values in this data map to
                        # data cell background colors.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "maxValue": 3.14,  # The maximum possible data value. Cells with values greater than this will
                    # have the same color as cells with this value. If not specified, defaults
                    # to the actual maximum value from color_data, or the maximum value from
                    # size_data if color_data is not specified.
                    "minValue": 3.14,  # The minimum possible data value. Cells with values less than this will
                    # have the same color as cells with this value. If not specified, defaults
                    # to the actual minimum value from color_data, or the minimum value from
                    # size_data if color_data is not specified.
                    "levels": 42,  # The number of data levels to show on the treemap chart. These levels are
                    # interactive and are shown with their labels. Defaults to 2 if not
                    # specified.
                    "hintedLevels": 42,  # The number of additional data levels beyond the labeled levels to be shown
                    # on the treemap chart. These levels are not interactive and are shown
                    # without their labels. Defaults to 0 if not specified.
                    "textFormat": {  # The format of a run of text in a cell. # The text format for all labels on the chart.
                        # Absent values indicate that the field isn't specified.
                        "foregroundColor": {  # Represents a color in the RGBA color space.
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                        "bold": True or False,  # True if the text is bold.
                        "foregroundColorStyle": {  # A color value. # The foreground color of the text.
                            # If foreground_color is also set, this field takes precedence.
                            "themeColor": "A String",  # Theme color.
                            "rgbColor": {  # Represents a color in the RGBA color space.
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                        },
                        "strikethrough": True
                        or False,  # True if the text has a strikethrough.
                        "fontFamily": "A String",  # The font family.
                        "fontSize": 42,  # The size of the font.
                        "italic": True or False,  # True if the text is italicized.
                        "underline": True or False,  # True if the text is underlined.
                    },
                    "headerColorStyle": {  # A color value. # The background color for header cells.
                        # If header_color is also set, this field takes precedence.
                        "themeColor": "A String",  # Theme color.
                        "rgbColor": {  # Represents a color in the RGBA color space.
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                    },
                    "colorScale": {  # A color scale for a treemap chart. # The color scale for data cells in the treemap chart. Data cells are
                        # assigned colors based on their color values. These color values come from
                        # color_data, or from size_data if color_data is not specified.
                        # Cells with color values less than or equal to min_value will
                        # have minValueColor as their
                        # background color. Cells with color values greater than or equal to
                        # max_value will have
                        # maxValueColor as their background
                        # color. Cells with color values between min_value and max_value will
                        # have background colors on a gradient between
                        # minValueColor and
                        # maxValueColor, the midpoint of
                        # the gradient being midValueColor.
                        # Cells with missing or non-numeric color values will have
                        # noDataColor as their background
                        # color.
                        "maxValueColor": {  # Represents a color in the RGBA color space. 
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                        "noDataColor": {  # Represents a color in the RGBA color space. 
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                        "midValueColorStyle": {  # A color value. # The background color for cells with a color value at the midpoint between
                            # minValue and
                            # maxValue. Defaults to #efe6dc if not
                            # specified.
                            # If mid_value_color is also set, this field takes precedence.
                            "themeColor": "A String",  # Theme color.
                            "rgbColor": {  # Represents a color in the RGBA color space.
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                        },
                        "maxValueColorStyle": {  # A color value. # The background color for cells with a color value greater than or equal
                            # to maxValue. Defaults to #109618 if not
                            # specified.
                            # If max_value_color is also set, this field takes precedence.
                            "themeColor": "A String",  # Theme color.
                            "rgbColor": {  # Represents a color in the RGBA color space.
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                        },
                        "minValueColor": {  # Represents a color in the RGBA color space. 
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                        "noDataColorStyle": {  # A color value. # The background color for cells that have no color data associated with
                            # them. Defaults to #000000 if not specified.
                            # If no_data_color is also set, this field takes precedence.
                            "themeColor": "A String",  # Theme color.
                            "rgbColor": {  # Represents a color in the RGBA color space.
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                        },
                        "midValueColor": {  # Represents a color in the RGBA color space. This representation is designed # The background color for cells with a color value at the midpoint between
                            # minValue and
                            # maxValue. Defaults to #efe6dc if not
                            # specified.
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. 
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                        "minValueColorStyle": {  # A color value. # The background color for cells with a color value less than or equal to
                            # minValue. Defaults to #dc3912 if not
                            # specified.
                            # If min_value_color is also set, this field takes precedence.
                            "themeColor": "A String",  # Theme color.
                            "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed # RGB color.
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                        },
                    },
                },
                "scorecardChart": { 
                    # A scorecard chart. Scorecard charts are used to highlight key performance # A scorecard chart specification.
                    # indicators, known as KPIs, on the spreadsheet. A scorecard chart can
                    # represent things like total sales, average cost, or a top selling item. You
                    # can specify a single data value, or aggregate over a range of data.
                    # Percentage or absolute difference from a baseline value can be highlighted,
                    # like changes over time.
                    "numberFormatSource": "A String",  # The number format source used in the scorecard chart.
                    # This field is optional.
                    "customFormatOptions": {  # Custom number formatting options for chart attributes. # Custom formatting options for numeric key/baseline values in scorecard
                        # chart. This field is used only when number_format_source is set to
                        # CUSTOM. This field is optional.
                        "prefix": "A String",  # Custom prefix to be prepended to the chart attribute.
                        # This field is optional.
                        "suffix": "A String",  # Custom suffix to be appended to the chart attribute.
                        # This field is optional.
                    },
                    "keyValueFormat": {  # Formatting options for key value. # Formatting options for key value.
                        "position": {  # Position settings for text. # Specifies the horizontal text positioning of key value.
                            # This field is optional. If not specified, default positioning is used.
                            "horizontalAlignment": "A String",  # Horizontal alignment setting for the piece of text.
                        },
                        "textFormat": {  # The format of a run of text in a cell. # Text formatting options for key value.
                            # Absent values indicate that the field isn't specified.
                            "foregroundColor": {  # Represents a color in the RGBA color space.
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                            "bold": True or False,  # True if the text is bold.
                            "foregroundColorStyle": {  # A color value. # The foreground color of the text.
                                # If foreground_color is also set, this field takes precedence.
                                "themeColor": "A String",  # Theme color.
                                "rgbColor": {  # Represents a color in the RGBA color space. 
                                    "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                    "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. 
                                    "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                    "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                },
                            },
                            "strikethrough": True
                            or False,  # True if the text has a strikethrough.
                            "fontFamily": "A String",  # The font family.
                            "fontSize": 42,  # The size of the font.
                            "italic": True or False,  # True if the text is italicized.
                            "underline": True
                            or False,  # True if the text is underlined.
                        },
                    },
                    "aggregateType": "A String",  # The aggregation type for key and baseline chart data in scorecard chart.
                    # This field is optional.
                    "baselineValueFormat": {  # Formatting options for baseline value. # Formatting options for baseline value.
                        # This field is needed only if baseline_value_data is specified.
                        "description": "A String",  # Description which is appended after the baseline value.
                        # This field is optional.
                        "negativeColor": {  # Represents a color in the RGBA color space. 
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                        "comparisonType": "A String",  # The comparison type of key value with baseline value.
                        "positiveColorStyle": {  # A color value. # Color to be used, in case baseline value represents a positive change for
                            # key value. This field is optional.
                            # If positive_color is also set, this field takes precedence.
                            "themeColor": "A String",  # Theme color.
                            "rgbColor": {  # Represents a color in the RGBA color space.
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                        },
                        "negativeColorStyle": {  # A color value. # Color to be used, in case baseline value represents a negative change for
                            # key value. This field is optional.
                            # If negative_color is also set, this field takes precedence.
                            "themeColor": "A String",  # Theme color.
                            "rgbColor": {  # Represents a color in the RGBA color space.
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                        },
                        "position": {  # Position settings for text. # Specifies the horizontal text positioning of baseline value.
                            # This field is optional. If not specified, default positioning is used.
                            "horizontalAlignment": "A String",  # Horizontal alignment setting for the piece of text.
                        },
                        "textFormat": {  # The format of a run of text in a cell. # Text formatting options for baseline value.
                            # Absent values indicate that the field isn't specified.
                            "foregroundColor": {  # Represents a color in the RGBA color space.
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                            "bold": True or False,  # True if the text is bold.
                            "foregroundColorStyle": {  # A color value. # The foreground color of the text.
                                # If foreground_color is also set, this field takes precedence.
                                "themeColor": "A String",  # Theme color.
                                "rgbColor": {  # Represents a color in the RGBA color space. 
                                    "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                    "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                                    "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                    "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                },
                            },
                            "strikethrough": True
                            or False,  # True if the text has a strikethrough.
                            "fontFamily": "A String",  # The font family.
                            "fontSize": 42,  # The size of the font.
                            "italic": True or False,  # True if the text is italicized.
                            "underline": True
                            or False,  # True if the text is underlined.
                        },
                        "positiveColor": {  # Represents a color in the RGBA color space.
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                    },
                    "keyValueData": {  # The data included in a domain or series. # The data for scorecard key value.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "scaleFactor": 3.14,  # Value to scale scorecard key and baseline value. For example, a factor of
                    # 10 can be used to divide all values in the chart by 10.
                    # This field is optional.
                    "baselineValueData": {  # The data included in a domain or series. # The data for scorecard baseline value.
                        # This field is optional.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                },
                "titleTextPosition": {  # Position settings for text. # The title text position.
                    # This field is optional.
                    "horizontalAlignment": "A String",  # Horizontal alignment setting for the piece of text.
                },
                "backgroundColorStyle": {  # A color value. # The background color of the entire chart.
                    # Not applicable to Org charts.
                    # If background_color is also set, this field takes precedence.
                    "themeColor": "A String",  # Theme color.
                    "rgbColor": {  # Represents a color in the RGBA color space. 
                        "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                        "alpha": 3.14,  # The fraction of this color that should be applied to the pixel.
                        "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                        "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                    },
                },
                "hiddenDimensionStrategy": "A String",  # Determines how the charts will use hidden rows or columns.
                "pieChart": {  # A <a href="/chart/interactive/docs/gallery/piechart">pie chart</a>. # A pie chart specification.
                    "series": {  # The data included in a domain or series. # The data that covers the one and only series of the pie chart.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "domain": {  # The data included in a domain or series. # The data that covers the domain of the pie chart.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "threeDimensional": True
                    or False,  # True if the pie is three dimensional.
                    "legendPosition": "A String",  # Where the legend of the pie chart should be drawn.
                    "pieHole": 3.14,  # The size of the hole in the pie chart.
                },
                "candlestickChart": {  # A <a href="/chart/interactive/docs/gallery/candlestickchart">candlestick # A candlestick chart specification.
                    # chart</a>.
                    "domain": {  # The domain of a CandlestickChart. # The domain data (horizontal axis) for the candlestick chart.  String data
                        # will be treated as discrete labels, other data will be treated as
                        # continuous values.
                        "reversed": True
                        or False,  # True to reverse the order of the domain values (horizontal axis).
                        "data": {  # The data included in a domain or series. # The data of the CandlestickDomain.
                            "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                                "sources": [  # The ranges of data for a series or domain.
                                    # Exactly one dimension must have a length of 1,
                                    # and all sources in the list must have the same dimension
                                    # with length 1.
                                    # The domain (if it exists) & all series must have the same number
                                    # of source ranges. If using more than one source range, then the source
                                    # range at a given offset must be in order and contiguous across the domain
                                    # and series.
                                    #
                                    # For example, these are valid configurations:
                                    #
                                    #     domain sources: A1:A5
                                    #     series1 sources: B1:B5
                                    #     series2 sources: D6:D10
                                    #
                                    #     domain sources: A1:A5, C10:C12
                                    #     series1 sources: B1:B5, D10:D12
                                    #     series2 sources: C1:C5, E10:E12
                                    {  # A range on a sheet.
                                        # All indexes are zero-based.
                                        # Indexes are half open, e.g the start index is inclusive
                                        # and the end index is exclusive -- [start_index, end_index).
                                        # Missing indexes indicate the range is unbounded on that side.
                                        #
                                        # For example, if `"Sheet1"` is sheet ID 0, then:
                                        #
                                        #   `Sheet1!A1:A1 == sheet_id: 0,
                                        #                   start_row_index: 0, end_row_index: 1,
                                        #                   start_column_index: 0, end_column_index: 1`
                                        #
                                        #   `Sheet1!A3:B4 == sheet_id: 0,
                                        #                   start_row_index: 2, end_row_index: 4,
                                        #                   start_column_index: 0, end_column_index: 2`
                                        #
                                        #   `Sheet1!A:B == sheet_id: 0,
                                        #                 start_column_index: 0, end_column_index: 2`
                                        #
                                        #   `Sheet1!A5:B == sheet_id: 0,
                                        #                  start_row_index: 4,
                                        #                  start_column_index: 0, end_column_index: 2`
                                        #
                                        #   `Sheet1 == sheet_id:0`
                                        #
                                        # The start index must always be less than or equal to the end index.
                                        # If the start index equals the end index, then the range is empty.
                                        # Empty ranges are typically not meaningful and are usually rendered in the
                                        # UI as `#REF!`.
                                        "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                        "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                        "sheetId": 42,  # The sheet this range is on.
                                        "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                        "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                    },
                                ],
                            },
                        },
                    },
                    "data": [  # The Candlestick chart data.
                        # Only one CandlestickData is supported.
                        {  # The Candlestick chart data, each containing the low, open, close, and high
                            # values for a series.
                            "lowSeries": {  # The series of a CandlestickData. # The range data (vertical axis) for the low/minimum value for each candle.
                                # This is the bottom of the candle's center line.
                                "data": {  # The data included in a domain or series. # The data of the CandlestickSeries.
                                    "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                                        "sources": [  # The ranges of data for a series or domain.
                                            # Exactly one dimension must have a length of 1,
                                            # and all sources in the list must have the same dimension
                                            # with length 1.
                                            # The domain (if it exists) & all series must have the same number
                                            # of source ranges. If using more than one source range, then the source
                                            # range at a given offset must be in order and contiguous across the domain
                                            # and series.
                                            #
                                            # For example, these are valid configurations:
                                            #
                                            #     domain sources: A1:A5
                                            #     series1 sources: B1:B5
                                            #     series2 sources: D6:D10
                                            #
                                            #     domain sources: A1:A5, C10:C12
                                            #     series1 sources: B1:B5, D10:D12
                                            #     series2 sources: C1:C5, E10:E12
                                            {  # A range on a sheet.
                                                # All indexes are zero-based.
                                                # Indexes are half open, e.g the start index is inclusive
                                                # and the end index is exclusive -- [start_index, end_index).
                                                # Missing indexes indicate the range is unbounded on that side.
                                                #
                                                # For example, if `"Sheet1"` is sheet ID 0, then:
                                                #
                                                #   `Sheet1!A1:A1 == sheet_id: 0,
                                                #                   start_row_index: 0, end_row_index: 1,
                                                #                   start_column_index: 0, end_column_index: 1`
                                                #
                                                #   `Sheet1!A3:B4 == sheet_id: 0,
                                                #                   start_row_index: 2, end_row_index: 4,
                                                #                   start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1!A:B == sheet_id: 0,
                                                #                 start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1!A5:B == sheet_id: 0,
                                                #                  start_row_index: 4,
                                                #                  start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1 == sheet_id:0`
                                                #
                                                # The start index must always be less than or equal to the end index.
                                                # If the start index equals the end index, then the range is empty.
                                                # Empty ranges are typically not meaningful and are usually rendered in the
                                                # UI as `#REF!`.
                                                "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                                "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                                "sheetId": 42,  # The sheet this range is on.
                                                "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                                "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                            },
                                        ],
                                    },
                                },
                            },
                            "highSeries": {  # The series of a CandlestickData. # The range data (vertical axis) for the high/maximum value for each
                                # candle. This is the top of the candle's center line.
                                "data": {  # The data included in a domain or series. # The data of the CandlestickSeries.
                                    "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                                        "sources": [  # The ranges of data for a series or domain.
                                            # Exactly one dimension must have a length of 1,
                                            # and all sources in the list must have the same dimension
                                            # with length 1.
                                            # The domain (if it exists) & all series must have the same number
                                            # of source ranges. If using more than one source range, then the source
                                            # range at a given offset must be in order and contiguous across the domain
                                            # and series.
                                            #
                                            # For example, these are valid configurations:
                                            #
                                            #     domain sources: A1:A5
                                            #     series1 sources: B1:B5
                                            #     series2 sources: D6:D10
                                            #
                                            #     domain sources: A1:A5, C10:C12
                                            #     series1 sources: B1:B5, D10:D12
                                            #     series2 sources: C1:C5, E10:E12
                                            {  # A range on a sheet.
                                                # All indexes are zero-based.
                                                # Indexes are half open, e.g the start index is inclusive
                                                # and the end index is exclusive -- [start_index, end_index).
                                                # Missing indexes indicate the range is unbounded on that side.
                                                #
                                                # For example, if `"Sheet1"` is sheet ID 0, then:
                                                #
                                                #   `Sheet1!A1:A1 == sheet_id: 0,
                                                #                   start_row_index: 0, end_row_index: 1,
                                                #                   start_column_index: 0, end_column_index: 1`
                                                #
                                                #   `Sheet1!A3:B4 == sheet_id: 0,
                                                #                   start_row_index: 2, end_row_index: 4,
                                                #                   start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1!A:B == sheet_id: 0,
                                                #                 start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1!A5:B == sheet_id: 0,
                                                #                  start_row_index: 4,
                                                #                  start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1 == sheet_id:0`
                                                #
                                                # The start index must always be less than or equal to the end index.
                                                # If the start index equals the end index, then the range is empty.
                                                # Empty ranges are typically not meaningful and are usually rendered in the
                                                # UI as `#REF!`.
                                                "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                                "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                                "sheetId": 42,  # The sheet this range is on.
                                                "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                                "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                            },
                                        ],
                                    },
                                },
                            },
                            "openSeries": {  # The series of a CandlestickData. # The range data (vertical axis) for the open/initial value for each
                                # candle. This is the bottom of the candle body.  If less than the close
                                # value the candle will be filled.  Otherwise the candle will be hollow.
                                "data": {  # The data included in a domain or series. # The data of the CandlestickSeries.
                                    "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                                        "sources": [  # The ranges of data for a series or domain.
                                            # Exactly one dimension must have a length of 1,
                                            # and all sources in the list must have the same dimension
                                            # with length 1.
                                            # The domain (if it exists) & all series must have the same number
                                            # of source ranges. If using more than one source range, then the source
                                            # range at a given offset must be in order and contiguous across the domain
                                            # and series.
                                            #
                                            # For example, these are valid configurations:
                                            #
                                            #     domain sources: A1:A5
                                            #     series1 sources: B1:B5
                                            #     series2 sources: D6:D10
                                            #
                                            #     domain sources: A1:A5, C10:C12
                                            #     series1 sources: B1:B5, D10:D12
                                            #     series2 sources: C1:C5, E10:E12
                                            {  # A range on a sheet.
                                                # All indexes are zero-based.
                                                # Indexes are half open, e.g the start index is inclusive
                                                # and the end index is exclusive -- [start_index, end_index).
                                                # Missing indexes indicate the range is unbounded on that side.
                                                #
                                                # For example, if `"Sheet1"` is sheet ID 0, then:
                                                #
                                                #   `Sheet1!A1:A1 == sheet_id: 0,
                                                #                   start_row_index: 0, end_row_index: 1,
                                                #                   start_column_index: 0, end_column_index: 1`
                                                #
                                                #   `Sheet1!A3:B4 == sheet_id: 0,
                                                #                   start_row_index: 2, end_row_index: 4,
                                                #                   start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1!A:B == sheet_id: 0,
                                                #                 start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1!A5:B == sheet_id: 0,
                                                #                  start_row_index: 4,
                                                #                  start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1 == sheet_id:0`
                                                #
                                                # The start index must always be less than or equal to the end index.
                                                # If the start index equals the end index, then the range is empty.
                                                # Empty ranges are typically not meaningful and are usually rendered in the
                                                # UI as `#REF!`.
                                                "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                                "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                                "sheetId": 42,  # The sheet this range is on.
                                                "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                                "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                            },
                                        ],
                                    },
                                },
                            },
                            "closeSeries": {  # The series of a CandlestickData. # The range data (vertical axis) for the close/final value for each candle.
                                # This is the top of the candle body.  If greater than the open value the
                                # candle will be filled.  Otherwise the candle will be hollow.
                                "data": {  # The data included in a domain or series. # The data of the CandlestickSeries.
                                    "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                                        "sources": [  # The ranges of data for a series or domain.
                                            # Exactly one dimension must have a length of 1,
                                            # and all sources in the list must have the same dimension
                                            # with length 1.
                                            # The domain (if it exists) & all series must have the same number
                                            # of source ranges. If using more than one source range, then the source
                                            # range at a given offset must be in order and contiguous across the domain
                                            # and series.
                                            #
                                            # For example, these are valid configurations:
                                            #
                                            #     domain sources: A1:A5
                                            #     series1 sources: B1:B5
                                            #     series2 sources: D6:D10
                                            #
                                            #     domain sources: A1:A5, C10:C12
                                            #     series1 sources: B1:B5, D10:D12
                                            #     series2 sources: C1:C5, E10:E12
                                            {  # A range on a sheet.
                                                # All indexes are zero-based.
                                                # Indexes are half open, e.g the start index is inclusive
                                                # and the end index is exclusive -- [start_index, end_index).
                                                # Missing indexes indicate the range is unbounded on that side.
                                                #
                                                # For example, if `"Sheet1"` is sheet ID 0, then:
                                                #
                                                #   `Sheet1!A1:A1 == sheet_id: 0,
                                                #                   start_row_index: 0, end_row_index: 1,
                                                #                   start_column_index: 0, end_column_index: 1`
                                                #
                                                #   `Sheet1!A3:B4 == sheet_id: 0,
                                                #                   start_row_index: 2, end_row_index: 4,
                                                #                   start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1!A:B == sheet_id: 0,
                                                #                 start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1!A5:B == sheet_id: 0,
                                                #                  start_row_index: 4,
                                                #                  start_column_index: 0, end_column_index: 2`
                                                #
                                                #   `Sheet1 == sheet_id:0`
                                                #
                                                # The start index must always be less than or equal to the end index.
                                                # If the start index equals the end index, then the range is empty.
                                                # Empty ranges are typically not meaningful and are usually rendered in the
                                                # UI as `#REF!`.
                                                "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                                "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                                "sheetId": 42,  # The sheet this range is on.
                                                "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                                "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                            },
                                        ],
                                    },
                                },
                            },
                        },
                    ],
                },
                "subtitleTextPosition": {  # Position settings for text. # The subtitle text position.
                    # This field is optional.
                    "horizontalAlignment": "A String",  # Horizontal alignment setting for the piece of text.
                },
                "backgroundColor": {  # Represents a color in the RGBA color space. This representation is designed # The background color of the entire chart.
                    # Not applicable to Org charts.
                    # for simplicity of conversion to/from color representations in various
                    # languages over compactness; for example, the fields of this representation
                    # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                    # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                    # method in iOS; and, with just a little work, it can be easily formatted into
                    # a CSS "rgba()" string in JavaScript, as well.
                    #
                    # Note: this proto does not carry information about the absolute color space
                    # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                    # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                    # space.
                    #
                    # Example (Java):
                    #
                    #      import com.google.type.Color;
                    #
                    #      // ...
                    #      public static java.awt.Color fromProto(Color protocolor) {
                    #        float alpha = protocolor.hasAlpha()
                    #            ? protocolor.getAlpha().getValue()
                    #            : 1.0;
                    #
                    #        return new java.awt.Color(
                    #            protocolor.getRed(),
                    #            protocolor.getGreen(),
                    #            protocolor.getBlue(),
                    #            alpha);
                    #      }
                    #
                    #      public static Color toProto(java.awt.Color color) {
                    #        float red = (float) color.getRed();
                    #        float green = (float) color.getGreen();
                    #        float blue = (float) color.getBlue();
                    #        float denominator = 255.0;
                    #        Color.Builder resultBuilder =
                    #            Color
                    #                .newBuilder()
                    #                .setRed(red / denominator)
                    #                .setGreen(green / denominator)
                    #                .setBlue(blue / denominator);
                    #        int alpha = color.getAlpha();
                    #        if (alpha != 255) {
                    #          result.setAlpha(
                    #              FloatValue
                    #                  .newBuilder()
                    #                  .setValue(((float) alpha) / denominator)
                    #                  .build());
                    #        }
                    #        return resultBuilder.build();
                    #      }
                    #      // ...
                    #
                    # Example (iOS / Obj-C):
                    #
                    #      // ...
                    #      static UIColor* fromProto(Color* protocolor) {
                    #         float red = [protocolor red];
                    #         float green = [protocolor green];
                    #         float blue = [protocolor blue];
                    #         FloatValue* alpha_wrapper = [protocolor alpha];
                    #         float alpha = 1.0;
                    #         if (alpha_wrapper != nil) {
                    #           alpha = [alpha_wrapper value];
                    #         }
                    #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                    #      }
                    #
                    #      static Color* toProto(UIColor* color) {
                    #          CGFloat red, green, blue, alpha;
                    #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                    #            return nil;
                    #          }
                    #          Color* result = [[Color alloc] init];
                    #          [result setRed:red];
                    #          [result setGreen:green];
                    #          [result setBlue:blue];
                    #          if (alpha <= 0.9999) {
                    #            [result setAlpha:floatWrapperWithValue(alpha)];
                    #          }
                    #          [result autorelease];
                    #          return result;
                    #     }
                    #     // ...
                    #
                    #  Example (JavaScript):
                    #
                    #     // ...
                    #
                    #     var protoToCssColor = function(rgb_color) {
                    #        var redFrac = rgb_color.red || 0.0;
                    #        var greenFrac = rgb_color.green || 0.0;
                    #        var blueFrac = rgb_color.blue || 0.0;
                    #        var red = Math.floor(redFrac * 255);
                    #        var green = Math.floor(greenFrac * 255);
                    #        var blue = Math.floor(blueFrac * 255);
                    #
                    #        if (!('alpha' in rgb_color)) {
                    #           return rgbToCssColor_(red, green, blue);
                    #        }
                    #
                    #        var alphaFrac = rgb_color.alpha.value || 0.0;
                    #        var rgbParams = [red, green, blue].join(',');
                    #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                    #     };
                    #
                    #     var rgbToCssColor_ = function(red, green, blue) {
                    #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                    #       var hexString = rgbNumber.toString(16);
                    #       var missingZeros = 6 - hexString.length;
                    #       var resultBuilder = ['#'];
                    #       for (var i = 0; i < missingZeros; i++) {
                    #          resultBuilder.push('0');
                    #       }
                    #       resultBuilder.push(hexString);
                    #       return resultBuilder.join('');
                    #     };
                    #
                    #     // ...
                    "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                    "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                    # the final pixel color is defined by the equation:
                    #
                    #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                    #
                    # This means that a value of 1.0 corresponds to a solid color, whereas
                    # a value of 0.0 corresponds to a completely transparent color. This
                    # uses a wrapper message rather than a simple float scalar so that it is
                    # possible to distinguish between a default value and the value being unset.
                    # If omitted, this color object is to be rendered as a solid color
                    # (as if the alpha value had been explicitly given with a value of 1.0).
                    "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                    "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                },
                "maximized": True
                or False,  # True to make a chart fill the entire space in which it's rendered with
                # minimum padding.  False to use the default padding.
                # (Not applicable to Geo and Org charts.)
                "waterfallChart": {  # A waterfall chart. # A waterfall chart specification.
                    "stackedType": "A String",  # The stacked type.
                    "hideConnectorLines": True
                    or False,  # True to hide connector lines between columns.
                    "domain": {  # The domain of a waterfall chart. # The domain data (horizontal axis) for the waterfall chart.
                        "reversed": True
                        or False,  # True to reverse the order of the domain values (horizontal axis).
                        "data": {  # The data included in a domain or series. # The data of the WaterfallChartDomain.
                            "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                                "sources": [  # The ranges of data for a series or domain.
                                    # Exactly one dimension must have a length of 1,
                                    # and all sources in the list must have the same dimension
                                    # with length 1.
                                    # The domain (if it exists) & all series must have the same number
                                    # of source ranges. If using more than one source range, then the source
                                    # range at a given offset must be in order and contiguous across the domain
                                    # and series.
                                    #
                                    # For example, these are valid configurations:
                                    #
                                    #     domain sources: A1:A5
                                    #     series1 sources: B1:B5
                                    #     series2 sources: D6:D10
                                    #
                                    #     domain sources: A1:A5, C10:C12
                                    #     series1 sources: B1:B5, D10:D12
                                    #     series2 sources: C1:C5, E10:E12
                                    {  # A range on a sheet.
                                        # All indexes are zero-based.
                                        # Indexes are half open, e.g the start index is inclusive
                                        # and the end index is exclusive -- [start_index, end_index).
                                        # Missing indexes indicate the range is unbounded on that side.
                                        #
                                        # For example, if `"Sheet1"` is sheet ID 0, then:
                                        #
                                        #   `Sheet1!A1:A1 == sheet_id: 0,
                                        #                   start_row_index: 0, end_row_index: 1,
                                        #                   start_column_index: 0, end_column_index: 1`
                                        #
                                        #   `Sheet1!A3:B4 == sheet_id: 0,
                                        #                   start_row_index: 2, end_row_index: 4,
                                        #                   start_column_index: 0, end_column_index: 2`
                                        #
                                        #   `Sheet1!A:B == sheet_id: 0,
                                        #                 start_column_index: 0, end_column_index: 2`
                                        #
                                        #   `Sheet1!A5:B == sheet_id: 0,
                                        #                  start_row_index: 4,
                                        #                  start_column_index: 0, end_column_index: 2`
                                        #
                                        #   `Sheet1 == sheet_id:0`
                                        #
                                        # The start index must always be less than or equal to the end index.
                                        # If the start index equals the end index, then the range is empty.
                                        # Empty ranges are typically not meaningful and are usually rendered in the
                                        # UI as `#REF!`.
                                        "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                        "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                        "sheetId": 42,  # The sheet this range is on.
                                        "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                        "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                    },
                                ],
                            },
                        },
                    },
                    "connectorLineStyle": {  # Properties that describe the style of a line. # The line style for the connector lines.
                        "width": 42,  # The thickness of the line, in px.
                        "type": "A String",  # The dash type of the line.
                    },
                    "series": [  # The data this waterfall chart is visualizing.
                        {  # A single series of data for a waterfall chart.
                            "hideTrailingSubtotal": True
                            or False,  # True to hide the subtotal column from the end of the series. By default,
                            # a subtotal column will appear at the end of each series. Setting this
                            # field to true will hide that subtotal column for this series.
                            "positiveColumnsStyle": {  # Styles for a waterfall chart column. # Styles for all columns in this series with positive values.
                                "color": {  # Represents a color in the RGBA color space. This representation is designed # The color of the column.
                                    # for simplicity of conversion to/from color representations in various
                                    # languages over compactness; for example, the fields of this representation
                                    # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                    # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                    # method in iOS; and, with just a little work, it can be easily formatted into
                                    # a CSS "rgba()" string in JavaScript, as well.
                                    #
                                    # Note: this proto does not carry information about the absolute color space
                                    # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                    # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                    # space.
                                    #
                                    # Example (Java):
                                    #
                                    #      import com.google.type.Color;
                                    #
                                    #      // ...
                                    #      public static java.awt.Color fromProto(Color protocolor) {
                                    #        float alpha = protocolor.hasAlpha()
                                    #            ? protocolor.getAlpha().getValue()
                                    #            : 1.0;
                                    #
                                    #        return new java.awt.Color(
                                    #            protocolor.getRed(),
                                    #            protocolor.getGreen(),
                                    #            protocolor.getBlue(),
                                    #            alpha);
                                    #      }
                                    #
                                    #      public static Color toProto(java.awt.Color color) {
                                    #        float red = (float) color.getRed();
                                    #        float green = (float) color.getGreen();
                                    #        float blue = (float) color.getBlue();
                                    #        float denominator = 255.0;
                                    #        Color.Builder resultBuilder =
                                    #            Color
                                    #                .newBuilder()
                                    #                .setRed(red / denominator)
                                    #                .setGreen(green / denominator)
                                    #                .setBlue(blue / denominator);
                                    #        int alpha = color.getAlpha();
                                    #        if (alpha != 255) {
                                    #          result.setAlpha(
                                    #              FloatValue
                                    #                  .newBuilder()
                                    #                  .setValue(((float) alpha) / denominator)
                                    #                  .build());
                                    #        }
                                    #        return resultBuilder.build();
                                    #      }
                                    #      // ...
                                    #
                                    # Example (iOS / Obj-C):
                                    #
                                    #      // ...
                                    #      static UIColor* fromProto(Color* protocolor) {
                                    #         float red = [protocolor red];
                                    #         float green = [protocolor green];
                                    #         float blue = [protocolor blue];
                                    #         FloatValue* alpha_wrapper = [protocolor alpha];
                                    #         float alpha = 1.0;
                                    #         if (alpha_wrapper != nil) {
                                    #           alpha = [alpha_wrapper value];
                                    #         }
                                    #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                    #      }
                                    #
                                    #      static Color* toProto(UIColor* color) {
                                    #          CGFloat red, green, blue, alpha;
                                    #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                    #            return nil;
                                    #          }
                                    #          Color* result = [[Color alloc] init];
                                    #          [result setRed:red];
                                    #          [result setGreen:green];
                                    #          [result setBlue:blue];
                                    #          if (alpha <= 0.9999) {
                                    #            [result setAlpha:floatWrapperWithValue(alpha)];
                                    #          }
                                    #          [result autorelease];
                                    #          return result;
                                    #     }
                                    #     // ...
                                    #
                                    #  Example (JavaScript):
                                    #
                                    #     // ...
                                    #
                                    #     var protoToCssColor = function(rgb_color) {
                                    #        var redFrac = rgb_color.red || 0.0;
                                    #        var greenFrac = rgb_color.green || 0.0;
                                    #        var blueFrac = rgb_color.blue || 0.0;
                                    #        var red = Math.floor(redFrac * 255);
                                    #        var green = Math.floor(greenFrac * 255);
                                    #        var blue = Math.floor(blueFrac * 255);
                                    #
                                    #        if (!('alpha' in rgb_color)) {
                                    #           return rgbToCssColor_(red, green, blue);
                                    #        }
                                    #
                                    #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                    #        var rgbParams = [red, green, blue].join(',');
                                    #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                    #     };
                                    #
                                    #     var rgbToCssColor_ = function(red, green, blue) {
                                    #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                    #       var hexString = rgbNumber.toString(16);
                                    #       var missingZeros = 6 - hexString.length;
                                    #       var resultBuilder = ['#'];
                                    #       for (var i = 0; i < missingZeros; i++) {
                                    #          resultBuilder.push('0');
                                    #       }
                                    #       resultBuilder.push(hexString);
                                    #       return resultBuilder.join('');
                                    #     };
                                    #
                                    #     // ...
                                    "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                    "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                    # the final pixel color is defined by the equation:
                                    #
                                    #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                    #
                                    # This means that a value of 1.0 corresponds to a solid color, whereas
                                    # a value of 0.0 corresponds to a completely transparent color. This
                                    # uses a wrapper message rather than a simple float scalar so that it is
                                    # possible to distinguish between a default value and the value being unset.
                                    # If omitted, this color object is to be rendered as a solid color
                                    # (as if the alpha value had been explicitly given with a value of 1.0).
                                    "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                    "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                },
                                "colorStyle": {  # A color value. # The color of the column.
                                    # If color is also set, this field takes precedence.
                                    "themeColor": "A String",  # Theme color.
                                    "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed # RGB color.
                                        # for simplicity of conversion to/from color representations in various
                                        # languages over compactness; for example, the fields of this representation
                                        # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                        # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                        # method in iOS; and, with just a little work, it can be easily formatted into
                                        # a CSS "rgba()" string in JavaScript, as well.
                                        #
                                        # Note: this proto does not carry information about the absolute color space
                                        # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                        # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                        # space.
                                        #
                                        # Example (Java):
                                        #
                                        #      import com.google.type.Color;
                                        #
                                        #      // ...
                                        #      public static java.awt.Color fromProto(Color protocolor) {
                                        #        float alpha = protocolor.hasAlpha()
                                        #            ? protocolor.getAlpha().getValue()
                                        #            : 1.0;
                                        #
                                        #        return new java.awt.Color(
                                        #            protocolor.getRed(),
                                        #            protocolor.getGreen(),
                                        #            protocolor.getBlue(),
                                        #            alpha);
                                        #      }
                                        #
                                        #      public static Color toProto(java.awt.Color color) {
                                        #        float red = (float) color.getRed();
                                        #        float green = (float) color.getGreen();
                                        #        float blue = (float) color.getBlue();
                                        #        float denominator = 255.0;
                                        #        Color.Builder resultBuilder =
                                        #            Color
                                        #                .newBuilder()
                                        #                .setRed(red / denominator)
                                        #                .setGreen(green / denominator)
                                        #                .setBlue(blue / denominator);
                                        #        int alpha = color.getAlpha();
                                        #        if (alpha != 255) {
                                        #          result.setAlpha(
                                        #              FloatValue
                                        #                  .newBuilder()
                                        #                  .setValue(((float) alpha) / denominator)
                                        #                  .build());
                                        #        }
                                        #        return resultBuilder.build();
                                        #      }
                                        #      // ...
                                        #
                                        # Example (iOS / Obj-C):
                                        #
                                        #      // ...
                                        #      static UIColor* fromProto(Color* protocolor) {
                                        #         float red = [protocolor red];
                                        #         float green = [protocolor green];
                                        #         float blue = [protocolor blue];
                                        #         FloatValue* alpha_wrapper = [protocolor alpha];
                                        #         float alpha = 1.0;
                                        #         if (alpha_wrapper != nil) {
                                        #           alpha = [alpha_wrapper value];
                                        #         }
                                        #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                        #      }
                                        #
                                        #      static Color* toProto(UIColor* color) {
                                        #          CGFloat red, green, blue, alpha;
                                        #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                        #            return nil;
                                        #          }
                                        #          Color* result = [[Color alloc] init];
                                        #          [result setRed:red];
                                        #          [result setGreen:green];
                                        #          [result setBlue:blue];
                                        #          if (alpha <= 0.9999) {
                                        #            [result setAlpha:floatWrapperWithValue(alpha)];
                                        #          }
                                        #          [result autorelease];
                                        #          return result;
                                        #     }
                                        #     // ...
                                        #
                                        #  Example (JavaScript):
                                        #
                                        #     // ...
                                        #
                                        #     var protoToCssColor = function(rgb_color) {
                                        #        var redFrac = rgb_color.red || 0.0;
                                        #        var greenFrac = rgb_color.green || 0.0;
                                        #        var blueFrac = rgb_color.blue || 0.0;
                                        #        var red = Math.floor(redFrac * 255);
                                        #        var green = Math.floor(greenFrac * 255);
                                        #        var blue = Math.floor(blueFrac * 255);
                                        #
                                        #        if (!('alpha' in rgb_color)) {
                                        #           return rgbToCssColor_(red, green, blue);
                                        #        }
                                        #
                                        #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                        #        var rgbParams = [red, green, blue].join(',');
                                        #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                        #     };
                                        #
                                        #     var rgbToCssColor_ = function(red, green, blue) {
                                        #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                        #       var hexString = rgbNumber.toString(16);
                                        #       var missingZeros = 6 - hexString.length;
                                        #       var resultBuilder = ['#'];
                                        #       for (var i = 0; i < missingZeros; i++) {
                                        #          resultBuilder.push('0');
                                        #       }
                                        #       resultBuilder.push(hexString);
                                        #       return resultBuilder.join('');
                                        #     };
                                        #
                                        #     // ...
                                        "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                        "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                        # the final pixel color is defined by the equation:
                                        #
                                        #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                        #
                                        # This means that a value of 1.0 corresponds to a solid color, whereas
                                        # a value of 0.0 corresponds to a completely transparent color. This
                                        # uses a wrapper message rather than a simple float scalar so that it is
                                        # possible to distinguish between a default value and the value being unset.
                                        # If omitted, this color object is to be rendered as a solid color
                                        # (as if the alpha value had been explicitly given with a value of 1.0).
                                        "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                        "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                    },
                                },
                                "label": "A String",  # The label of the column's legend.
                            },
                            "subtotalColumnsStyle": {  # Styles for a waterfall chart column. # Styles for all subtotal columns in this series.
                                "color": {  # Represents a color in the RGBA color space. This representation is designed # The color of the column.
                                    # for simplicity of conversion to/from color representations in various
                                    # languages over compactness; for example, the fields of this representation
                                    # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                    # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                    # method in iOS; and, with just a little work, it can be easily formatted into
                                    # a CSS "rgba()" string in JavaScript, as well.
                                    #
                                    # Note: this proto does not carry information about the absolute color space
                                    # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                    # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                    # space.
                                    #
                                    # Example (Java):
                                    #
                                    #      import com.google.type.Color;
                                    #
                                    #      // ...
                                    #      public static java.awt.Color fromProto(Color protocolor) {
                                    #        float alpha = protocolor.hasAlpha()
                                    #            ? protocolor.getAlpha().getValue()
                                    #            : 1.0;
                                    #
                                    #        return new java.awt.Color(
                                    #            protocolor.getRed(),
                                    #            protocolor.getGreen(),
                                    #            protocolor.getBlue(),
                                    #            alpha);
                                    #      }
                                    #
                                    #      public static Color toProto(java.awt.Color color) {
                                    #        float red = (float) color.getRed();
                                    #        float green = (float) color.getGreen();
                                    #        float blue = (float) color.getBlue();
                                    #        float denominator = 255.0;
                                    #        Color.Builder resultBuilder =
                                    #            Color
                                    #                .newBuilder()
                                    #                .setRed(red / denominator)
                                    #                .setGreen(green / denominator)
                                    #                .setBlue(blue / denominator);
                                    #        int alpha = color.getAlpha();
                                    #        if (alpha != 255) {
                                    #          result.setAlpha(
                                    #              FloatValue
                                    #                  .newBuilder()
                                    #                  .setValue(((float) alpha) / denominator)
                                    #                  .build());
                                    #        }
                                    #        return resultBuilder.build();
                                    #      }
                                    #      // ...
                                    #
                                    # Example (iOS / Obj-C):
                                    #
                                    #      // ...
                                    #      static UIColor* fromProto(Color* protocolor) {
                                    #         float red = [protocolor red];
                                    #         float green = [protocolor green];
                                    #         float blue = [protocolor blue];
                                    #         FloatValue* alpha_wrapper = [protocolor alpha];
                                    #         float alpha = 1.0;
                                    #         if (alpha_wrapper != nil) {
                                    #           alpha = [alpha_wrapper value];
                                    #         }
                                    #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                    #      }
                                    #
                                    #      static Color* toProto(UIColor* color) {
                                    #          CGFloat red, green, blue, alpha;
                                    #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                    #            return nil;
                                    #          }
                                    #          Color* result = [[Color alloc] init];
                                    #          [result setRed:red];
                                    #          [result setGreen:green];
                                    #          [result setBlue:blue];
                                    #          if (alpha <= 0.9999) {
                                    #            [result setAlpha:floatWrapperWithValue(alpha)];
                                    #          }
                                    #          [result autorelease];
                                    #          return result;
                                    #     }
                                    #     // ...
                                    #
                                    #  Example (JavaScript):
                                    #
                                    #     // ...
                                    #
                                    #     var protoToCssColor = function(rgb_color) {
                                    #        var redFrac = rgb_color.red || 0.0;
                                    #        var greenFrac = rgb_color.green || 0.0;
                                    #        var blueFrac = rgb_color.blue || 0.0;
                                    #        var red = Math.floor(redFrac * 255);
                                    #        var green = Math.floor(greenFrac * 255);
                                    #        var blue = Math.floor(blueFrac * 255);
                                    #
                                    #        if (!('alpha' in rgb_color)) {
                                    #           return rgbToCssColor_(red, green, blue);
                                    #        }
                                    #
                                    #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                    #        var rgbParams = [red, green, blue].join(',');
                                    #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                    #     };
                                    #
                                    #     var rgbToCssColor_ = function(red, green, blue) {
                                    #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                    #       var hexString = rgbNumber.toString(16);
                                    #       var missingZeros = 6 - hexString.length;
                                    #       var resultBuilder = ['#'];
                                    #       for (var i = 0; i < missingZeros; i++) {
                                    #          resultBuilder.push('0');
                                    #       }
                                    #       resultBuilder.push(hexString);
                                    #       return resultBuilder.join('');
                                    #     };
                                    #
                                    #     // ...
                                    "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                    "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                    # the final pixel color is defined by the equation:
                                    #
                                    #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                    #
                                    # This means that a value of 1.0 corresponds to a solid color, whereas
                                    # a value of 0.0 corresponds to a completely transparent color. This
                                    # uses a wrapper message rather than a simple float scalar so that it is
                                    # possible to distinguish between a default value and the value being unset.
                                    # If omitted, this color object is to be rendered as a solid color
                                    # (as if the alpha value had been explicitly given with a value of 1.0).
                                    "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                    "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                },
                                "colorStyle": {  # A color value. # The color of the column.
                                    # If color is also set, this field takes precedence.
                                    "themeColor": "A String",  # Theme color.
                                    "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed # RGB color.
                                        # for simplicity of conversion to/from color representations in various
                                        # languages over compactness; for example, the fields of this representation
                                        # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                        # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                        # method in iOS; and, with just a little work, it can be easily formatted into
                                        # a CSS "rgba()" string in JavaScript, as well.
                                        #
                                        # Note: this proto does not carry information about the absolute color space
                                        # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                        # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                        # space.
                                        #
                                        # Example (Java):
                                        #
                                        #      import com.google.type.Color;
                                        #
                                        #      // ...
                                        #      public static java.awt.Color fromProto(Color protocolor) {
                                        #        float alpha = protocolor.hasAlpha()
                                        #            ? protocolor.getAlpha().getValue()
                                        #            : 1.0;
                                        #
                                        #        return new java.awt.Color(
                                        #            protocolor.getRed(),
                                        #            protocolor.getGreen(),
                                        #            protocolor.getBlue(),
                                        #            alpha);
                                        #      }
                                        #
                                        #      public static Color toProto(java.awt.Color color) {
                                        #        float red = (float) color.getRed();
                                        #        float green = (float) color.getGreen();
                                        #        float blue = (float) color.getBlue();
                                        #        float denominator = 255.0;
                                        #        Color.Builder resultBuilder =
                                        #            Color
                                        #                .newBuilder()
                                        #                .setRed(red / denominator)
                                        #                .setGreen(green / denominator)
                                        #                .setBlue(blue / denominator);
                                        #        int alpha = color.getAlpha();
                                        #        if (alpha != 255) {
                                        #          result.setAlpha(
                                        #              FloatValue
                                        #                  .newBuilder()
                                        #                  .setValue(((float) alpha) / denominator)
                                        #                  .build());
                                        #        }
                                        #        return resultBuilder.build();
                                        #      }
                                        #      // ...
                                        #
                                        # Example (iOS / Obj-C):
                                        #
                                        #      // ...
                                        #      static UIColor* fromProto(Color* protocolor) {
                                        #         float red = [protocolor red];
                                        #         float green = [protocolor green];
                                        #         float blue = [protocolor blue];
                                        #         FloatValue* alpha_wrapper = [protocolor alpha];
                                        #         float alpha = 1.0;
                                        #         if (alpha_wrapper != nil) {
                                        #           alpha = [alpha_wrapper value];
                                        #         }
                                        #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                        #      }
                                        #
                                        #      static Color* toProto(UIColor* color) {
                                        #          CGFloat red, green, blue, alpha;
                                        #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                        #            return nil;
                                        #          }
                                        #          Color* result = [[Color alloc] init];
                                        #          [result setRed:red];
                                        #          [result setGreen:green];
                                        #          [result setBlue:blue];
                                        #          if (alpha <= 0.9999) {
                                        #            [result setAlpha:floatWrapperWithValue(alpha)];
                                        #          }
                                        #          [result autorelease];
                                        #          return result;
                                        #     }
                                        #     // ...
                                        #
                                        #  Example (JavaScript):
                                        #
                                        #     // ...
                                        #
                                        #     var protoToCssColor = function(rgb_color) {
                                        #        var redFrac = rgb_color.red || 0.0;
                                        #        var greenFrac = rgb_color.green || 0.0;
                                        #        var blueFrac = rgb_color.blue || 0.0;
                                        #        var red = Math.floor(redFrac * 255);
                                        #        var green = Math.floor(greenFrac * 255);
                                        #        var blue = Math.floor(blueFrac * 255);
                                        #
                                        #        if (!('alpha' in rgb_color)) {
                                        #           return rgbToCssColor_(red, green, blue);
                                        #        }
                                        #
                                        #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                        #        var rgbParams = [red, green, blue].join(',');
                                        #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                        #     };
                                        #
                                        #     var rgbToCssColor_ = function(red, green, blue) {
                                        #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                        #       var hexString = rgbNumber.toString(16);
                                        #       var missingZeros = 6 - hexString.length;
                                        #       var resultBuilder = ['#'];
                                        #       for (var i = 0; i < missingZeros; i++) {
                                        #          resultBuilder.push('0');
                                        #       }
                                        #       resultBuilder.push(hexString);
                                        #       return resultBuilder.join('');
                                        #     };
                                        #
                                        #     // ...
                                        "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                        "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                        # the final pixel color is defined by the equation:
                                        #
                                        #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                        #
                                        # This means that a value of 1.0 corresponds to a solid color, whereas
                                        # a value of 0.0 corresponds to a completely transparent color. This
                                        # uses a wrapper message rather than a simple float scalar so that it is
                                        # possible to distinguish between a default value and the value being unset.
                                        # If omitted, this color object is to be rendered as a solid color
                                        # (as if the alpha value had been explicitly given with a value of 1.0).
                                        "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                        "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                    },
                                },
                                "label": "A String",  # The label of the column's legend.
                            },
                            "negativeColumnsStyle": {  # Styles for a waterfall chart column. # Styles for all columns in this series with negative values.
                                "color": {  # Represents a color in the RGBA color space. This representation is designed # The color of the column.
                                    # for simplicity of conversion to/from color representations in various
                                    # languages over compactness; for example, the fields of this representation
                                    # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                    # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                    # method in iOS; and, with just a little work, it can be easily formatted into
                                    # a CSS "rgba()" string in JavaScript, as well.
                                    #
                                    # Note: this proto does not carry information about the absolute color space
                                    # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                    # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                    # space.
                                    #
                                    # Example (Java):
                                    #
                                    #      import com.google.type.Color;
                                    #
                                    #      // ...
                                    #      public static java.awt.Color fromProto(Color protocolor) {
                                    #        float alpha = protocolor.hasAlpha()
                                    #            ? protocolor.getAlpha().getValue()
                                    #            : 1.0;
                                    #
                                    #        return new java.awt.Color(
                                    #            protocolor.getRed(),
                                    #            protocolor.getGreen(),
                                    #            protocolor.getBlue(),
                                    #            alpha);
                                    #      }
                                    #
                                    #      public static Color toProto(java.awt.Color color) {
                                    #        float red = (float) color.getRed();
                                    #        float green = (float) color.getGreen();
                                    #        float blue = (float) color.getBlue();
                                    #        float denominator = 255.0;
                                    #        Color.Builder resultBuilder =
                                    #            Color
                                    #                .newBuilder()
                                    #                .setRed(red / denominator)
                                    #                .setGreen(green / denominator)
                                    #                .setBlue(blue / denominator);
                                    #        int alpha = color.getAlpha();
                                    #        if (alpha != 255) {
                                    #          result.setAlpha(
                                    #              FloatValue
                                    #                  .newBuilder()
                                    #                  .setValue(((float) alpha) / denominator)
                                    #                  .build());
                                    #        }
                                    #        return resultBuilder.build();
                                    #      }
                                    #      // ...
                                    #
                                    # Example (iOS / Obj-C):
                                    #
                                    #      // ...
                                    #      static UIColor* fromProto(Color* protocolor) {
                                    #         float red = [protocolor red];
                                    #         float green = [protocolor green];
                                    #         float blue = [protocolor blue];
                                    #         FloatValue* alpha_wrapper = [protocolor alpha];
                                    #         float alpha = 1.0;
                                    #         if (alpha_wrapper != nil) {
                                    #           alpha = [alpha_wrapper value];
                                    #         }
                                    #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                    #      }
                                    #
                                    #      static Color* toProto(UIColor* color) {
                                    #          CGFloat red, green, blue, alpha;
                                    #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                    #            return nil;
                                    #          }
                                    #          Color* result = [[Color alloc] init];
                                    #          [result setRed:red];
                                    #          [result setGreen:green];
                                    #          [result setBlue:blue];
                                    #          if (alpha <= 0.9999) {
                                    #            [result setAlpha:floatWrapperWithValue(alpha)];
                                    #          }
                                    #          [result autorelease];
                                    #          return result;
                                    #     }
                                    #     // ...
                                    #
                                    #  Example (JavaScript):
                                    #
                                    #     // ...
                                    #
                                    #     var protoToCssColor = function(rgb_color) {
                                    #        var redFrac = rgb_color.red || 0.0;
                                    #        var greenFrac = rgb_color.green || 0.0;
                                    #        var blueFrac = rgb_color.blue || 0.0;
                                    #        var red = Math.floor(redFrac * 255);
                                    #        var green = Math.floor(greenFrac * 255);
                                    #        var blue = Math.floor(blueFrac * 255);
                                    #
                                    #        if (!('alpha' in rgb_color)) {
                                    #           return rgbToCssColor_(red, green, blue);
                                    #        }
                                    #
                                    #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                    #        var rgbParams = [red, green, blue].join(',');
                                    #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                    #     };
                                    #
                                    #     var rgbToCssColor_ = function(red, green, blue) {
                                    #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                    #       var hexString = rgbNumber.toString(16);
                                    #       var missingZeros = 6 - hexString.length;
                                    #       var resultBuilder = ['#'];
                                    #       for (var i = 0; i < missingZeros; i++) {
                                    #          resultBuilder.push('0');
                                    #       }
                                    #       resultBuilder.push(hexString);
                                    #       return resultBuilder.join('');
                                    #     };
                                    #
                                    #     // ...
                                    "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                    "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                    # the final pixel color is defined by the equation:
                                    #
                                    #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                    #
                                    # This means that a value of 1.0 corresponds to a solid color, whereas
                                    # a value of 0.0 corresponds to a completely transparent color. This
                                    # uses a wrapper message rather than a simple float scalar so that it is
                                    # possible to distinguish between a default value and the value being unset.
                                    # If omitted, this color object is to be rendered as a solid color
                                    # (as if the alpha value had been explicitly given with a value of 1.0).
                                    "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                    "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                },
                                "colorStyle": {  # A color value. # The color of the column.
                                    # If color is also set, this field takes precedence.
                                    "themeColor": "A String",  # Theme color.
                                    "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed # RGB color.
                                        # for simplicity of conversion to/from color representations in various
                                        # languages over compactness; for example, the fields of this representation
                                        # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                        # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                        # method in iOS; and, with just a little work, it can be easily formatted into
                                        # a CSS "rgba()" string in JavaScript, as well.
                                        #
                                        # Note: this proto does not carry information about the absolute color space
                                        # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                        # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                        # space.
                                        #
                                        # Example (Java):
                                        #
                                        #      import com.google.type.Color;
                                        #
                                        #      // ...
                                        #      public static java.awt.Color fromProto(Color protocolor) {
                                        #        float alpha = protocolor.hasAlpha()
                                        #            ? protocolor.getAlpha().getValue()
                                        #            : 1.0;
                                        #
                                        #        return new java.awt.Color(
                                        #            protocolor.getRed(),
                                        #            protocolor.getGreen(),
                                        #            protocolor.getBlue(),
                                        #            alpha);
                                        #      }
                                        #
                                        #      public static Color toProto(java.awt.Color color) {
                                        #        float red = (float) color.getRed();
                                        #        float green = (float) color.getGreen();
                                        #        float blue = (float) color.getBlue();
                                        #        float denominator = 255.0;
                                        #        Color.Builder resultBuilder =
                                        #            Color
                                        #                .newBuilder()
                                        #                .setRed(red / denominator)
                                        #                .setGreen(green / denominator)
                                        #                .setBlue(blue / denominator);
                                        #        int alpha = color.getAlpha();
                                        #        if (alpha != 255) {
                                        #          result.setAlpha(
                                        #              FloatValue
                                        #                  .newBuilder()
                                        #                  .setValue(((float) alpha) / denominator)
                                        #                  .build());
                                        #        }
                                        #        return resultBuilder.build();
                                        #      }
                                        #      // ...
                                        #
                                        # Example (iOS / Obj-C):
                                        #
                                        #      // ...
                                        #      static UIColor* fromProto(Color* protocolor) {
                                        #         float red = [protocolor red];
                                        #         float green = [protocolor green];
                                        #         float blue = [protocolor blue];
                                        #         FloatValue* alpha_wrapper = [protocolor alpha];
                                        #         float alpha = 1.0;
                                        #         if (alpha_wrapper != nil) {
                                        #           alpha = [alpha_wrapper value];
                                        #         }
                                        #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                        #      }
                                        #
                                        #      static Color* toProto(UIColor* color) {
                                        #          CGFloat red, green, blue, alpha;
                                        #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                        #            return nil;
                                        #          }
                                        #          Color* result = [[Color alloc] init];
                                        #          [result setRed:red];
                                        #          [result setGreen:green];
                                        #          [result setBlue:blue];
                                        #          if (alpha <= 0.9999) {
                                        #            [result setAlpha:floatWrapperWithValue(alpha)];
                                        #          }
                                        #          [result autorelease];
                                        #          return result;
                                        #     }
                                        #     // ...
                                        #
                                        #  Example (JavaScript):
                                        #
                                        #     // ...
                                        #
                                        #     var protoToCssColor = function(rgb_color) {
                                        #        var redFrac = rgb_color.red || 0.0;
                                        #        var greenFrac = rgb_color.green || 0.0;
                                        #        var blueFrac = rgb_color.blue || 0.0;
                                        #        var red = Math.floor(redFrac * 255);
                                        #        var green = Math.floor(greenFrac * 255);
                                        #        var blue = Math.floor(blueFrac * 255);
                                        #
                                        #        if (!('alpha' in rgb_color)) {
                                        #           return rgbToCssColor_(red, green, blue);
                                        #        }
                                        #
                                        #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                        #        var rgbParams = [red, green, blue].join(',');
                                        #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                        #     };
                                        #
                                        #     var rgbToCssColor_ = function(red, green, blue) {
                                        #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                        #       var hexString = rgbNumber.toString(16);
                                        #       var missingZeros = 6 - hexString.length;
                                        #       var resultBuilder = ['#'];
                                        #       for (var i = 0; i < missingZeros; i++) {
                                        #          resultBuilder.push('0');
                                        #       }
                                        #       resultBuilder.push(hexString);
                                        #       return resultBuilder.join('');
                                        #     };
                                        #
                                        #     // ...
                                        "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                        "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                        # the final pixel color is defined by the equation:
                                        #
                                        #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                        #
                                        # This means that a value of 1.0 corresponds to a solid color, whereas
                                        # a value of 0.0 corresponds to a completely transparent color. This
                                        # uses a wrapper message rather than a simple float scalar so that it is
                                        # possible to distinguish between a default value and the value being unset.
                                        # If omitted, this color object is to be rendered as a solid color
                                        # (as if the alpha value had been explicitly given with a value of 1.0).
                                        "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                        "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                    },
                                },
                                "label": "A String",  # The label of the column's legend.
                            },
                            "customSubtotals": [  # Custom subtotal columns appearing in this series. The order in which
                                # subtotals are defined is not significant. Only one subtotal may be
                                # defined for each data point.
                                {  # A custom subtotal column for a waterfall chart series.
                                    "dataIsSubtotal": True
                                    or False,  # True if the data point at subtotal_index is the subtotal. If false,
                                    # the subtotal will be computed and appear after the data point.
                                    "subtotalIndex": 42,  # The 0-based index of a data point within the series. If
                                    # data_is_subtotal is true, the data point at this index is the
                                    # subtotal. Otherwise, the subtotal appears after the data point with
                                    # this index. A series can have multiple subtotals at arbitrary indices,
                                    # but subtotals do not affect the indices of the data points. For
                                    # example, if a series has three data points, their indices will always
                                    # be 0, 1, and 2, regardless of how many subtotals exist on the series or
                                    # what data points they are associated with.
                                    "label": "A String",  # A label for the subtotal column.
                                },
                            ],
                            "data": {  # The data included in a domain or series. # The data being visualized in this series.
                                "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                                    "sources": [  # The ranges of data for a series or domain.
                                        # Exactly one dimension must have a length of 1,
                                        # and all sources in the list must have the same dimension
                                        # with length 1.
                                        # The domain (if it exists) & all series must have the same number
                                        # of source ranges. If using more than one source range, then the source
                                        # range at a given offset must be in order and contiguous across the domain
                                        # and series.
                                        #
                                        # For example, these are valid configurations:
                                        #
                                        #     domain sources: A1:A5
                                        #     series1 sources: B1:B5
                                        #     series2 sources: D6:D10
                                        #
                                        #     domain sources: A1:A5, C10:C12
                                        #     series1 sources: B1:B5, D10:D12
                                        #     series2 sources: C1:C5, E10:E12
                                        {  # A range on a sheet.
                                            # All indexes are zero-based.
                                            # Indexes are half open, e.g the start index is inclusive
                                            # and the end index is exclusive -- [start_index, end_index).
                                            # Missing indexes indicate the range is unbounded on that side.
                                            #
                                            # For example, if `"Sheet1"` is sheet ID 0, then:
                                            #
                                            #   `Sheet1!A1:A1 == sheet_id: 0,
                                            #                   start_row_index: 0, end_row_index: 1,
                                            #                   start_column_index: 0, end_column_index: 1`
                                            #
                                            #   `Sheet1!A3:B4 == sheet_id: 0,
                                            #                   start_row_index: 2, end_row_index: 4,
                                            #                   start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1!A:B == sheet_id: 0,
                                            #                 start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1!A5:B == sheet_id: 0,
                                            #                  start_row_index: 4,
                                            #                  start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1 == sheet_id:0`
                                            #
                                            # The start index must always be less than or equal to the end index.
                                            # If the start index equals the end index, then the range is empty.
                                            # Empty ranges are typically not meaningful and are usually rendered in the
                                            # UI as `#REF!`.
                                            "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                            "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                            "sheetId": 42,  # The sheet this range is on.
                                            "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                            "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                        },
                                    ],
                                },
                            },
                        },
                    ],
                    "firstValueIsTotal": True
                    or False,  # True to interpret the first value as a total.
                },
                "basicChart": {  # The specification for a basic chart.  See BasicChartType for the list # A basic chart specification, can be one of many kinds of charts.
                    # See BasicChartType for the list of all
                    # charts this supports.
                    # of charts this supports.
                    "stackedType": "A String",  # The stacked type for charts that support vertical stacking.
                    # Applies to Area, Bar, Column, Combo, and Stepped Area charts.
                    "compareMode": "A String",  # The behavior of tooltips and data highlighting when hovering on data and
                    # chart area.
                    "lineSmoothing": True
                    or False,  # Gets whether all lines should be rendered smooth or straight by default.
                    # Applies to Line charts.
                    "series": [  # The data this chart is visualizing.
                        {  # A single series of data in a chart.
                            # For example, if charting stock prices over time, multiple series may exist,
                            # one for the "Open Price", "High Price", "Low Price" and "Close Price".
                            "targetAxis": "A String",  # The minor axis that will specify the range of values for this series.
                            # For example, if charting stocks over time, the "Volume" series
                            # may want to be pinned to the right with the prices pinned to the left,
                            # because the scale of trading volume is different than the scale of
                            # prices.
                            # It is an error to specify an axis that isn't a valid minor axis
                            # for the chart's type.
                            "color": {  # Represents a color in the RGBA color space. This representation is designed # The color for elements (such as bars, lines, and points) associated with
                                # this series.  If empty, a default color is used.
                                # for simplicity of conversion to/from color representations in various
                                # languages over compactness; for example, the fields of this representation
                                # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                # method in iOS; and, with just a little work, it can be easily formatted into
                                # a CSS "rgba()" string in JavaScript, as well.
                                #
                                # Note: this proto does not carry information about the absolute color space
                                # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                # space.
                                #
                                # Example (Java):
                                #
                                #      import com.google.type.Color;
                                #
                                #      // ...
                                #      public static java.awt.Color fromProto(Color protocolor) {
                                #        float alpha = protocolor.hasAlpha()
                                #            ? protocolor.getAlpha().getValue()
                                #            : 1.0;
                                #
                                #        return new java.awt.Color(
                                #            protocolor.getRed(),
                                #            protocolor.getGreen(),
                                #            protocolor.getBlue(),
                                #            alpha);
                                #      }
                                #
                                #      public static Color toProto(java.awt.Color color) {
                                #        float red = (float) color.getRed();
                                #        float green = (float) color.getGreen();
                                #        float blue = (float) color.getBlue();
                                #        float denominator = 255.0;
                                #        Color.Builder resultBuilder =
                                #            Color
                                #                .newBuilder()
                                #                .setRed(red / denominator)
                                #                .setGreen(green / denominator)
                                #                .setBlue(blue / denominator);
                                #        int alpha = color.getAlpha();
                                #        if (alpha != 255) {
                                #          result.setAlpha(
                                #              FloatValue
                                #                  .newBuilder()
                                #                  .setValue(((float) alpha) / denominator)
                                #                  .build());
                                #        }
                                #        return resultBuilder.build();
                                #      }
                                #      // ...
                                #
                                # Example (iOS / Obj-C):
                                #
                                #      // ...
                                #      static UIColor* fromProto(Color* protocolor) {
                                #         float red = [protocolor red];
                                #         float green = [protocolor green];
                                #         float blue = [protocolor blue];
                                #         FloatValue* alpha_wrapper = [protocolor alpha];
                                #         float alpha = 1.0;
                                #         if (alpha_wrapper != nil) {
                                #           alpha = [alpha_wrapper value];
                                #         }
                                #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                #      }
                                #
                                #      static Color* toProto(UIColor* color) {
                                #          CGFloat red, green, blue, alpha;
                                #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                #            return nil;
                                #          }
                                #          Color* result = [[Color alloc] init];
                                #          [result setRed:red];
                                #          [result setGreen:green];
                                #          [result setBlue:blue];
                                #          if (alpha <= 0.9999) {
                                #            [result setAlpha:floatWrapperWithValue(alpha)];
                                #          }
                                #          [result autorelease];
                                #          return result;
                                #     }
                                #     // ...
                                #
                                #  Example (JavaScript):
                                #
                                #     // ...
                                #
                                #     var protoToCssColor = function(rgb_color) {
                                #        var redFrac = rgb_color.red || 0.0;
                                #        var greenFrac = rgb_color.green || 0.0;
                                #        var blueFrac = rgb_color.blue || 0.0;
                                #        var red = Math.floor(redFrac * 255);
                                #        var green = Math.floor(greenFrac * 255);
                                #        var blue = Math.floor(blueFrac * 255);
                                #
                                #        if (!('alpha' in rgb_color)) {
                                #           return rgbToCssColor_(red, green, blue);
                                #        }
                                #
                                #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                #        var rgbParams = [red, green, blue].join(',');
                                #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                #     };
                                #
                                #     var rgbToCssColor_ = function(red, green, blue) {
                                #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                #       var hexString = rgbNumber.toString(16);
                                #       var missingZeros = 6 - hexString.length;
                                #       var resultBuilder = ['#'];
                                #       for (var i = 0; i < missingZeros; i++) {
                                #          resultBuilder.push('0');
                                #       }
                                #       resultBuilder.push(hexString);
                                #       return resultBuilder.join('');
                                #     };
                                #
                                #     // ...
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                # the final pixel color is defined by the equation:
                                #
                                #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                #
                                # This means that a value of 1.0 corresponds to a solid color, whereas
                                # a value of 0.0 corresponds to a completely transparent color. This
                                # uses a wrapper message rather than a simple float scalar so that it is
                                # possible to distinguish between a default value and the value being unset.
                                # If omitted, this color object is to be rendered as a solid color
                                # (as if the alpha value had been explicitly given with a value of 1.0).
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                            "lineStyle": {  # Properties that describe the style of a line. # The line style of this series. Valid only if the
                                # chartType is AREA,
                                # LINE, or SCATTER.
                                # COMBO charts are also supported if the
                                # series chart type is
                                # AREA or LINE.
                                "width": 42,  # The thickness of the line, in px.
                                "type": "A String",  # The dash type of the line.
                            },
                            "colorStyle": {  # A color value. # The color for elements (such as bars, lines, and points) associated with
                                # this series.  If empty, a default color is used.
                                # If color is also set, this field takes precedence.
                                "themeColor": "A String",  # Theme color.
                                "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed # RGB color.
                                    # for simplicity of conversion to/from color representations in various
                                    # languages over compactness; for example, the fields of this representation
                                    # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                    # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                    # method in iOS; and, with just a little work, it can be easily formatted into
                                    # a CSS "rgba()" string in JavaScript, as well.
                                    #
                                    # Note: this proto does not carry information about the absolute color space
                                    # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                    # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                    # space.
                                    #
                                    # Example (Java):
                                    #
                                    #      import com.google.type.Color;
                                    #
                                    #      // ...
                                    #      public static java.awt.Color fromProto(Color protocolor) {
                                    #        float alpha = protocolor.hasAlpha()
                                    #            ? protocolor.getAlpha().getValue()
                                    #            : 1.0;
                                    #
                                    #        return new java.awt.Color(
                                    #            protocolor.getRed(),
                                    #            protocolor.getGreen(),
                                    #            protocolor.getBlue(),
                                    #            alpha);
                                    #      }
                                    #
                                    #      public static Color toProto(java.awt.Color color) {
                                    #        float red = (float) color.getRed();
                                    #        float green = (float) color.getGreen();
                                    #        float blue = (float) color.getBlue();
                                    #        float denominator = 255.0;
                                    #        Color.Builder resultBuilder =
                                    #            Color
                                    #                .newBuilder()
                                    #                .setRed(red / denominator)
                                    #                .setGreen(green / denominator)
                                    #                .setBlue(blue / denominator);
                                    #        int alpha = color.getAlpha();
                                    #        if (alpha != 255) {
                                    #          result.setAlpha(
                                    #              FloatValue
                                    #                  .newBuilder()
                                    #                  .setValue(((float) alpha) / denominator)
                                    #                  .build());
                                    #        }
                                    #        return resultBuilder.build();
                                    #      }
                                    #      // ...
                                    #
                                    # Example (iOS / Obj-C):
                                    #
                                    #      // ...
                                    #      static UIColor* fromProto(Color* protocolor) {
                                    #         float red = [protocolor red];
                                    #         float green = [protocolor green];
                                    #         float blue = [protocolor blue];
                                    #         FloatValue* alpha_wrapper = [protocolor alpha];
                                    #         float alpha = 1.0;
                                    #         if (alpha_wrapper != nil) {
                                    #           alpha = [alpha_wrapper value];
                                    #         }
                                    #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                    #      }
                                    #
                                    #      static Color* toProto(UIColor* color) {
                                    #          CGFloat red, green, blue, alpha;
                                    #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                    #            return nil;
                                    #          }
                                    #          Color* result = [[Color alloc] init];
                                    #          [result setRed:red];
                                    #          [result setGreen:green];
                                    #          [result setBlue:blue];
                                    #          if (alpha <= 0.9999) {
                                    #            [result setAlpha:floatWrapperWithValue(alpha)];
                                    #          }
                                    #          [result autorelease];
                                    #          return result;
                                    #     }
                                    #     // ...
                                    #
                                    #  Example (JavaScript):
                                    #
                                    #     // ...
                                    #
                                    #     var protoToCssColor = function(rgb_color) {
                                    #        var redFrac = rgb_color.red || 0.0;
                                    #        var greenFrac = rgb_color.green || 0.0;
                                    #        var blueFrac = rgb_color.blue || 0.0;
                                    #        var red = Math.floor(redFrac * 255);
                                    #        var green = Math.floor(greenFrac * 255);
                                    #        var blue = Math.floor(blueFrac * 255);
                                    #
                                    #        if (!('alpha' in rgb_color)) {
                                    #           return rgbToCssColor_(red, green, blue);
                                    #        }
                                    #
                                    #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                    #        var rgbParams = [red, green, blue].join(',');
                                    #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                    #     };
                                    #
                                    #     var rgbToCssColor_ = function(red, green, blue) {
                                    #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                    #       var hexString = rgbNumber.toString(16);
                                    #       var missingZeros = 6 - hexString.length;
                                    #       var resultBuilder = ['#'];
                                    #       for (var i = 0; i < missingZeros; i++) {
                                    #          resultBuilder.push('0');
                                    #       }
                                    #       resultBuilder.push(hexString);
                                    #       return resultBuilder.join('');
                                    #     };
                                    #
                                    #     // ...
                                    "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                    "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                    # the final pixel color is defined by the equation:
                                    #
                                    #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                    #
                                    # This means that a value of 1.0 corresponds to a solid color, whereas
                                    # a value of 0.0 corresponds to a completely transparent color. This
                                    # uses a wrapper message rather than a simple float scalar so that it is
                                    # possible to distinguish between a default value and the value being unset.
                                    # If omitted, this color object is to be rendered as a solid color
                                    # (as if the alpha value had been explicitly given with a value of 1.0).
                                    "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                    "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                },
                            },
                            "series": {  # The data included in a domain or series. # The data being visualized in this chart series.
                                "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                                    "sources": [  # The ranges of data for a series or domain.
                                        # Exactly one dimension must have a length of 1,
                                        # and all sources in the list must have the same dimension
                                        # with length 1.
                                        # The domain (if it exists) & all series must have the same number
                                        # of source ranges. If using more than one source range, then the source
                                        # range at a given offset must be in order and contiguous across the domain
                                        # and series.
                                        #
                                        # For example, these are valid configurations:
                                        #
                                        #     domain sources: A1:A5
                                        #     series1 sources: B1:B5
                                        #     series2 sources: D6:D10
                                        #
                                        #     domain sources: A1:A5, C10:C12
                                        #     series1 sources: B1:B5, D10:D12
                                        #     series2 sources: C1:C5, E10:E12
                                        {  # A range on a sheet.
                                            # All indexes are zero-based.
                                            # Indexes are half open, e.g the start index is inclusive
                                            # and the end index is exclusive -- [start_index, end_index).
                                            # Missing indexes indicate the range is unbounded on that side.
                                            #
                                            # For example, if `"Sheet1"` is sheet ID 0, then:
                                            #
                                            #   `Sheet1!A1:A1 == sheet_id: 0,
                                            #                   start_row_index: 0, end_row_index: 1,
                                            #                   start_column_index: 0, end_column_index: 1`
                                            #
                                            #   `Sheet1!A3:B4 == sheet_id: 0,
                                            #                   start_row_index: 2, end_row_index: 4,
                                            #                   start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1!A:B == sheet_id: 0,
                                            #                 start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1!A5:B == sheet_id: 0,
                                            #                  start_row_index: 4,
                                            #                  start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1 == sheet_id:0`
                                            #
                                            # The start index must always be less than or equal to the end index.
                                            # If the start index equals the end index, then the range is empty.
                                            # Empty ranges are typically not meaningful and are usually rendered in the
                                            # UI as `#REF!`.
                                            "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                            "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                            "sheetId": 42,  # The sheet this range is on.
                                            "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                            "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                        },
                                    ],
                                },
                            },
                            "type": "A String",  # The type of this series. Valid only if the
                            # chartType is
                            # COMBO.
                            # Different types will change the way the series is visualized.
                            # Only LINE, AREA,
                            # and COLUMN are supported.
                        },
                    ],
                    "headerCount": 42,  # The number of rows or columns in the data that are "headers".
                    # If not set, Google Sheets will guess how many rows are headers based
                    # on the data.
                    #
                    # (Note that BasicChartAxis.title may override the axis title
                    #  inferred from the header values.)
                    "legendPosition": "A String",  # The position of the chart legend.
                    "interpolateNulls": True
                    or False,  # If some values in a series are missing, gaps may appear in the chart (e.g,
                    # segments of lines in a line chart will be missing).  To eliminate these
                    # gaps set this to true.
                    # Applies to Line, Area, and Combo charts.
                    "threeDimensional": True or False,  # True to make the chart 3D.
                    # Applies to Bar and Column charts.
                    "domains": [  # The domain of data this is charting.
                        # Only a single domain is supported.
                        {  # The domain of a chart.
                            # For example, if charting stock prices over time, this would be the date.
                            "domain": {  # The data included in a domain or series. # The data of the domain. For example, if charting stock prices over time,
                                # this is the data representing the dates.
                                "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                                    "sources": [  # The ranges of data for a series or domain.
                                        # Exactly one dimension must have a length of 1,
                                        # and all sources in the list must have the same dimension
                                        # with length 1.
                                        # The domain (if it exists) & all series must have the same number
                                        # of source ranges. If using more than one source range, then the source
                                        # range at a given offset must be in order and contiguous across the domain
                                        # and series.
                                        #
                                        # For example, these are valid configurations:
                                        #
                                        #     domain sources: A1:A5
                                        #     series1 sources: B1:B5
                                        #     series2 sources: D6:D10
                                        #
                                        #     domain sources: A1:A5, C10:C12
                                        #     series1 sources: B1:B5, D10:D12
                                        #     series2 sources: C1:C5, E10:E12
                                        {  # A range on a sheet.
                                            # All indexes are zero-based.
                                            # Indexes are half open, e.g the start index is inclusive
                                            # and the end index is exclusive -- [start_index, end_index).
                                            # Missing indexes indicate the range is unbounded on that side.
                                            #
                                            # For example, if `"Sheet1"` is sheet ID 0, then:
                                            #
                                            #   `Sheet1!A1:A1 == sheet_id: 0,
                                            #                   start_row_index: 0, end_row_index: 1,
                                            #                   start_column_index: 0, end_column_index: 1`
                                            #
                                            #   `Sheet1!A3:B4 == sheet_id: 0,
                                            #                   start_row_index: 2, end_row_index: 4,
                                            #                   start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1!A:B == sheet_id: 0,
                                            #                 start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1!A5:B == sheet_id: 0,
                                            #                  start_row_index: 4,
                                            #                  start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1 == sheet_id:0`
                                            #
                                            # The start index must always be less than or equal to the end index.
                                            # If the start index equals the end index, then the range is empty.
                                            # Empty ranges are typically not meaningful and are usually rendered in the
                                            # UI as `#REF!`.
                                            "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                            "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                            "sheetId": 42,  # The sheet this range is on.
                                            "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                            "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                        },
                                    ],
                                },
                            },
                            "reversed": True
                            or False,  # True to reverse the order of the domain values (horizontal axis).
                        },
                    ],
                    "chartType": "A String",  # The type of the chart.
                    "axis": [  # The axis on the chart.
                        {  # An axis of the chart.
                            # A chart may not have more than one axis per
                            # axis position.
                            "position": "A String",  # The position of this axis.
                            "viewWindowOptions": {  # The options that define a "view window" for a chart (such as the visible # The view window options for this axis.
                                # values in an axis).
                                "viewWindowMin": 3.14,  # The minimum numeric value to be shown in this view window. If unset, will
                                # automatically determine a minimum value that looks good for the data.
                                "viewWindowMax": 3.14,  # The maximum numeric value to be shown in this view window. If unset, will
                                # automatically determine a maximum value that looks good for the data.
                                "viewWindowMode": "A String",  # The view window's mode.
                            },
                            "format": {  # The format of a run of text in a cell. # The format of the title.
                                # Only valid if the axis is not associated with the domain.
                                # Absent values indicate that the field isn't specified.
                                "foregroundColor": {  # Represents a color in the RGBA color space. This representation is designed # The foreground color of the text.
                                    # for simplicity of conversion to/from color representations in various
                                    # languages over compactness; for example, the fields of this representation
                                    # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                    # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                    # method in iOS; and, with just a little work, it can be easily formatted into
                                    # a CSS "rgba()" string in JavaScript, as well.
                                    #
                                    # Note: this proto does not carry information about the absolute color space
                                    # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                    # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                    # space.
                                    #
                                    # Example (Java):
                                    #
                                    #      import com.google.type.Color;
                                    #
                                    #      // ...
                                    #      public static java.awt.Color fromProto(Color protocolor) {
                                    #        float alpha = protocolor.hasAlpha()
                                    #            ? protocolor.getAlpha().getValue()
                                    #            : 1.0;
                                    #
                                    #        return new java.awt.Color(
                                    #            protocolor.getRed(),
                                    #            protocolor.getGreen(),
                                    #            protocolor.getBlue(),
                                    #            alpha);
                                    #      }
                                    #
                                    #      public static Color toProto(java.awt.Color color) {
                                    #        float red = (float) color.getRed();
                                    #        float green = (float) color.getGreen();
                                    #        float blue = (float) color.getBlue();
                                    #        float denominator = 255.0;
                                    #        Color.Builder resultBuilder =
                                    #            Color
                                    #                .newBuilder()
                                    #                .setRed(red / denominator)
                                    #                .setGreen(green / denominator)
                                    #                .setBlue(blue / denominator);
                                    #        int alpha = color.getAlpha();
                                    #        if (alpha != 255) {
                                    #          result.setAlpha(
                                    #              FloatValue
                                    #                  .newBuilder()
                                    #                  .setValue(((float) alpha) / denominator)
                                    #                  .build());
                                    #        }
                                    #        return resultBuilder.build();
                                    #      }
                                    #      // ...
                                    #
                                    # Example (iOS / Obj-C):
                                    #
                                    #      // ...
                                    #      static UIColor* fromProto(Color* protocolor) {
                                    #         float red = [protocolor red];
                                    #         float green = [protocolor green];
                                    #         float blue = [protocolor blue];
                                    #         FloatValue* alpha_wrapper = [protocolor alpha];
                                    #         float alpha = 1.0;
                                    #         if (alpha_wrapper != nil) {
                                    #           alpha = [alpha_wrapper value];
                                    #         }
                                    #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                    #      }
                                    #
                                    #      static Color* toProto(UIColor* color) {
                                    #          CGFloat red, green, blue, alpha;
                                    #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                    #            return nil;
                                    #          }
                                    #          Color* result = [[Color alloc] init];
                                    #          [result setRed:red];
                                    #          [result setGreen:green];
                                    #          [result setBlue:blue];
                                    #          if (alpha <= 0.9999) {
                                    #            [result setAlpha:floatWrapperWithValue(alpha)];
                                    #          }
                                    #          [result autorelease];
                                    #          return result;
                                    #     }
                                    #     // ...
                                    #
                                    #  Example (JavaScript):
                                    #
                                    #     // ...
                                    #
                                    #     var protoToCssColor = function(rgb_color) {
                                    #        var redFrac = rgb_color.red || 0.0;
                                    #        var greenFrac = rgb_color.green || 0.0;
                                    #        var blueFrac = rgb_color.blue || 0.0;
                                    #        var red = Math.floor(redFrac * 255);
                                    #        var green = Math.floor(greenFrac * 255);
                                    #        var blue = Math.floor(blueFrac * 255);
                                    #
                                    #        if (!('alpha' in rgb_color)) {
                                    #           return rgbToCssColor_(red, green, blue);
                                    #        }
                                    #
                                    #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                    #        var rgbParams = [red, green, blue].join(',');
                                    #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                    #     };
                                    #
                                    #     var rgbToCssColor_ = function(red, green, blue) {
                                    #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                    #       var hexString = rgbNumber.toString(16);
                                    #       var missingZeros = 6 - hexString.length;
                                    #       var resultBuilder = ['#'];
                                    #       for (var i = 0; i < missingZeros; i++) {
                                    #          resultBuilder.push('0');
                                    #       }
                                    #       resultBuilder.push(hexString);
                                    #       return resultBuilder.join('');
                                    #     };
                                    #
                                    #     // ...
                                    "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                    "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                    # the final pixel color is defined by the equation:
                                    #
                                    #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                    #
                                    # This means that a value of 1.0 corresponds to a solid color, whereas
                                    # a value of 0.0 corresponds to a completely transparent color. This
                                    # uses a wrapper message rather than a simple float scalar so that it is
                                    # possible to distinguish between a default value and the value being unset.
                                    # If omitted, this color object is to be rendered as a solid color
                                    # (as if the alpha value had been explicitly given with a value of 1.0).
                                    "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                    "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                },
                                "bold": True or False,  # True if the text is bold.
                                "foregroundColorStyle": {  # A color value. # The foreground color of the text.
                                    # If foreground_color is also set, this field takes precedence.
                                    "themeColor": "A String",  # Theme color.
                                    "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed # RGB color.
                                        # for simplicity of conversion to/from color representations in various
                                        # languages over compactness; for example, the fields of this representation
                                        # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                        # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                        # method in iOS; and, with just a little work, it can be easily formatted into
                                        # a CSS "rgba()" string in JavaScript, as well.
                                        #
                                        # Note: this proto does not carry information about the absolute color space
                                        # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                        # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                        # space.
                                        #
                                        # Example (Java):
                                        #
                                        #      import com.google.type.Color;
                                        #
                                        #      // ...
                                        #      public static java.awt.Color fromProto(Color protocolor) {
                                        #        float alpha = protocolor.hasAlpha()
                                        #            ? protocolor.getAlpha().getValue()
                                        #            : 1.0;
                                        #
                                        #        return new java.awt.Color(
                                        #            protocolor.getRed(),
                                        #            protocolor.getGreen(),
                                        #            protocolor.getBlue(),
                                        #            alpha);
                                        #      }
                                        #
                                        #      public static Color toProto(java.awt.Color color) {
                                        #        float red = (float) color.getRed();
                                        #        float green = (float) color.getGreen();
                                        #        float blue = (float) color.getBlue();
                                        #        float denominator = 255.0;
                                        #        Color.Builder resultBuilder =
                                        #            Color
                                        #                .newBuilder()
                                        #                .setRed(red / denominator)
                                        #                .setGreen(green / denominator)
                                        #                .setBlue(blue / denominator);
                                        #        int alpha = color.getAlpha();
                                        #        if (alpha != 255) {
                                        #          result.setAlpha(
                                        #              FloatValue
                                        #                  .newBuilder()
                                        #                  .setValue(((float) alpha) / denominator)
                                        #                  .build());
                                        #        }
                                        #        return resultBuilder.build();
                                        #      }
                                        #      // ...
                                        #
                                        # Example (iOS / Obj-C):
                                        #
                                        #      // ...
                                        #      static UIColor* fromProto(Color* protocolor) {
                                        #         float red = [protocolor red];
                                        #         float green = [protocolor green];
                                        #         float blue = [protocolor blue];
                                        #         FloatValue* alpha_wrapper = [protocolor alpha];
                                        #         float alpha = 1.0;
                                        #         if (alpha_wrapper != nil) {
                                        #           alpha = [alpha_wrapper value];
                                        #         }
                                        #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                        #      }
                                        #
                                        #      static Color* toProto(UIColor* color) {
                                        #          CGFloat red, green, blue, alpha;
                                        #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                        #            return nil;
                                        #          }
                                        #          Color* result = [[Color alloc] init];
                                        #          [result setRed:red];
                                        #          [result setGreen:green];
                                        #          [result setBlue:blue];
                                        #          if (alpha <= 0.9999) {
                                        #            [result setAlpha:floatWrapperWithValue(alpha)];
                                        #          }
                                        #          [result autorelease];
                                        #          return result;
                                        #     }
                                        #     // ...
                                        #
                                        #  Example (JavaScript):
                                        #
                                        #     // ...
                                        #
                                        #     var protoToCssColor = function(rgb_color) {
                                        #        var redFrac = rgb_color.red || 0.0;
                                        #        var greenFrac = rgb_color.green || 0.0;
                                        #        var blueFrac = rgb_color.blue || 0.0;
                                        #        var red = Math.floor(redFrac * 255);
                                        #        var green = Math.floor(greenFrac * 255);
                                        #        var blue = Math.floor(blueFrac * 255);
                                        #
                                        #        if (!('alpha' in rgb_color)) {
                                        #           return rgbToCssColor_(red, green, blue);
                                        #        }
                                        #
                                        #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                        #        var rgbParams = [red, green, blue].join(',');
                                        #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                        #     };
                                        #
                                        #     var rgbToCssColor_ = function(red, green, blue) {
                                        #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                        #       var hexString = rgbNumber.toString(16);
                                        #       var missingZeros = 6 - hexString.length;
                                        #       var resultBuilder = ['#'];
                                        #       for (var i = 0; i < missingZeros; i++) {
                                        #          resultBuilder.push('0');
                                        #       }
                                        #       resultBuilder.push(hexString);
                                        #       return resultBuilder.join('');
                                        #     };
                                        #
                                        #     // ...
                                        "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                        "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                        # the final pixel color is defined by the equation:
                                        #
                                        #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                        #
                                        # This means that a value of 1.0 corresponds to a solid color, whereas
                                        # a value of 0.0 corresponds to a completely transparent color. This
                                        # uses a wrapper message rather than a simple float scalar so that it is
                                        # possible to distinguish between a default value and the value being unset.
                                        # If omitted, this color object is to be rendered as a solid color
                                        # (as if the alpha value had been explicitly given with a value of 1.0).
                                        "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                        "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                    },
                                },
                                "strikethrough": True
                                or False,  # True if the text has a strikethrough.
                                "fontFamily": "A String",  # The font family.
                                "fontSize": 42,  # The size of the font.
                                "italic": True
                                or False,  # True if the text is italicized.
                                "underline": True
                                or False,  # True if the text is underlined.
                            },
                            "title": "A String",  # The title of this axis. If set, this overrides any title inferred
                            # from headers of the data.
                            "titleTextPosition": {  # Position settings for text. # The axis title text position.
                                "horizontalAlignment": "A String",  # Horizontal alignment setting for the piece of text.
                            },
                        },
                    ],
                },
                "histogramChart": {  # A <a href="/chart/interactive/docs/gallery/histogram">histogram chart</a>. # A histogram chart specification.
                    # A histogram chart groups data items into bins, displaying each bin as a
                    # column of stacked items.  Histograms are used to display the distribution
                    # of a dataset.  Each column of items represents a range into which those
                    # items fall.  The number of bins can be chosen automatically or specified
                    # explicitly.
                    "outlierPercentile": 3.14,  # The outlier percentile is used to ensure that outliers do not adversely
                    # affect the calculation of bucket sizes.  For example, setting an outlier
                    # percentile of 0.05 indicates that the top and bottom 5% of values when
                    # calculating buckets.  The values are still included in the chart, they will
                    # be added to the first or last buckets instead of their own buckets.
                    # Must be between 0.0 and 0.5.
                    "showItemDividers": True
                    or False,  # Whether horizontal divider lines should be displayed between items in each
                    # column.
                    "legendPosition": "A String",  # The position of the chart legend.
                    "series": [  # The series for a histogram may be either a single series of values to be
                        # bucketed or multiple series, each of the same length, containing the name
                        # of the series followed by the values to be bucketed for that series.
                        {  # A histogram series containing the series color and data.
                            "barColor": {  # Represents a color in the RGBA color space. This representation is designed # The color of the column representing this series in each bucket.
                                # This field is optional.
                                # for simplicity of conversion to/from color representations in various
                                # languages over compactness; for example, the fields of this representation
                                # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                # method in iOS; and, with just a little work, it can be easily formatted into
                                # a CSS "rgba()" string in JavaScript, as well.
                                #
                                # Note: this proto does not carry information about the absolute color space
                                # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                # space.
                                #
                                # Example (Java):
                                #
                                #      import com.google.type.Color;
                                #
                                #      // ...
                                #      public static java.awt.Color fromProto(Color protocolor) {
                                #        float alpha = protocolor.hasAlpha()
                                #            ? protocolor.getAlpha().getValue()
                                #            : 1.0;
                                #
                                #        return new java.awt.Color(
                                #            protocolor.getRed(),
                                #            protocolor.getGreen(),
                                #            protocolor.getBlue(),
                                #            alpha);
                                #      }
                                #
                                #      public static Color toProto(java.awt.Color color) {
                                #        float red = (float) color.getRed();
                                #        float green = (float) color.getGreen();
                                #        float blue = (float) color.getBlue();
                                #        float denominator = 255.0;
                                #        Color.Builder resultBuilder =
                                #            Color
                                #                .newBuilder()
                                #                .setRed(red / denominator)
                                #                .setGreen(green / denominator)
                                #                .setBlue(blue / denominator);
                                #        int alpha = color.getAlpha();
                                #        if (alpha != 255) {
                                #          result.setAlpha(
                                #              FloatValue
                                #                  .newBuilder()
                                #                  .setValue(((float) alpha) / denominator)
                                #                  .build());
                                #        }
                                #        return resultBuilder.build();
                                #      }
                                #      // ...
                                #
                                # Example (iOS / Obj-C):
                                #
                                #      // ...
                                #      static UIColor* fromProto(Color* protocolor) {
                                #         float red = [protocolor red];
                                #         float green = [protocolor green];
                                #         float blue = [protocolor blue];
                                #         FloatValue* alpha_wrapper = [protocolor alpha];
                                #         float alpha = 1.0;
                                #         if (alpha_wrapper != nil) {
                                #           alpha = [alpha_wrapper value];
                                #         }
                                #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                #      }
                                #
                                #      static Color* toProto(UIColor* color) {
                                #          CGFloat red, green, blue, alpha;
                                #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                #            return nil;
                                #          }
                                #          Color* result = [[Color alloc] init];
                                #          [result setRed:red];
                                #          [result setGreen:green];
                                #          [result setBlue:blue];
                                #          if (alpha <= 0.9999) {
                                #            [result setAlpha:floatWrapperWithValue(alpha)];
                                #          }
                                #          [result autorelease];
                                #          return result;
                                #     }
                                #     // ...
                                #
                                #  Example (JavaScript):
                                #
                                #     // ...
                                #
                                #     var protoToCssColor = function(rgb_color) {
                                #        var redFrac = rgb_color.red || 0.0;
                                #        var greenFrac = rgb_color.green || 0.0;
                                #        var blueFrac = rgb_color.blue || 0.0;
                                #        var red = Math.floor(redFrac * 255);
                                #        var green = Math.floor(greenFrac * 255);
                                #        var blue = Math.floor(blueFrac * 255);
                                #
                                #        if (!('alpha' in rgb_color)) {
                                #           return rgbToCssColor_(red, green, blue);
                                #        }
                                #
                                #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                #        var rgbParams = [red, green, blue].join(',');
                                #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                #     };
                                #
                                #     var rgbToCssColor_ = function(red, green, blue) {
                                #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                #       var hexString = rgbNumber.toString(16);
                                #       var missingZeros = 6 - hexString.length;
                                #       var resultBuilder = ['#'];
                                #       for (var i = 0; i < missingZeros; i++) {
                                #          resultBuilder.push('0');
                                #       }
                                #       resultBuilder.push(hexString);
                                #       return resultBuilder.join('');
                                #     };
                                #
                                #     // ...
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                # the final pixel color is defined by the equation:
                                #
                                #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                #
                                # This means that a value of 1.0 corresponds to a solid color, whereas
                                # a value of 0.0 corresponds to a completely transparent color. This
                                # uses a wrapper message rather than a simple float scalar so that it is
                                # possible to distinguish between a default value and the value being unset.
                                # If omitted, this color object is to be rendered as a solid color
                                # (as if the alpha value had been explicitly given with a value of 1.0).
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                            "barColorStyle": {  # A color value. # The color of the column representing this series in each bucket.
                                # This field is optional.
                                # If bar_color is also set, this field takes precedence.
                                "themeColor": "A String",  # Theme color.
                                "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed # RGB color.
                                    # for simplicity of conversion to/from color representations in various
                                    # languages over compactness; for example, the fields of this representation
                                    # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                    # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                    # method in iOS; and, with just a little work, it can be easily formatted into
                                    # a CSS "rgba()" string in JavaScript, as well.
                                    #
                                    # Note: this proto does not carry information about the absolute color space
                                    # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                    # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                    # space.
                                    #
                                    # Example (Java):
                                    #
                                    #      import com.google.type.Color;
                                    #
                                    #      // ...
                                    #      public static java.awt.Color fromProto(Color protocolor) {
                                    #        float alpha = protocolor.hasAlpha()
                                    #            ? protocolor.getAlpha().getValue()
                                    #            : 1.0;
                                    #
                                    #        return new java.awt.Color(
                                    #            protocolor.getRed(),
                                    #            protocolor.getGreen(),
                                    #            protocolor.getBlue(),
                                    #            alpha);
                                    #      }
                                    #
                                    #      public static Color toProto(java.awt.Color color) {
                                    #        float red = (float) color.getRed();
                                    #        float green = (float) color.getGreen();
                                    #        float blue = (float) color.getBlue();
                                    #        float denominator = 255.0;
                                    #        Color.Builder resultBuilder =
                                    #            Color
                                    #                .newBuilder()
                                    #                .setRed(red / denominator)
                                    #                .setGreen(green / denominator)
                                    #                .setBlue(blue / denominator);
                                    #        int alpha = color.getAlpha();
                                    #        if (alpha != 255) {
                                    #          result.setAlpha(
                                    #              FloatValue
                                    #                  .newBuilder()
                                    #                  .setValue(((float) alpha) / denominator)
                                    #                  .build());
                                    #        }
                                    #        return resultBuilder.build();
                                    #      }
                                    #      // ...
                                    #
                                    # Example (iOS / Obj-C):
                                    #
                                    #      // ...
                                    #      static UIColor* fromProto(Color* protocolor) {
                                    #         float red = [protocolor red];
                                    #         float green = [protocolor green];
                                    #         float blue = [protocolor blue];
                                    #         FloatValue* alpha_wrapper = [protocolor alpha];
                                    #         float alpha = 1.0;
                                    #         if (alpha_wrapper != nil) {
                                    #           alpha = [alpha_wrapper value];
                                    #         }
                                    #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                    #      }
                                    #
                                    #      static Color* toProto(UIColor* color) {
                                    #          CGFloat red, green, blue, alpha;
                                    #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                    #            return nil;
                                    #          }
                                    #          Color* result = [[Color alloc] init];
                                    #          [result setRed:red];
                                    #          [result setGreen:green];
                                    #          [result setBlue:blue];
                                    #          if (alpha <= 0.9999) {
                                    #            [result setAlpha:floatWrapperWithValue(alpha)];
                                    #          }
                                    #          [result autorelease];
                                    #          return result;
                                    #     }
                                    #     // ...
                                    #
                                    #  Example (JavaScript):
                                    #
                                    #     // ...
                                    #
                                    #     var protoToCssColor = function(rgb_color) {
                                    #        var redFrac = rgb_color.red || 0.0;
                                    #        var greenFrac = rgb_color.green || 0.0;
                                    #        var blueFrac = rgb_color.blue || 0.0;
                                    #        var red = Math.floor(redFrac * 255);
                                    #        var green = Math.floor(greenFrac * 255);
                                    #        var blue = Math.floor(blueFrac * 255);
                                    #
                                    #        if (!('alpha' in rgb_color)) {
                                    #           return rgbToCssColor_(red, green, blue);
                                    #        }
                                    #
                                    #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                    #        var rgbParams = [red, green, blue].join(',');
                                    #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                    #     };
                                    #
                                    #     var rgbToCssColor_ = function(red, green, blue) {
                                    #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                    #       var hexString = rgbNumber.toString(16);
                                    #       var missingZeros = 6 - hexString.length;
                                    #       var resultBuilder = ['#'];
                                    #       for (var i = 0; i < missingZeros; i++) {
                                    #          resultBuilder.push('0');
                                    #       }
                                    #       resultBuilder.push(hexString);
                                    #       return resultBuilder.join('');
                                    #     };
                                    #
                                    #     // ...
                                    "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                    "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                    # the final pixel color is defined by the equation:
                                    #
                                    #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                    #
                                    # This means that a value of 1.0 corresponds to a solid color, whereas
                                    # a value of 0.0 corresponds to a completely transparent color. This
                                    # uses a wrapper message rather than a simple float scalar so that it is
                                    # possible to distinguish between a default value and the value being unset.
                                    # If omitted, this color object is to be rendered as a solid color
                                    # (as if the alpha value had been explicitly given with a value of 1.0).
                                    "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                    "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                                },
                            },
                            "data": {  # The data included in a domain or series. # The data for this histogram series.
                                "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                                    "sources": [  # The ranges of data for a series or domain.
                                        # Exactly one dimension must have a length of 1,
                                        # and all sources in the list must have the same dimension
                                        # with length 1.
                                        # The domain (if it exists) & all series must have the same number
                                        # of source ranges. If using more than one source range, then the source
                                        # range at a given offset must be in order and contiguous across the domain
                                        # and series.
                                        #
                                        # For example, these are valid configurations:
                                        #
                                        #     domain sources: A1:A5
                                        #     series1 sources: B1:B5
                                        #     series2 sources: D6:D10
                                        #
                                        #     domain sources: A1:A5, C10:C12
                                        #     series1 sources: B1:B5, D10:D12
                                        #     series2 sources: C1:C5, E10:E12
                                        {  # A range on a sheet.
                                            # All indexes are zero-based.
                                            # Indexes are half open, e.g the start index is inclusive
                                            # and the end index is exclusive -- [start_index, end_index).
                                            # Missing indexes indicate the range is unbounded on that side.
                                            #
                                            # For example, if `"Sheet1"` is sheet ID 0, then:
                                            #
                                            #   `Sheet1!A1:A1 == sheet_id: 0,
                                            #                   start_row_index: 0, end_row_index: 1,
                                            #                   start_column_index: 0, end_column_index: 1`
                                            #
                                            #   `Sheet1!A3:B4 == sheet_id: 0,
                                            #                   start_row_index: 2, end_row_index: 4,
                                            #                   start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1!A:B == sheet_id: 0,
                                            #                 start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1!A5:B == sheet_id: 0,
                                            #                  start_row_index: 4,
                                            #                  start_column_index: 0, end_column_index: 2`
                                            #
                                            #   `Sheet1 == sheet_id:0`
                                            #
                                            # The start index must always be less than or equal to the end index.
                                            # If the start index equals the end index, then the range is empty.
                                            # Empty ranges are typically not meaningful and are usually rendered in the
                                            # UI as `#REF!`.
                                            "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                            "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                            "sheetId": 42,  # The sheet this range is on.
                                            "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                            "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                        },
                                    ],
                                },
                            },
                        },
                    ],
                    "bucketSize": 3.14,  # By default the bucket size (the range of values stacked in a single
                    # column) is chosen automatically, but it may be overridden here.
                    # E.g., A bucket size of 1.5 results in buckets from 0 - 1.5, 1.5 - 3.0, etc.
                    # Cannot be negative.
                    # This field is optional.
                },
                "bubbleChart": {  # A <a href="/chart/interactive/docs/gallery/bubblechart">bubble chart</a>. # A bubble chart specification.
                    "bubbleMinRadiusSize": 42,  # The minimum radius size of the bubbles, in pixels.
                    # If specific, the field must be a positive value.
                    "domain": {  # The data included in a domain or series. # The data containing the bubble x-values.  These values locate the bubbles
                        # in the chart horizontally.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "bubbleTextStyle": {  # The format of a run of text in a cell. # The format of the text inside the bubbles.
                        # Underline and Strikethrough are not supported.
                        # Absent values indicate that the field isn't specified.
                        "foregroundColor": {  # Represents a color in the RGBA color space. This representation is designed # The foreground color of the text.
                            # for simplicity of conversion to/from color representations in various
                            # languages over compactness; for example, the fields of this representation
                            # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                            # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                            # method in iOS; and, with just a little work, it can be easily formatted into
                            # a CSS "rgba()" string in JavaScript, as well.
                            #
                            # Note: this proto does not carry information about the absolute color space
                            # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                            # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                            # space.
                            #
                            # Example (Java):
                            #
                            #      import com.google.type.Color;
                            #
                            #      // ...
                            #      public static java.awt.Color fromProto(Color protocolor) {
                            #        float alpha = protocolor.hasAlpha()
                            #            ? protocolor.getAlpha().getValue()
                            #            : 1.0;
                            #
                            #        return new java.awt.Color(
                            #            protocolor.getRed(),
                            #            protocolor.getGreen(),
                            #            protocolor.getBlue(),
                            #            alpha);
                            #      }
                            #
                            #      public static Color toProto(java.awt.Color color) {
                            #        float red = (float) color.getRed();
                            #        float green = (float) color.getGreen();
                            #        float blue = (float) color.getBlue();
                            #        float denominator = 255.0;
                            #        Color.Builder resultBuilder =
                            #            Color
                            #                .newBuilder()
                            #                .setRed(red / denominator)
                            #                .setGreen(green / denominator)
                            #                .setBlue(blue / denominator);
                            #        int alpha = color.getAlpha();
                            #        if (alpha != 255) {
                            #          result.setAlpha(
                            #              FloatValue
                            #                  .newBuilder()
                            #                  .setValue(((float) alpha) / denominator)
                            #                  .build());
                            #        }
                            #        return resultBuilder.build();
                            #      }
                            #      // ...
                            #
                            # Example (iOS / Obj-C):
                            #
                            #      // ...
                            #      static UIColor* fromProto(Color* protocolor) {
                            #         float red = [protocolor red];
                            #         float green = [protocolor green];
                            #         float blue = [protocolor blue];
                            #         FloatValue* alpha_wrapper = [protocolor alpha];
                            #         float alpha = 1.0;
                            #         if (alpha_wrapper != nil) {
                            #           alpha = [alpha_wrapper value];
                            #         }
                            #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                            #      }
                            #
                            #      static Color* toProto(UIColor* color) {
                            #          CGFloat red, green, blue, alpha;
                            #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                            #            return nil;
                            #          }
                            #          Color* result = [[Color alloc] init];
                            #          [result setRed:red];
                            #          [result setGreen:green];
                            #          [result setBlue:blue];
                            #          if (alpha <= 0.9999) {
                            #            [result setAlpha:floatWrapperWithValue(alpha)];
                            #          }
                            #          [result autorelease];
                            #          return result;
                            #     }
                            #     // ...
                            #
                            #  Example (JavaScript):
                            #
                            #     // ...
                            #
                            #     var protoToCssColor = function(rgb_color) {
                            #        var redFrac = rgb_color.red || 0.0;
                            #        var greenFrac = rgb_color.green || 0.0;
                            #        var blueFrac = rgb_color.blue || 0.0;
                            #        var red = Math.floor(redFrac * 255);
                            #        var green = Math.floor(greenFrac * 255);
                            #        var blue = Math.floor(blueFrac * 255);
                            #
                            #        if (!('alpha' in rgb_color)) {
                            #           return rgbToCssColor_(red, green, blue);
                            #        }
                            #
                            #        var alphaFrac = rgb_color.alpha.value || 0.0;
                            #        var rgbParams = [red, green, blue].join(',');
                            #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                            #     };
                            #
                            #     var rgbToCssColor_ = function(red, green, blue) {
                            #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                            #       var hexString = rgbNumber.toString(16);
                            #       var missingZeros = 6 - hexString.length;
                            #       var resultBuilder = ['#'];
                            #       for (var i = 0; i < missingZeros; i++) {
                            #          resultBuilder.push('0');
                            #       }
                            #       resultBuilder.push(hexString);
                            #       return resultBuilder.join('');
                            #     };
                            #
                            #     // ...
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                            # the final pixel color is defined by the equation:
                            #
                            #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                            #
                            # This means that a value of 1.0 corresponds to a solid color, whereas
                            # a value of 0.0 corresponds to a completely transparent color. This
                            # uses a wrapper message rather than a simple float scalar so that it is
                            # possible to distinguish between a default value and the value being unset.
                            # If omitted, this color object is to be rendered as a solid color
                            # (as if the alpha value had been explicitly given with a value of 1.0).
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                        "bold": True or False,  # True if the text is bold.
                        "foregroundColorStyle": {  # A color value. # The foreground color of the text.
                            # If foreground_color is also set, this field takes precedence.
                            "themeColor": "A String",  # Theme color.
                            "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed # RGB color.
                                # for simplicity of conversion to/from color representations in various
                                # languages over compactness; for example, the fields of this representation
                                # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                                # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                                # method in iOS; and, with just a little work, it can be easily formatted into
                                # a CSS "rgba()" string in JavaScript, as well.
                                #
                                # Note: this proto does not carry information about the absolute color space
                                # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                                # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                                # space.
                                #
                                # Example (Java):
                                #
                                #      import com.google.type.Color;
                                #
                                #      // ...
                                #      public static java.awt.Color fromProto(Color protocolor) {
                                #        float alpha = protocolor.hasAlpha()
                                #            ? protocolor.getAlpha().getValue()
                                #            : 1.0;
                                #
                                #        return new java.awt.Color(
                                #            protocolor.getRed(),
                                #            protocolor.getGreen(),
                                #            protocolor.getBlue(),
                                #            alpha);
                                #      }
                                #
                                #      public static Color toProto(java.awt.Color color) {
                                #        float red = (float) color.getRed();
                                #        float green = (float) color.getGreen();
                                #        float blue = (float) color.getBlue();
                                #        float denominator = 255.0;
                                #        Color.Builder resultBuilder =
                                #            Color
                                #                .newBuilder()
                                #                .setRed(red / denominator)
                                #                .setGreen(green / denominator)
                                #                .setBlue(blue / denominator);
                                #        int alpha = color.getAlpha();
                                #        if (alpha != 255) {
                                #          result.setAlpha(
                                #              FloatValue
                                #                  .newBuilder()
                                #                  .setValue(((float) alpha) / denominator)
                                #                  .build());
                                #        }
                                #        return resultBuilder.build();
                                #      }
                                #      // ...
                                #
                                # Example (iOS / Obj-C):
                                #
                                #      // ...
                                #      static UIColor* fromProto(Color* protocolor) {
                                #         float red = [protocolor red];
                                #         float green = [protocolor green];
                                #         float blue = [protocolor blue];
                                #         FloatValue* alpha_wrapper = [protocolor alpha];
                                #         float alpha = 1.0;
                                #         if (alpha_wrapper != nil) {
                                #           alpha = [alpha_wrapper value];
                                #         }
                                #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                                #      }
                                #
                                #      static Color* toProto(UIColor* color) {
                                #          CGFloat red, green, blue, alpha;
                                #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                                #            return nil;
                                #          }
                                #          Color* result = [[Color alloc] init];
                                #          [result setRed:red];
                                #          [result setGreen:green];
                                #          [result setBlue:blue];
                                #          if (alpha <= 0.9999) {
                                #            [result setAlpha:floatWrapperWithValue(alpha)];
                                #          }
                                #          [result autorelease];
                                #          return result;
                                #     }
                                #     // ...
                                #
                                #  Example (JavaScript):
                                #
                                #     // ...
                                #
                                #     var protoToCssColor = function(rgb_color) {
                                #        var redFrac = rgb_color.red || 0.0;
                                #        var greenFrac = rgb_color.green || 0.0;
                                #        var blueFrac = rgb_color.blue || 0.0;
                                #        var red = Math.floor(redFrac * 255);
                                #        var green = Math.floor(greenFrac * 255);
                                #        var blue = Math.floor(blueFrac * 255);
                                #
                                #        if (!('alpha' in rgb_color)) {
                                #           return rgbToCssColor_(red, green, blue);
                                #        }
                                #
                                #        var alphaFrac = rgb_color.alpha.value || 0.0;
                                #        var rgbParams = [red, green, blue].join(',');
                                #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                                #     };
                                #
                                #     var rgbToCssColor_ = function(red, green, blue) {
                                #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                                #       var hexString = rgbNumber.toString(16);
                                #       var missingZeros = 6 - hexString.length;
                                #       var resultBuilder = ['#'];
                                #       for (var i = 0; i < missingZeros; i++) {
                                #          resultBuilder.push('0');
                                #       }
                                #       resultBuilder.push(hexString);
                                #       return resultBuilder.join('');
                                #     };
                                #
                                #     // ...
                                "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                                "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                                # the final pixel color is defined by the equation:
                                #
                                #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                                #
                                # This means that a value of 1.0 corresponds to a solid color, whereas
                                # a value of 0.0 corresponds to a completely transparent color. This
                                # uses a wrapper message rather than a simple float scalar so that it is
                                # possible to distinguish between a default value and the value being unset.
                                # If omitted, this color object is to be rendered as a solid color
                                # (as if the alpha value had been explicitly given with a value of 1.0).
                                "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                                "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                            },
                        },
                        "strikethrough": True
                        or False,  # True if the text has a strikethrough.
                        "fontFamily": "A String",  # The font family.
                        "fontSize": 42,  # The size of the font.
                        "italic": True or False,  # True if the text is italicized.
                        "underline": True or False,  # True if the text is underlined.
                    },
                    "series": {  # The data included in a domain or series. # The data contianing the bubble y-values.  These values locate the bubbles
                        # in the chart vertically.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "bubbleBorderColorStyle": {  # A color value. # The bubble border color.
                        # If bubble_border_color is also set, this field takes precedence.
                        "themeColor": "A String",  # Theme color.
                        "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed # RGB color.
                            # for simplicity of conversion to/from color representations in various
                            # languages over compactness; for example, the fields of this representation
                            # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                            # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                            # method in iOS; and, with just a little work, it can be easily formatted into
                            # a CSS "rgba()" string in JavaScript, as well.
                            #
                            # Note: this proto does not carry information about the absolute color space
                            # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                            # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                            # space.
                            #
                            # Example (Java):
                            #
                            #      import com.google.type.Color;
                            #
                            #      // ...
                            #      public static java.awt.Color fromProto(Color protocolor) {
                            #        float alpha = protocolor.hasAlpha()
                            #            ? protocolor.getAlpha().getValue()
                            #            : 1.0;
                            #
                            #        return new java.awt.Color(
                            #            protocolor.getRed(),
                            #            protocolor.getGreen(),
                            #            protocolor.getBlue(),
                            #            alpha);
                            #      }
                            #
                            #      public static Color toProto(java.awt.Color color) {
                            #        float red = (float) color.getRed();
                            #        float green = (float) color.getGreen();
                            #        float blue = (float) color.getBlue();
                            #        float denominator = 255.0;
                            #        Color.Builder resultBuilder =
                            #            Color
                            #                .newBuilder()
                            #                .setRed(red / denominator)
                            #                .setGreen(green / denominator)
                            #                .setBlue(blue / denominator);
                            #        int alpha = color.getAlpha();
                            #        if (alpha != 255) {
                            #          result.setAlpha(
                            #              FloatValue
                            #                  .newBuilder()
                            #                  .setValue(((float) alpha) / denominator)
                            #                  .build());
                            #        }
                            #        return resultBuilder.build();
                            #      }
                            #      // ...
                            #
                            # Example (iOS / Obj-C):
                            #
                            #      // ...
                            #      static UIColor* fromProto(Color* protocolor) {
                            #         float red = [protocolor red];
                            #         float green = [protocolor green];
                            #         float blue = [protocolor blue];
                            #         FloatValue* alpha_wrapper = [protocolor alpha];
                            #         float alpha = 1.0;
                            #         if (alpha_wrapper != nil) {
                            #           alpha = [alpha_wrapper value];
                            #         }
                            #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                            #      }
                            #
                            #      static Color* toProto(UIColor* color) {
                            #          CGFloat red, green, blue, alpha;
                            #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                            #            return nil;
                            #          }
                            #          Color* result = [[Color alloc] init];
                            #          [result setRed:red];
                            #          [result setGreen:green];
                            #          [result setBlue:blue];
                            #          if (alpha <= 0.9999) {
                            #            [result setAlpha:floatWrapperWithValue(alpha)];
                            #          }
                            #          [result autorelease];
                            #          return result;
                            #     }
                            #     // ...
                            #
                            #  Example (JavaScript):
                            #
                            #     // ...
                            #
                            #     var protoToCssColor = function(rgb_color) {
                            #        var redFrac = rgb_color.red || 0.0;
                            #        var greenFrac = rgb_color.green || 0.0;
                            #        var blueFrac = rgb_color.blue || 0.0;
                            #        var red = Math.floor(redFrac * 255);
                            #        var green = Math.floor(greenFrac * 255);
                            #        var blue = Math.floor(blueFrac * 255);
                            #
                            #        if (!('alpha' in rgb_color)) {
                            #           return rgbToCssColor_(red, green, blue);
                            #        }
                            #
                            #        var alphaFrac = rgb_color.alpha.value || 0.0;
                            #        var rgbParams = [red, green, blue].join(',');
                            #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                            #     };
                            #
                            #     var rgbToCssColor_ = function(red, green, blue) {
                            #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                            #       var hexString = rgbNumber.toString(16);
                            #       var missingZeros = 6 - hexString.length;
                            #       var resultBuilder = ['#'];
                            #       for (var i = 0; i < missingZeros; i++) {
                            #          resultBuilder.push('0');
                            #       }
                            #       resultBuilder.push(hexString);
                            #       return resultBuilder.join('');
                            #     };
                            #
                            #     // ...
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                            # the final pixel color is defined by the equation:
                            #
                            #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                            #
                            # This means that a value of 1.0 corresponds to a solid color, whereas
                            # a value of 0.0 corresponds to a completely transparent color. This
                            # uses a wrapper message rather than a simple float scalar so that it is
                            # possible to distinguish between a default value and the value being unset.
                            # If omitted, this color object is to be rendered as a solid color
                            # (as if the alpha value had been explicitly given with a value of 1.0).
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                    },
                    "legendPosition": "A String",  # Where the legend of the chart should be drawn.
                    "bubbleMaxRadiusSize": 42,  # The max radius size of the bubbles, in pixels.
                    # If specified, the field must be a positive value.
                    "bubbleOpacity": 3.14,  # The opacity of the bubbles between 0 and 1.0.
                    # 0 is fully transparent and 1 is fully opaque.
                    "groupIds": {  # The data included in a domain or series. # The data containing the bubble group IDs. All bubbles with the same group
                        # ID are drawn in the same color. If bubble_sizes is specified then
                        # this field must also be specified but may contain blank values.
                        # This field is optional.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "bubbleSizes": {  # The data included in a domain or series. # The data contianing the bubble sizes.  Bubble sizes are used to draw
                        # the bubbles at different sizes relative to each other.
                        # If specified, group_ids must also be specified.  This field is
                        # optional.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "bubbleBorderColor": {  # Represents a color in the RGBA color space. This representation is designed # The bubble border color.
                        # for simplicity of conversion to/from color representations in various
                        # languages over compactness; for example, the fields of this representation
                        # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                        # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                        # method in iOS; and, with just a little work, it can be easily formatted into
                        # a CSS "rgba()" string in JavaScript, as well.
                        #
                        # Note: this proto does not carry information about the absolute color space
                        # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                        # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                        # space.
                        #
                        # Example (Java):
                        #
                        #      import com.google.type.Color;
                        #
                        #      // ...
                        #      public static java.awt.Color fromProto(Color protocolor) {
                        #        float alpha = protocolor.hasAlpha()
                        #            ? protocolor.getAlpha().getValue()
                        #            : 1.0;
                        #
                        #        return new java.awt.Color(
                        #            protocolor.getRed(),
                        #            protocolor.getGreen(),
                        #            protocolor.getBlue(),
                        #            alpha);
                        #      }
                        #
                        #      public static Color toProto(java.awt.Color color) {
                        #        float red = (float) color.getRed();
                        #        float green = (float) color.getGreen();
                        #        float blue = (float) color.getBlue();
                        #        float denominator = 255.0;
                        #        Color.Builder resultBuilder =
                        #            Color
                        #                .newBuilder()
                        #                .setRed(red / denominator)
                        #                .setGreen(green / denominator)
                        #                .setBlue(blue / denominator);
                        #        int alpha = color.getAlpha();
                        #        if (alpha != 255) {
                        #          result.setAlpha(
                        #              FloatValue
                        #                  .newBuilder()
                        #                  .setValue(((float) alpha) / denominator)
                        #                  .build());
                        #        }
                        #        return resultBuilder.build();
                        #      }
                        #      // ...
                        #
                        # Example (iOS / Obj-C):
                        #
                        #      // ...
                        #      static UIColor* fromProto(Color* protocolor) {
                        #         float red = [protocolor red];
                        #         float green = [protocolor green];
                        #         float blue = [protocolor blue];
                        #         FloatValue* alpha_wrapper = [protocolor alpha];
                        #         float alpha = 1.0;
                        #         if (alpha_wrapper != nil) {
                        #           alpha = [alpha_wrapper value];
                        #         }
                        #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                        #      }
                        #
                        #      static Color* toProto(UIColor* color) {
                        #          CGFloat red, green, blue, alpha;
                        #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                        #            return nil;
                        #          }
                        #          Color* result = [[Color alloc] init];
                        #          [result setRed:red];
                        #          [result setGreen:green];
                        #          [result setBlue:blue];
                        #          if (alpha <= 0.9999) {
                        #            [result setAlpha:floatWrapperWithValue(alpha)];
                        #          }
                        #          [result autorelease];
                        #          return result;
                        #     }
                        #     // ...
                        #
                        #  Example (JavaScript):
                        #
                        #     // ...
                        #
                        #     var protoToCssColor = function(rgb_color) {
                        #        var redFrac = rgb_color.red || 0.0;
                        #        var greenFrac = rgb_color.green || 0.0;
                        #        var blueFrac = rgb_color.blue || 0.0;
                        #        var red = Math.floor(redFrac * 255);
                        #        var green = Math.floor(greenFrac * 255);
                        #        var blue = Math.floor(blueFrac * 255);
                        #
                        #        if (!('alpha' in rgb_color)) {
                        #           return rgbToCssColor_(red, green, blue);
                        #        }
                        #
                        #        var alphaFrac = rgb_color.alpha.value || 0.0;
                        #        var rgbParams = [red, green, blue].join(',');
                        #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                        #     };
                        #
                        #     var rgbToCssColor_ = function(red, green, blue) {
                        #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                        #       var hexString = rgbNumber.toString(16);
                        #       var missingZeros = 6 - hexString.length;
                        #       var resultBuilder = ['#'];
                        #       for (var i = 0; i < missingZeros; i++) {
                        #          resultBuilder.push('0');
                        #       }
                        #       resultBuilder.push(hexString);
                        #       return resultBuilder.join('');
                        #     };
                        #
                        #     // ...
                        "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                        "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                        # the final pixel color is defined by the equation:
                        #
                        #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                        #
                        # This means that a value of 1.0 corresponds to a solid color, whereas
                        # a value of 0.0 corresponds to a completely transparent color. This
                        # uses a wrapper message rather than a simple float scalar so that it is
                        # possible to distinguish between a default value and the value being unset.
                        # If omitted, this color object is to be rendered as a solid color
                        # (as if the alpha value had been explicitly given with a value of 1.0).
                        "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                        "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                    },
                    "bubbleLabels": {  # The data included in a domain or series. # The data containing the bubble labels.  These do not need to be unique.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                },
                "orgChart": {  # An <a href="/chart/interactive/docs/gallery/orgchart">org chart</a>. # An org chart specification.
                    # Org charts require a unique set of labels in labels and may
                    # optionally include parent_labels and tooltips.
                    # parent_labels contain, for each node, the label identifying the parent
                    # node.  tooltips contain, for each node, an optional tooltip.
                    #
                    # For example, to describe an OrgChart with Alice as the CEO, Bob as the
                    # President (reporting to Alice) and Cathy as VP of Sales (also reporting to
                    # Alice), have labels contain "Alice", "Bob", "Cathy",
                    # parent_labels contain "", "Alice", "Alice" and tooltips contain
                    # "CEO", "President", "VP Sales".
                    "tooltips": {  # The data included in a domain or series. # The data containing the tooltip for the corresponding node.  A blank value
                        # results in no tooltip being displayed for the node.
                        # This field is optional.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "parentLabels": {  # The data included in a domain or series. # The data containing the label of the parent for the corresponding node.
                        # A blank value indicates that the node has no parent and is a top-level
                        # node.
                        # This field is optional.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "nodeColor": {  # Represents a color in the RGBA color space. This representation is designed # The color of the org chart nodes.
                        # for simplicity of conversion to/from color representations in various
                        # languages over compactness; for example, the fields of this representation
                        # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                        # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                        # method in iOS; and, with just a little work, it can be easily formatted into
                        # a CSS "rgba()" string in JavaScript, as well.
                        #
                        # Note: this proto does not carry information about the absolute color space
                        # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                        # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                        # space.
                        #
                        # Example (Java):
                        #
                        #      import com.google.type.Color;
                        #
                        #      // ...
                        #      public static java.awt.Color fromProto(Color protocolor) {
                        #        float alpha = protocolor.hasAlpha()
                        #            ? protocolor.getAlpha().getValue()
                        #            : 1.0;
                        #
                        #        return new java.awt.Color(
                        #            protocolor.getRed(),
                        #            protocolor.getGreen(),
                        #            protocolor.getBlue(),
                        #            alpha);
                        #      }
                        #
                        #      public static Color toProto(java.awt.Color color) {
                        #        float red = (float) color.getRed();
                        #        float green = (float) color.getGreen();
                        #        float blue = (float) color.getBlue();
                        #        float denominator = 255.0;
                        #        Color.Builder resultBuilder =
                        #            Color
                        #                .newBuilder()
                        #                .setRed(red / denominator)
                        #                .setGreen(green / denominator)
                        #                .setBlue(blue / denominator);
                        #        int alpha = color.getAlpha();
                        #        if (alpha != 255) {
                        #          result.setAlpha(
                        #              FloatValue
                        #                  .newBuilder()
                        #                  .setValue(((float) alpha) / denominator)
                        #                  .build());
                        #        }
                        #        return resultBuilder.build();
                        #      }
                        #      // ...
                        #
                        # Example (iOS / Obj-C):
                        #
                        #      // ...
                        #      static UIColor* fromProto(Color* protocolor) {
                        #         float red = [protocolor red];
                        #         float green = [protocolor green];
                        #         float blue = [protocolor blue];
                        #         FloatValue* alpha_wrapper = [protocolor alpha];
                        #         float alpha = 1.0;
                        #         if (alpha_wrapper != nil) {
                        #           alpha = [alpha_wrapper value];
                        #         }
                        #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                        #      }
                        #
                        #      static Color* toProto(UIColor* color) {
                        #          CGFloat red, green, blue, alpha;
                        #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                        #            return nil;
                        #          }
                        #          Color* result = [[Color alloc] init];
                        #          [result setRed:red];
                        #          [result setGreen:green];
                        #          [result setBlue:blue];
                        #          if (alpha <= 0.9999) {
                        #            [result setAlpha:floatWrapperWithValue(alpha)];
                        #          }
                        #          [result autorelease];
                        #          return result;
                        #     }
                        #     // ...
                        #
                        #  Example (JavaScript):
                        #
                        #     // ...
                        #
                        #     var protoToCssColor = function(rgb_color) {
                        #        var redFrac = rgb_color.red || 0.0;
                        #        var greenFrac = rgb_color.green || 0.0;
                        #        var blueFrac = rgb_color.blue || 0.0;
                        #        var red = Math.floor(redFrac * 255);
                        #        var green = Math.floor(greenFrac * 255);
                        #        var blue = Math.floor(blueFrac * 255);
                        #
                        #        if (!('alpha' in rgb_color)) {
                        #           return rgbToCssColor_(red, green, blue);
                        #        }
                        #
                        #        var alphaFrac = rgb_color.alpha.value || 0.0;
                        #        var rgbParams = [red, green, blue].join(',');
                        #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                        #     };
                        #
                        #     var rgbToCssColor_ = function(red, green, blue) {
                        #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                        #       var hexString = rgbNumber.toString(16);
                        #       var missingZeros = 6 - hexString.length;
                        #       var resultBuilder = ['#'];
                        #       for (var i = 0; i < missingZeros; i++) {
                        #          resultBuilder.push('0');
                        #       }
                        #       resultBuilder.push(hexString);
                        #       return resultBuilder.join('');
                        #     };
                        #
                        #     // ...
                        "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                        "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                        # the final pixel color is defined by the equation:
                        #
                        #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                        #
                        # This means that a value of 1.0 corresponds to a solid color, whereas
                        # a value of 0.0 corresponds to a completely transparent color. This
                        # uses a wrapper message rather than a simple float scalar so that it is
                        # possible to distinguish between a default value and the value being unset.
                        # If omitted, this color object is to be rendered as a solid color
                        # (as if the alpha value had been explicitly given with a value of 1.0).
                        "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                        "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                    },
                    "labels": {  # The data included in a domain or series. # The data containing the labels for all the nodes in the chart.  Labels
                        # must be unique.
                        "sourceRange": {  # Source ranges for a chart. # The source ranges of the data.
                            "sources": [  # The ranges of data for a series or domain.
                                # Exactly one dimension must have a length of 1,
                                # and all sources in the list must have the same dimension
                                # with length 1.
                                # The domain (if it exists) & all series must have the same number
                                # of source ranges. If using more than one source range, then the source
                                # range at a given offset must be in order and contiguous across the domain
                                # and series.
                                #
                                # For example, these are valid configurations:
                                #
                                #     domain sources: A1:A5
                                #     series1 sources: B1:B5
                                #     series2 sources: D6:D10
                                #
                                #     domain sources: A1:A5, C10:C12
                                #     series1 sources: B1:B5, D10:D12
                                #     series2 sources: C1:C5, E10:E12
                                {  # A range on a sheet.
                                    # All indexes are zero-based.
                                    # Indexes are half open, e.g the start index is inclusive
                                    # and the end index is exclusive -- [start_index, end_index).
                                    # Missing indexes indicate the range is unbounded on that side.
                                    #
                                    # For example, if `"Sheet1"` is sheet ID 0, then:
                                    #
                                    #   `Sheet1!A1:A1 == sheet_id: 0,
                                    #                   start_row_index: 0, end_row_index: 1,
                                    #                   start_column_index: 0, end_column_index: 1`
                                    #
                                    #   `Sheet1!A3:B4 == sheet_id: 0,
                                    #                   start_row_index: 2, end_row_index: 4,
                                    #                   start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A:B == sheet_id: 0,
                                    #                 start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1!A5:B == sheet_id: 0,
                                    #                  start_row_index: 4,
                                    #                  start_column_index: 0, end_column_index: 2`
                                    #
                                    #   `Sheet1 == sheet_id:0`
                                    #
                                    # The start index must always be less than or equal to the end index.
                                    # If the start index equals the end index, then the range is empty.
                                    # Empty ranges are typically not meaningful and are usually rendered in the
                                    # UI as `#REF!`.
                                    "endRowIndex": 42,  # The end row (exclusive) of the range, or not set if unbounded.
                                    "endColumnIndex": 42,  # The end column (exclusive) of the range, or not set if unbounded.
                                    "sheetId": 42,  # The sheet this range is on.
                                    "startColumnIndex": 42,  # The start column (inclusive) of the range, or not set if unbounded.
                                    "startRowIndex": 42,  # The start row (inclusive) of the range, or not set if unbounded.
                                },
                            ],
                        },
                    },
                    "selectedNodeColor": {  # Represents a color in the RGBA color space. This representation is designed # The color of the selected org chart nodes.
                        # for simplicity of conversion to/from color representations in various
                        # languages over compactness; for example, the fields of this representation
                        # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                        # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                        # method in iOS; and, with just a little work, it can be easily formatted into
                        # a CSS "rgba()" string in JavaScript, as well.
                        #
                        # Note: this proto does not carry information about the absolute color space
                        # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                        # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                        # space.
                        #
                        # Example (Java):
                        #
                        #      import com.google.type.Color;
                        #
                        #      // ...
                        #      public static java.awt.Color fromProto(Color protocolor) {
                        #        float alpha = protocolor.hasAlpha()
                        #            ? protocolor.getAlpha().getValue()
                        #            : 1.0;
                        #
                        #        return new java.awt.Color(
                        #            protocolor.getRed(),
                        #            protocolor.getGreen(),
                        #            protocolor.getBlue(),
                        #            alpha);
                        #      }
                        #
                        #      public static Color toProto(java.awt.Color color) {
                        #        float red = (float) color.getRed();
                        #        float green = (float) color.getGreen();
                        #        float blue = (float) color.getBlue();
                        #        float denominator = 255.0;
                        #        Color.Builder resultBuilder =
                        #            Color
                        #                .newBuilder()
                        #                .setRed(red / denominator)
                        #                .setGreen(green / denominator)
                        #                .setBlue(blue / denominator);
                        #        int alpha = color.getAlpha();
                        #        if (alpha != 255) {
                        #          result.setAlpha(
                        #              FloatValue
                        #                  .newBuilder()
                        #                  .setValue(((float) alpha) / denominator)
                        #                  .build());
                        #        }
                        #        return resultBuilder.build();
                        #      }
                        #      // ...
                        #
                        # Example (iOS / Obj-C):
                        #
                        #      // ...
                        #      static UIColor* fromProto(Color* protocolor) {
                        #         float red = [protocolor red];
                        #         float green = [protocolor green];
                        #         float blue = [protocolor blue];
                        #         FloatValue* alpha_wrapper = [protocolor alpha];
                        #         float alpha = 1.0;
                        #         if (alpha_wrapper != nil) {
                        #           alpha = [alpha_wrapper value];
                        #         }
                        #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                        #      }
                        #
                        #      static Color* toProto(UIColor* color) {
                        #          CGFloat red, green, blue, alpha;
                        #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                        #            return nil;
                        #          }
                        #          Color* result = [[Color alloc] init];
                        #          [result setRed:red];
                        #          [result setGreen:green];
                        #          [result setBlue:blue];
                        #          if (alpha <= 0.9999) {
                        #            [result setAlpha:floatWrapperWithValue(alpha)];
                        #          }
                        #          [result autorelease];
                        #          return result;
                        #     }
                        #     // ...
                        #
                        #  Example (JavaScript):
                        #
                        #     // ...
                        #
                        #     var protoToCssColor = function(rgb_color) {
                        #        var redFrac = rgb_color.red || 0.0;
                        #        var greenFrac = rgb_color.green || 0.0;
                        #        var blueFrac = rgb_color.blue || 0.0;
                        #        var red = Math.floor(redFrac * 255);
                        #        var green = Math.floor(greenFrac * 255);
                        #        var blue = Math.floor(blueFrac * 255);
                        #
                        #        if (!('alpha' in rgb_color)) {
                        #           return rgbToCssColor_(red, green, blue);
                        #        }
                        #
                        #        var alphaFrac = rgb_color.alpha.value || 0.0;
                        #        var rgbParams = [red, green, blue].join(',');
                        #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                        #     };
                        #
                        #     var rgbToCssColor_ = function(red, green, blue) {
                        #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                        #       var hexString = rgbNumber.toString(16);
                        #       var missingZeros = 6 - hexString.length;
                        #       var resultBuilder = ['#'];
                        #       for (var i = 0; i < missingZeros; i++) {
                        #          resultBuilder.push('0');
                        #       }
                        #       resultBuilder.push(hexString);
                        #       return resultBuilder.join('');
                        #     };
                        #
                        #     // ...
                        "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                        "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                        # the final pixel color is defined by the equation:
                        #
                        #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                        #
                        # This means that a value of 1.0 corresponds to a solid color, whereas
                        # a value of 0.0 corresponds to a completely transparent color. This
                        # uses a wrapper message rather than a simple float scalar so that it is
                        # possible to distinguish between a default value and the value being unset.
                        # If omitted, this color object is to be rendered as a solid color
                        # (as if the alpha value had been explicitly given with a value of 1.0).
                        "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                        "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                    },
                    "nodeColorStyle": {  # A color value. # The color of the org chart nodes.
                        # If node_color is also set, this field takes precedence.
                        "themeColor": "A String",  # Theme color.
                        "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed # RGB color.
                            # for simplicity of conversion to/from color representations in various
                            # languages over compactness; for example, the fields of this representation
                            # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                            # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                            # method in iOS; and, with just a little work, it can be easily formatted into
                            # a CSS "rgba()" string in JavaScript, as well.
                            #
                            # Note: this proto does not carry information about the absolute color space
                            # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                            # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                            # space.
                            #
                            # Example (Java):
                            #
                            #      import com.google.type.Color;
                            #
                            #      // ...
                            #      public static java.awt.Color fromProto(Color protocolor) {
                            #        float alpha = protocolor.hasAlpha()
                            #            ? protocolor.getAlpha().getValue()
                            #            : 1.0;
                            #
                            #        return new java.awt.Color(
                            #            protocolor.getRed(),
                            #            protocolor.getGreen(),
                            #            protocolor.getBlue(),
                            #            alpha);
                            #      }
                            #
                            #      public static Color toProto(java.awt.Color color) {
                            #        float red = (float) color.getRed();
                            #        float green = (float) color.getGreen();
                            #        float blue = (float) color.getBlue();
                            #        float denominator = 255.0;
                            #        Color.Builder resultBuilder =
                            #            Color
                            #                .newBuilder()
                            #                .setRed(red / denominator)
                            #                .setGreen(green / denominator)
                            #                .setBlue(blue / denominator);
                            #        int alpha = color.getAlpha();
                            #        if (alpha != 255) {
                            #          result.setAlpha(
                            #              FloatValue
                            #                  .newBuilder()
                            #                  .setValue(((float) alpha) / denominator)
                            #                  .build());
                            #        }
                            #        return resultBuilder.build();
                            #      }
                            #      // ...
                            #
                            # Example (iOS / Obj-C):
                            #
                            #      // ...
                            #      static UIColor* fromProto(Color* protocolor) {
                            #         float red = [protocolor red];
                            #         float green = [protocolor green];
                            #         float blue = [protocolor blue];
                            #         FloatValue* alpha_wrapper = [protocolor alpha];
                            #         float alpha = 1.0;
                            #         if (alpha_wrapper != nil) {
                            #           alpha = [alpha_wrapper value];
                            #         }
                            #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                            #      }
                            #
                            #      static Color* toProto(UIColor* color) {
                            #          CGFloat red, green, blue, alpha;
                            #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                            #            return nil;
                            #          }
                            #          Color* result = [[Color alloc] init];
                            #          [result setRed:red];
                            #          [result setGreen:green];
                            #          [result setBlue:blue];
                            #          if (alpha <= 0.9999) {
                            #            [result setAlpha:floatWrapperWithValue(alpha)];
                            #          }
                            #          [result autorelease];
                            #          return result;
                            #     }
                            #     // ...
                            #
                            #  Example (JavaScript):
                            #
                            #     // ...
                            #
                            #     var protoToCssColor = function(rgb_color) {
                            #        var redFrac = rgb_color.red || 0.0;
                            #        var greenFrac = rgb_color.green || 0.0;
                            #        var blueFrac = rgb_color.blue || 0.0;
                            #        var red = Math.floor(redFrac * 255);
                            #        var green = Math.floor(greenFrac * 255);
                            #        var blue = Math.floor(blueFrac * 255);
                            #
                            #        if (!('alpha' in rgb_color)) {
                            #           return rgbToCssColor_(red, green, blue);
                            #        }
                            #
                            #        var alphaFrac = rgb_color.alpha.value || 0.0;
                            #        var rgbParams = [red, green, blue].join(',');
                            #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                            #     };
                            #
                            #     var rgbToCssColor_ = function(red, green, blue) {
                            #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                            #       var hexString = rgbNumber.toString(16);
                            #       var missingZeros = 6 - hexString.length;
                            #       var resultBuilder = ['#'];
                            #       for (var i = 0; i < missingZeros; i++) {
                            #          resultBuilder.push('0');
                            #       }
                            #       resultBuilder.push(hexString);
                            #       return resultBuilder.join('');
                            #     };
                            #
                            #     // ...
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                            # the final pixel color is defined by the equation:
                            #
                            #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                            #
                            # This means that a value of 1.0 corresponds to a solid color, whereas
                            # a value of 0.0 corresponds to a completely transparent color. This
                            # uses a wrapper message rather than a simple float scalar so that it is
                            # possible to distinguish between a default value and the value being unset.
                            # If omitted, this color object is to be rendered as a solid color
                            # (as if the alpha value had been explicitly given with a value of 1.0).
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                    },
                    "selectedNodeColorStyle": {  # A color value. # The color of the selected org chart nodes.
                        # If selected_node_color is also set, this field takes precedence.
                        "themeColor": "A String",  # Theme color.
                        "rgbColor": {  # Represents a color in the RGBA color space. This representation is designed # RGB color.
                            # for simplicity of conversion to/from color representations in various
                            # languages over compactness; for example, the fields of this representation
                            # can be trivially provided to the constructor of "java.awt.Color" in Java; it
                            # can also be trivially provided to UIColor's "+colorWithRed:green:blue:alpha"
                            # method in iOS; and, with just a little work, it can be easily formatted into
                            # a CSS "rgba()" string in JavaScript, as well.
                            #
                            # Note: this proto does not carry information about the absolute color space
                            # that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                            # DCI-P3, BT.2020, etc.). By default, applications SHOULD assume the sRGB color
                            # space.
                            #
                            # Example (Java):
                            #
                            #      import com.google.type.Color;
                            #
                            #      // ...
                            #      public static java.awt.Color fromProto(Color protocolor) {
                            #        float alpha = protocolor.hasAlpha()
                            #            ? protocolor.getAlpha().getValue()
                            #            : 1.0;
                            #
                            #        return new java.awt.Color(
                            #            protocolor.getRed(),
                            #            protocolor.getGreen(),
                            #            protocolor.getBlue(),
                            #            alpha);
                            #      }
                            #
                            #      public static Color toProto(java.awt.Color color) {
                            #        float red = (float) color.getRed();
                            #        float green = (float) color.getGreen();
                            #        float blue = (float) color.getBlue();
                            #        float denominator = 255.0;
                            #        Color.Builder resultBuilder =
                            #            Color
                            #                .newBuilder()
                            #                .setRed(red / denominator)
                            #                .setGreen(green / denominator)
                            #                .setBlue(blue / denominator);
                            #        int alpha = color.getAlpha();
                            #        if (alpha != 255) {
                            #          result.setAlpha(
                            #              FloatValue
                            #                  .newBuilder()
                            #                  .setValue(((float) alpha) / denominator)
                            #                  .build());
                            #        }
                            #        return resultBuilder.build();
                            #      }
                            #      // ...
                            #
                            # Example (iOS / Obj-C):
                            #
                            #      // ...
                            #      static UIColor* fromProto(Color* protocolor) {
                            #         float red = [protocolor red];
                            #         float green = [protocolor green];
                            #         float blue = [protocolor blue];
                            #         FloatValue* alpha_wrapper = [protocolor alpha];
                            #         float alpha = 1.0;
                            #         if (alpha_wrapper != nil) {
                            #           alpha = [alpha_wrapper value];
                            #         }
                            #         return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
                            #      }
                            #
                            #      static Color* toProto(UIColor* color) {
                            #          CGFloat red, green, blue, alpha;
                            #          if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                            #            return nil;
                            #          }
                            #          Color* result = [[Color alloc] init];
                            #          [result setRed:red];
                            #          [result setGreen:green];
                            #          [result setBlue:blue];
                            #          if (alpha <= 0.9999) {
                            #            [result setAlpha:floatWrapperWithValue(alpha)];
                            #          }
                            #          [result autorelease];
                            #          return result;
                            #     }
                            #     // ...
                            #
                            #  Example (JavaScript):
                            #
                            #     // ...
                            #
                            #     var protoToCssColor = function(rgb_color) {
                            #        var redFrac = rgb_color.red || 0.0;
                            #        var greenFrac = rgb_color.green || 0.0;
                            #        var blueFrac = rgb_color.blue || 0.0;
                            #        var red = Math.floor(redFrac * 255);
                            #        var green = Math.floor(greenFrac * 255);
                            #        var blue = Math.floor(blueFrac * 255);
                            #
                            #        if (!('alpha' in rgb_color)) {
                            #           return rgbToCssColor_(red, green, blue);
                            #        }
                            #
                            #        var alphaFrac = rgb_color.alpha.value || 0.0;
                            #        var rgbParams = [red, green, blue].join(',');
                            #        return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
                            #     };
                            #
                            #     var rgbToCssColor_ = function(red, green, blue) {
                            #       var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                            #       var hexString = rgbNumber.toString(16);
                            #       var missingZeros = 6 - hexString.length;
                            #       var resultBuilder = ['#'];
                            #       for (var i = 0; i < missingZeros; i++) {
                            #          resultBuilder.push('0');
                            #       }
                            #       resultBuilder.push(hexString);
                            #       return resultBuilder.join('');
                            #     };
                            #
                            #     // ...
                            "blue": 3.14,  # The amount of blue in the color as a value in the interval [0, 1].
                            "alpha": 3.14,  # The fraction of this color that should be applied to the pixel. That is,
                            # the final pixel color is defined by the equation:
                            #
                            #   pixel color = alpha * (this color) + (1.0 - alpha) * (background color)
                            #
                            # This means that a value of 1.0 corresponds to a solid color, whereas
                            # a value of 0.0 corresponds to a completely transparent color. This
                            # uses a wrapper message rather than a simple float scalar so that it is
                            # possible to distinguish between a default value and the value being unset.
                            # If omitted, this color object is to be rendered as a solid color
                            # (as if the alpha value had been explicitly given with a value of 1.0).
                            "green": 3.14,  # The amount of green in the color as a value in the interval [0, 1].
                            "red": 3.14,  # The amount of red in the color as a value in the interval [0, 1].
                        },
                    },
                    "nodeSize": "A String",  # The size of the org chart nodes.
                },
            },
        },
    }
}
