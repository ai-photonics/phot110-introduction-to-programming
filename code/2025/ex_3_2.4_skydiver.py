# Exercise 2.4: Velocity of a skydiver

# Parameters
g = 9.81
k = 0.24
m = 70

# Initialization
v = 0
a = g

# Loop until the acceleration becomes very small (1 m/s^2)
while a > 1:
    v = a + v
    a = g - k * v**2 / m
    print(f"Velocity = {v} m/s")
