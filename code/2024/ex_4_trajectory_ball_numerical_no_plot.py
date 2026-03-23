# Script calculating the trajectory of a ball.
#
#   A ball is thrown under an angle and with a specific velocity.
#   We compute the distance that the ball covers before falling
#   down and the time it takes. We use a numerical approximation
#   to find the velocity and position at each time-step.

# Load library for sin, cos
import math

# Algorithm parameters in MKS units
v0 = 6
angle_in_degrees = 37
g = 9.81
x = 0; y = 1.20; t = 0

# Calculate initial velocity in x
#     and y directions
angle = angle_in_degrees * math.pi / 180
vx = v0 * math.cos(angle)
vy = v0 * math.sin(angle)

# Initiate values at time t = 0
x_values = list([x])
y_values = list([y])
t_values = list([t])

# Find the trajectory by step-by-step incrementing time and at each time-step
# approximating the velocity according to the constant downward acceleration
# (Euler approximation, forward difference scheme).
# Print the (x, y) coordinates for each time-step
dt = 0.1
print(f't = {t:.2f}: ({x:.2f},{y:.2f})')
while (y >= 0) and (t < 10):
    # update velocities (vx, vy), coords (x, y), and time t
    vy = vy - g * dt
    y = y + vy * dt
    x = x + vx * dt
    t = t + dt
    x_values.append(x)
    y_values.append(y)
    t_values.append(t)
    print(f't = {t:.2f}: ({x:.2f},{y:.2f})')
