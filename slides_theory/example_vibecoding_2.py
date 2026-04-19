"""Plot a sine curve """
import matplotlib.pyplot as plt
from numpy import pi, sin, linspace

# Parameters
A = 1               # Amplitude
f = 2               # frequency

# Plot
x = linspace(0, 2, 1000)
y = A * sin(2 * pi * f * x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
