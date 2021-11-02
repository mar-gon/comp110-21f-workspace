"""Utility functions."""

__author__ = "730394836"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads csv data into a list of dict rows."""
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


def head(old: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Returns a new column based table with only the n rows of data for each column."""
    new: dict[str, list[str]] = {}
    
    for column in old:
        store_items: list[str] = []
        i: int = 0
        while i < N:
            store_items.append(old[column][i])
            i += 1
        new[column] = store_items
    return new 


def select(old: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Returns only the columns you want."""
    new: dict[str, list[str]] = {}
    for column in col_names:
        new[column] = old[column]
    return new


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column based tables."""
    combined: dict[str, list[str]] = {}
    for column in first:
        combined[column] = first[column]
    for column in second:
        if column in combined:
            i: int = 0
            while i < len(second[column]):
                combined[column].append(second[column][i])
                i += 1
        else:
            combined[column] = second[column]
    return combined
