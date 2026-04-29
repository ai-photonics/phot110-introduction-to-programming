import numpy as np
import matplotlib.pyplot as plt

## -------- (1-2)
# Parameters
B = 3; A = -3
N = 100

# Forward differences
dx = (B - A) / N
x = np.linspace(A, B, N+1)
y = np.sin(5 * np.pi * x) / (1 + x ** 2)
#
dy = np.diff(y)
der_forward = dy / dx
der_central = (y[2:] - y[:-2]) / (2 * dx)
#
xx = np.linspace(A, B, 1000)
der_exact = 5 * np.pi * np.cos(5 * np.pi * xx) / (1 + xx ** 2)  -  2 * xx * np.sin(5 * np.pi * xx) / (1 + xx ** 2) ** 2

fig, ax = plt.subplots()
ax.plot(xx, der_exact, label="exact")
ax.plot(x[:-1], der_forward, label="forward")
ax.plot(x[1:-1], der_central, label="central")
ax.legend()
plt.show()
