import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
erf = np.zeros_like(x)
for i in range(len(x)):
    erf[i] = math.erf(x[i])

fig, ax = plt.subplots()
ax.plot(x, erf)
ax.set_xlabel("x")
ax.set_ylabel("erf(x)")
fig.savefig("output_plot_matherf.png")
