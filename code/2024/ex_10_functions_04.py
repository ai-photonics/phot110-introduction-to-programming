# Exercises on functions
# Exercise 4: Intersection of many lines
#
# Use the function that you created in exercise 3 to
# calculate the intersection of a line with a list of
# other lines defined by:
#
# Parameters of the single line:
# m1 = -0.1
# c1 = 2
#
# Parameters of the other lines:
# m_list = [-3, 2, -1.5, 3,  -1, 10];
# c_list = [3,   1, -1,  -2, -1,   0]

# Import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("WebAgg")


def calc_intersection(m1, c1, m2, c2):
    xp = -(c2 - c1) / (m2 - m1)
    yp = m1 * xp + c1
    return xp, yp


# Parameters of the single line:
m1 = -0.1
c1 = 2

# Parameters of the lines:
m_list = [-3, 2, -1.5, 3, -1, 10]
c_list = [3, 1, -1, -2, -1, 0]

# Calculate the coordinates for the first line
x = np.linspace(-7, 7, 100)
y1 = m1 * x + c1

# Initialize the plot
fig, ax = plt.subplots()
ax.plot(x, y1, linewidth=3)

# Loop over all the other lines
for i in range(len(m_list)):
    m2 = m_list[i]
    c2 = c_list[i]
    # Calculate the second line
    y2 = m2 * x + c2
    # Calculate the intersection point
    xp, yp = calc_intersection(m1, c1, m2, c2)
    # Plot the lines and the intersection point
    ax.plot(x, y2, color="gray")
    ax.plot(xp, yp, marker="x")

# Set the limits of the plot and show
ax.set_xlim([-7, 7])
ax.set_ylim([-5, 5])
ax.set_aspect("equal")
plt.show()
