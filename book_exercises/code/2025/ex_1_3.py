# Exercise 3: use the import command to be able to use the math library
# Hint: You can use multiple ways to import functions or objects:
#   (1) import math
#   (2) from math import sin, cos, pi
#   (3) from math import sqrt as sr

# import sine, cosine, and variable pi from the math library
from math import sin, cos, pi
angle = float(input("Give an angle (in degrees): "))

# Verify that the sine squared plus cosine squared results into one
y = sin(angle)**2 + cos(angle)**2
# Print out the result in a clear manner using a formatted string (put f in front of the "-symbol)
print(f"sin({angle})**2 + cos({angle})**2 = {y}")

# Calculate the sine of an angle given in degrees
y = sin(angle / 180 * pi)
# Output the result (we used the same variable name here as before)
print(y)
