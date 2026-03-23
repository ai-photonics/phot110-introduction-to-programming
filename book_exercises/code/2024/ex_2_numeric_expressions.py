# Lecture 02: Examples of ways to import a package

# import the package with its name
import math

area = 3**2 * math.pi
print(f"Area of a circle with radius 3 = {area}")

# import functions of the package separately
from math import sin, cos, pi, sqrt

angle = 23/180*pi
formula = sqrt(2/3) * sin(angle) + cos(angle)

# import all functions of a package
from math import *

a_value = 3 * sinh(pi/2)
print(f"The value of 3*sinh(pi/2) = {a_value}")

# import packages or functions and rename them
from math import sqrt as sr

print(f"The square root of 2 = {sr(2)}")
