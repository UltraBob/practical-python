# mortgage.py
#
# Exercise 1.7
extra_payment_start_month = 5 * 12 + 1
extra_payment_end_month = 10 * 12 - 1
extra_payment = 1000

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    month += 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        additional = extra_payment
    else:
        additional = 0
    principal = principal * (1 + rate / 12) - payment - additional
    if principal < 0:
        overpay = abs(0 - principal)
        additional -= overpay
        principal = 0
    total_paid = total_paid + payment + additional
    print(f'{month:>10d} {total_paid:15.2f} {principal:15.2f}')

print(f"Paid {total_paid} in {month} months.")
