import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Prepare the plot data
t = np.linspace(0, 10, 11)
x = np.linspace(0, 1, 100)

# Plot the initial plot
fig, ax = plt.subplots()
ax.set_ylim([-0.1, 1.1])
handle = ax.plot(x, t[0] * np.sqrt(x))


def update_plot(frame):
    """ Update the plot data """
    handle[0].set_ydata(t[frame]/50 * np.sqrt(x))
    return handle


#
ani = animation.FuncAnimation(fig=fig, func=update_plot, frames=11, interval=500)
plt.show()
