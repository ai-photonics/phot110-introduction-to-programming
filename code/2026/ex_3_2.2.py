# Practical 3: Exercise 2.2
from math import e, factorial, fabs

mindiff = 0.001
e_approx = 0
n = 0
while fabs(e - e_approx) > mindiff:
    e_approx = e_approx + 1 / factorial(n)
    print(f"Euler's e = {e:5.5} approximated to {n+1} terms = {e_approx:5.5}")
    n = n + 1
