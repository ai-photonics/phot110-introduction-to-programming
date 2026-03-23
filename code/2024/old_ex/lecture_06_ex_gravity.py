# ex 6: Compute and plot the orbit of a planet around a star:
#
# Assume the star has a fixed position.
# The planet undergoes the gravitational force F:
#       F = G*m1*m2 / R^2
# where m1 = mass of the planet, m2 = mass of the star
#   G = the gravitational constant, and R the distance
#   between the planet and the star (changes in time).
# To simplify the problem we assume G = 1, m1 = 1, m2 = 10,
# and the coordinate of the sun in the origin.
#
# Use a while loop to find the planet position at
# consequent times.

# Import statements
import math
#
import matplotlib.pyplot as plt

# initial t, position, and velocity
G = 1
m1 = 1; m2 = 10
t = 0
x = 1; y = 0
vx = 0; vy = 3.8
ax = 0; ay = 0
traversed_angle = 0
dt = 0.01

xs = []
ys = []
ts = []
while (traversed_angle < 1.95*math.pi) and (t < 100):
    # Calculate the current distance between the
    # planet and the star
    R = math.sqrt(x**2 + y**2)
    # Calculate the gravitational force
    F = G * m1 * m2 / R**2
    # Calculate the x and y components of the force
    Fx = -x/R * F
    Fy = -y/R * F
    # Derive the acceleration from the force
    ax = Fx / m1
    ay = Fy / m1
    # Update the velocity with the acceleration
    vx = vx + ax * dt
    vy = vy + ay * dt
    # Update the positions with the velocity
    x = x + vx * dt
    y = y + vy * dt
    # Append the new positions to the coords xs and ys
    xs.append(x)
    ys.append(y)
    # increase the time and append
    t = t + dt
    ts.append(t)
    # update the traversed angle
    traversed_angle = math.atan2(y, x)

# Plot the coordinates with a line plot
plt.plot(xs, ys)
plt.show()

# Plot the coordinates using a scatter plot and indicate
# time with color of the dots
plt.scatter(xs, ys, 20, ts)
plt.show()

