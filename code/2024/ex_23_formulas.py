import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 400)
x = x.astype(dtype=complex)
print(x.dtype)

y = np.real(np.sqrt(x))

plt.plot(np.real(x), y)
plt.show()
