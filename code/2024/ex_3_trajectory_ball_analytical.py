# Script calculating the trajectory of a ball.
#
#   A ball is thrown under an angle and with a specific velocity.
#   We compute the distance that the ball covers before falling
#   down and the time it takes. We don't use numerical solutions
#   but analytical formulas.

# Loading packages for sin, cos, pi, sqrt
from math import sin, cos, pi, sqrt, tan

# Parameters of the trajectory
y0 = 1.20; x0 = 0
v0 = 8
alpha0 = 37 * (pi / 180)  # Angle
g = 9.81

# compute the time that the ball will hit the ground
vy0 = v0 * sin(alpha0)
vx0 = v0 * cos(alpha0)
te = (vy0 + sqrt(vy0**2 + 2*g*y0)) / g

# compute the distance covered by the ball
xe_num = (tan(alpha0) + sqrt(tan(alpha0)**2 + 2*g*y0 / (v0*cos(alpha0))**2))
xe_den = (g / (v0 * cos(alpha0))**2)
xe = xe_num / xe_den

print(f"The ball falls at distance: {xe} m, after {te} s")

# Loading packages for plotting and numeric calculations.
# We should actually put these after the other import
# statement at the top of the file. For clarity I put
# them now here.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Computing x and y coordinates for the trajectory
ts = np.linspace(0, te, 10)
xs = vx0 * ts
ys = y0 + (vy0 * ts) - (g*ts**2)/2

# Plotting the trajectory of the ball
matplotlib.rcParams.update({'font.size': 20})
plt.plot(xs, ys, "-", color="red")
plt.plot(xs, ys, ".", color="blue")
ax = plt.gca()
ax.set_xlabel("x (in m)")
ax.set_ylabel("y (in m)")
ax.set_aspect('equal', 'box')
plt.show()
