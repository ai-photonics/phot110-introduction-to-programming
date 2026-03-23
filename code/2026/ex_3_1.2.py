# Practical 3: Exercise 1.2
from math import sqrt

print(f"--- Roots of the equation ax^2 + bx + c = 0 ---")
a = 2
b = 3
c = -5
a = float(input("Parameter a: "))
b = float(input("Parameter b: "))
c = float(input("Parameter c: "))
D = b**2 - 4 * a * c
if D > 0:
    xm = (-b - sqrt(D)) / (2 * a)
    xp = (-b + sqrt(D)) / (2 * a)
    print(f"The discriminant D = {D} > 0, two roots x = {xm}, {xp}")
elif D == 0:
    x = -b / (2 * a)
    print(f"The discriminant D = {D} = 0, one root x = {x}")
else:
    print(f"The discriminant D = {D} < 0, no real roots!")
