import matplotlib.pyplot as plt
import numpy as np

#x = [0, 2, 6, 1, 4]
#y = [7, 4, 11, 43, 3]
#x = np.arange(-2, 3.3, 1)
x = np.linspace(-2, 3.3, 100)
y = x / 3 + x**3 / np.sqrt(x + 3)
fig, axs = plt.subplots(2,2)
axs[0, 1].plot(x, y, color="orange", linewidth=10)
axs[0, 0].plot(x, x**2, color="green", linewidth=5)
ax = plt.gca()
ax.set_xlabel("x (in nm)", fontsize=34)
plt.show()

