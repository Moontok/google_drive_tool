# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python library for programmatically interacting with Google Sheets via the Google Sheets API v4. Provides high-level abstractions for cell operations, formatting, sheet management, and chart creation using a service account authentication model.

## Setup

```bash
pip install -r requirements.txt
pip install -e .
```

Two files are required in a `secrets/` directory (gitignored):
- `secrets/google_info.json` — Google service account credentials JSON (downloaded from Google Cloud Console)
- `secrets/info.json` — App config: `{"sheet_id": "<spreadsheet_id>"}`

## Running

There are no tests or linting tools configured. The `dev_spot.py` script serves as the primary demo/manual-testing file:

```bash
python dev_spot.py
```

## Architecture: Request Pooling Pattern

The central design is a **two-pool batch system** in `SheetTool` (`sheets.py`). Most methods do **not** execute immediately — they append to one of two internal lists:

- `__requests` — structural/formatting changes (sheet operations, cell formatting, merges, etc.)
- `__update_values_requests` — cell value changes (insert, clear, etc.)

Nothing is sent to the API until the user explicitly calls:
- `batch_update()` — flushes `__requests` and clears the pool
- `batch_update_values()` — flushes `__update_values_requests` and clears the pool

A few methods are **not batched** and execute immediately (noted in their docstrings): `setup()`, `create_spreadsheet()`, `set_spreadsheet()`, `get_spreadsheet_properties()`, `get_values()`, `append_values()`.

## Component Relationships

- **`sheets.py` / `SheetTool`** — the main entry point. Handles authentication, holds the two request pools, and exposes all sheet/cell/formatting/chart operations.
- **`chart.py`** — chart specification builders. Chart objects are constructed and configured, then passed to `SheetTool` which converts them to API requests. Hierarchy: `Chart` → `BasicChart` → `LineChart`, `ScatterChart`, `ColumnChart`; `Chart` → `PieChart`.
- **`formatting.py`** — pure utility module. `Color` and `BorderLine` constants, plus `format_color()` and `format_range()` helpers used across the other modules.

## Key Conventions

- `process_range()` in `SheetTool` normalizes range inputs into API-compatible dict format — ranges can be passed as strings or int tuples throughout the API.
- Chart objects require calling `chart_request()` to get the finalized spec; this method validates that required fields are set before returning.
- The Google Sheets API reference used throughout the codebase: `https://developers.google.com/sheets/api/reference/rest`
