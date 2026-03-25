import numpy as np
import matplotlib.pyplot as plt
import module_ellipse as me

b = 1/2
a = np.linspace(0.5, 2, 100)
x = a
y = me.perimeter_ellipse(a, 1/2)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Major semi-axis a (with b = 1/2)")
ax.set_ylabel("Ellipse perimeter")
ax.set_xlim([0.5,2])
ax.grid()
fig.savefig("output_plot_ellipse.png")
