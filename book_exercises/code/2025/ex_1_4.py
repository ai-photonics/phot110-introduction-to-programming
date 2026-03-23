# Exercise 4: Compute the refracted angle from Snellius law
# Hint: the arcsine can be calculated by the function asin
# available from the math library

# import sine, arcsine, and variable pi from the math library
from math import sin, asin, pi

# Here we use fixed refraction indices as parameters of our script
n1 = 1.0
n2 = 1.55
# Prompt the user to give the incident angle (in degrees)
theta1_degrees = float(input("Give the angle of the incident light (in degrees): "))

# Extract the angle theta2 from the incident angle theta1 and refraction indices n1 and n2
theta1 = theta1_degrees / 180 * pi
theta2 = asin(n1 / n2 * sin(theta1))
# convert back to degrees
theta2_degrees = theta2 / pi * 180
# Print out the result
print(f"For an incident angle: {theta1_degrees}, the refracted angle is: {theta2_degrees}")
