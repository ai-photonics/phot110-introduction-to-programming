import matplotlib.pyplot as plt
import numpy as np

# Plot 1 plot in 1 figure
fig, ax = plt.subplots(1, 1)
ax.plot([1, 2, 4, 5, 6], [1, 3, 2, 7, 5])

# Plot 1 subplot in multiple axes
fig, ax = plt.subplots(2, 3)
ax[0, 2].plot([1, 2, 4, 5, 6], [1, 3, 2, 7, 5])

# Plot a 1D function
x = np.linspace(0, 1, 100)
y = np.sin(2 * np.pi * x)
fig, ax = plt.subplots(1, 1)
ax.plot(x, y)

# Plot a 1D function as a subplot
x = np.linspace(0, 1, 100)
fig, ax = plt.subplots(2, 3)
for i in range(3):
    ax[0, i].plot(x, x**i)
    ax[1, i].plot(x, 1 / (1 + i*x))

# Plot a 2D function
x = np.linspace(0, 2, 100)
y = np.linspace(0, 2*np.pi, 100)
xx, yy = np.meshgrid(x, y)
zz = np.sin((xx - 1) * (yy-1))# - np.sqrt(xx**2 + yy**2)/10
zz = zz / np.max(zz)
fig, ax = plt.subplots()
pc = ax.pcolormesh(xx, yy, zz, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=ax)
ax.set_title('pcolormesh()')

# Plot 2D functions as subplots
fig, ax = plt.subplots(1, 2)
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
xx, yy = np.meshgrid(x, y)
zz = np.sin(2*np.pi * xx * yy ** 2)
ax[0].pcolormesh(xx, yy, zz)
ax[1].contour(xx, yy, zz)
ax[1].set_xlabel(r"$\lambda_x$")

# Create the plots
plt.show()
