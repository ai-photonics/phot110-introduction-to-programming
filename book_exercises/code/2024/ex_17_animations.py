import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
t = np.linspace(0, 2, 100)
text = "Apple!"
xx = 2 + np.sin(3*np.pi*t)
yy = 2 + np.sin(2*np.pi*t + np.pi/2)
font_size = 10 * (1 + 3 * np.sin(2*np.pi*t)**2)

ax.plot(xx, yy)
text_plot = ax.text(xx[0], yy[0], text, fontsize=font_size[0])
ax.set(xlim=[0, 6], ylim=[0, 4], xlabel='x [m]', ylabel='y [m]')


def update(frame):
    # for each frame, update the artist data.
    x = xx[frame]
    y = yy[frame]
    fontsize = font_size[frame]
    text_plot.set_x(x)
    text_plot.set_y(y)
    text_plot.set_fontsize(fontsize)
    return text_plot


ani = animation.FuncAnimation(fig=fig, func=update, frames=100, interval=50)
plt.show()

ani.save("text_animation.gif", "pillow", fps=20)
ani.save("text_animation.html", "html", fps=20)
