# DELLOITE_1
# JSON Data Format Converter

This Python project converts two different JSON data formats into a unified output format. It handles device telemetry data from two distinct source structures and normalizes them for easier processing and analysis.

---

## Description

The repository contains Python code that reads JSON files in two formats representing device telemetry data. The program transforms both formats into a common structure with consistent field names and types.

Key features:
- Supports multiple input JSON schemas.
- Converts ISO 8601 timestamps to Unix milliseconds where necessary.
- Unifies device, location, and telemetry data into a consistent output.
- Includes unit tests to verify correctness with sample data.

This project demonstrates data transformation, JSON manipulation, and testing in Python.

---

## Files

- `main.py` — Main program with conversion functions and unit tests.
- `data-1.json` — Sample JSON file in format type 1.
- `data-2.json` — Sample JSON file in format type 2.
- `data-result.json` — Expected unified output format.
  
---

## Usage

1. Ensure Python 3 is installed.
2. Place your JSON input files (`data-1.json` and/or `data-2.json`) in the project directory.
3. Run the tests to validate conversion:

```bash
python main.py
