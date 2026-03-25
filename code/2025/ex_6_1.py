# Practical 6, exercise 1: Plotting functions
import numpy as np
import matplotlib.pyplot as plt

sigma = 2
gamma = 1
x = np.linspace(-5, 5, 500)
y1 = 1/np.sqrt(2*np.pi*sigma**2) * np.exp(-x ** 2 / (2*sigma ** 2))
y2 = 1/np.pi * gamma / (x**2 + gamma**2)
y3 = y2 - y1
plt.plot(y1)
plt.plot(y2)
plt.plot(y3)
plt.ylabel("y")
plt.xlabel("x")
plt.legend(["Gaussian","Lorentz","Difference"])
plt.show()
