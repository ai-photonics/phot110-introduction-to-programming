import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
y = np.linspace(-2, 2, 100)

[xx, yy] = np.meshgrid(x, y)
print(xx)

plt.scatter(xx, yy)
plt.show()

zz = xx ** 2 + np.sin(2*np.pi*yy)

plt.pcolormesh(xx, yy, zz)
plt.show()
