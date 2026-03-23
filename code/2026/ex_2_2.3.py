# Practical 2: Exercise 2.3

# Import statements
from math import exp

# Parameters
dv = 7.8
ve = 2.5

# Input
ms = float(input("Mass of the satelite (kg): "))
mr = float(input("Mass of the empty rocket (kg): "))

# Calculate require mass of fuel
mf = ((ms + mr) - 1) * exp(dv / ve)

# Output
print(f"==> Required fuel = {mf:4.4} kg")
