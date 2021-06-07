#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
import stock
import tableformat


def read_portfolio(filename: str) -> list:
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    with open(filename, 'rt') as f:
        holdings = parse_csv(f, types=[str, int, float])
        portfolio = [stock.Stock(holding['name'], holding['shares'], holding['price']) for holding in holdings]
    return portfolio


def read_prices(filename: str) -> dict:
    """
    Read prices from a CSV file of name, price data
    :param filename:
    :return:
    """
    with open(filename, 'rt') as f:
        prices = parse_csv(f, types=[str, float], has_headers=False)
    return dict(prices)


def make_report(portfolio, prices):
    data = []
    for holding in portfolio:
        price = prices[holding.name]
        data.append((holding.name, holding.shares, price, price - holding.price))
    return data


def print_report(report_data, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report_data:
        row_data = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(row_data)


def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    if len(argv) not in [3, 4]:
        raise SystemExit(f'Usage: {argv[0]} portfoliofile pricefile')
    print(argv)
    portfolio_report(*argv[1:])


if __name__ == '__main__':
    import sys
    main(sys.argv)
