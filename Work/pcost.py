# pcost.py
#
# Exercise 1.27
cost = 0
with open('Data/portfolio.csv') as f:
    next(f)
    for line in f:
        parts = line.split(',')
        cost += int(parts[1]) * float(parts[2])

print(f'Total cost {cost:.2f}')
