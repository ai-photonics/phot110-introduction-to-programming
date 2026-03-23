# Exercises on functions

# Import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("WebAgg")


# Exercise 1: Calculate the factorial of a number
#
#   Calculate the value of the factorial of a number: n!  by defining a new function: "factorial(n)".
#


# calculate the factorial
def factorial(n):
    f = 1
    for i in range(2, n):
        f = i * f
    return f

# Script of exercise 2

# input parameter
n = 5

# print the factorial
print(f"The value of {n}! = {factorial(n)}")

# Exercise 2: Calculate the number of combinations
#
# The number of combinations of k items out of a set of n objects is defined in statistics as
# $$
# \mathcal{C}_k^n = \begin{pmatrix}n\\k\end{pmatrix} = \frac{n!}{(n-k)! \, k!}
# $$
# where $k \leq n$.
#
# - Use the function `factorial(n)` which you created in previous exercise 1 to calculate the number of combinations $\mathcal{C}_3^5$.
# - Afterwards create a function `combinations(n, k)` to compute the combinations.

# Exercise 3: Intersection of two lines
#
# Find the intersection point $p = (x_p, y_p)$ between two lines with equations
#
# parameters of the lines: pick $m_1 = 1/5$ and $m_2 = 7$ as the direction coefficients, and $c_1 = 2$ and $c_2 = -3$ the off-sets at $x = 0$.

# Parameters of the lines
m1 = 0.2;
c1 = 2
m2 = 7;
c2 = -3

# Calculate the intersection point
# (convert the next couple of lines into a function)
xp = -(c2 - c1) / (m2 - m1)
yp = m1 * xp + c1

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


# Exercise 4: Intersection of many lines
#
# Use the function that you created in exercise 3 to calculate the intersection of a line with a list of other lines defined by:

# Parameters of the single line:
# m1 = -0.1
# c1 = 2
#
# Parameters of the other lines:
# m_list = [-3, 2, -1.5, 3,  -1, 10];
# c_list = [3,   1, -1,  -2, -1,   0]

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

ax.set_xlim([-7, 7])
ax.set_ylim([-5, 5])
ax.set_aspect("equal")
plt.show()
