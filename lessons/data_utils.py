"""Some helpful utility functions for working w CSV file."""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of cvs into a dict."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    # prepare to read the data file as csv rather than just strings
    csv_reader = DictReader(file_handle)
    # read each row line my line
    for row in csv_reader:
        result.append(row)
    # close file to free its resources
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table into a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column) 
    return result