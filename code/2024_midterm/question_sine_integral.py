import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
integral = np.zeros_like(x)
for i in range(len(x)):
    integral[i] = np.trapz(y=y[:i], x=x[:i])

fig, ax = plt.subplots()
ax.plot(x, y, label=r"$y=\sin(x)$")
ax.plot(x, integral, label=r"$y=\int_0^x\sin(t) dt$")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.legend()
fig.savefig("output_plot_sine_integral.png")
