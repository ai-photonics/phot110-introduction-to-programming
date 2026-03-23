# Exercise 2.6: Formatted table

# Import libraries
from math import sqrt

# Input
f1 = float(input("Give a first decimal number: "))
f2 = float(input("Give a second decimal number: "))

# Output
print(f"        |  number 1  |  number 2  |    sum    ")
print(f"Number  | {f1:10.2f} | {f2:10.2f} | {f1+f2:10.2f}")
print(f"Squares | {f1**2:10.2f} | {f2**2:10.2f} | {(f1+f2)**2:10.2f}")
print(f"Sqrt    | {sqrt(f1):10.2f} | {sqrt(f2):10.2f} | {sqrt(f1+f2):10.2f}")
