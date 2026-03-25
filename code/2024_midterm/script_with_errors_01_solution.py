# This script contains errors and doesn't run.
#
# The correct script prompts the user to enter an angle
# in degrees. The angle is then converted to radians and
# printed on the screen.
#
# Correct the errors so that it gives the intended output.

import math

print("-- Conversion from degrees to radials --")

the_angle = input("Provide the angle in degrees: ")
angle_in_radians = math.pi * the_angle / 180
print(angle_in_radians)

print("-- Conversion is finished --")

