#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27
import os, csv, sys
from report import read_portfolio


def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    cost = 0
    for holding in portfolio:
        cost += holding.cost
    return cost


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfoliofile')
    filename = argv[1]
    cost = portfolio_cost(filename)
    print(f'Total cost {cost:.2f}')


if __name__ == '__main__':
    import sys
    main(sys.argv)
