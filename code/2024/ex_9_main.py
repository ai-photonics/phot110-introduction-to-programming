#import formulas
import numpy as np
import matplotlib.pyplot as plt
from module_formulas import gaussian

x = np.linspace(-5, 5, 100)
y = gaussian(x, 2)
plt.plot(x, y)
plt.show()
