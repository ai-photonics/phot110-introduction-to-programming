# Exercises on functions
# Exercise 3: Intersection of two lines
#
# Find the intersection point p = (xp, yp) between two lines with equations
#   y1 = m1 * x + c1
#   y2 = m2 * x + c2
#
# parameters of the lines:
#   m1 = 1/5
#   c1 = 2
#   m2 = 7
#   c2 = -3

# Import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("WebAgg")


def calc_intersection(m1, c1, m2, c2):
    xp = -(c2 - c1) / (m2 - m1)
    yp = m1 * xp + c1
    return xp, yp


# Parameters of the lines
m1 = 0.2
c1 = 2
m2 = 7
c2 = -3

# Calculate the intersection point
xp, yp = calc_intersection(m1, c1, m2, c2)

# Calculate the coordinates for the lines to plot
x = np.linspace(-7, 7, 100)
y1 = m1 * x + c1
y2 = m2 * x + c2

# Plot the lines and the intersection point
fig, ax = plt.subplots()
ax.plot(x, y1)
ax.plot(x, y2)
ax.plot(xp, yp, marker="x")
ax.set_xlim([-7, 7])
ax.set_ylim([-5, 5])
ax.set_aspect("equal")
plt.show()
