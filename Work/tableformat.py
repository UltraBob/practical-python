# tableformat.py

class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, row_data):
        for column in row_data:
            print(f'{column:>10}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """
    def headings(self, headers):
        print(','.join(headers))

    def row(self, row_data):
        print(','.join(row_data))

class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """
    def print_row(self, data, wrapper='td'):
        print('<tr>', end='')
        for column in data:
            print(f'<{wrapper}>{column}</{wrapper}>', end='')
        print('</tr>')

    def headings(self, headers):
        self.print_row(headers, 'th')

    def row(self, row_data):
        self.print_row(row_data)


def create_formatter(name):
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')
    return formatter


def print_table(portfolio, columns, formatter):
    formatter.headings(columns)
    for holding in portfolio:
        line = [getattr(holding, column) for column in columns]
        formatter.row(line)


class FormatError(Exception):
    pass
