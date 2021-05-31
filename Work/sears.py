# sears.py
bill_thickness = 0.11 * 0.001 # Meters (0.11mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    day += 1
    num_bills *= 2

print(f"It took {day} days.")
print(f"We stacked up {num_bills} bills.")
print(f"The final height was {num_bills * bill_thickness}m.  This is {num_bills * bill_thickness - sears_height}m tallers than the tower.")
