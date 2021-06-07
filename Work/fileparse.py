# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(lines, select=[], types=[], has_headers = True, delimiter=',', silence_errors=False) -> list:
    """
    Parse a CSV file into a list of records.
    """
    if select and not has_headers:
        raise RuntimeError("Select argument requires column headers")
    if isinstance(lines, str):
        raise SystemExit("Expecting an iterable argument that can be parsed as csv.")

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers
    headers = next(rows) if has_headers else []

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers user for resulting dictionaries.
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for row_no, row in enumerate(rows, start=1):
        if not row:
            continue
        # Filter the row if specified columns were selected
        if select:
            row = [row[index] for index in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if silence_errors:
                    continue
                print(f'Row {row_no} Invalid: `{row}` cannot be converted.')
                print(f'  Reason: {e}')

        if headers:
            # Make a dictionary
            record = dict(zip(headers, row))
        else:
            # Make a tuple
            record = tuple(row)
        records.append(record)

    return records
