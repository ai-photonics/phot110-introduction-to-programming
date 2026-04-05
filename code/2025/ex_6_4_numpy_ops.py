import numpy as np

# Create the x-coordinates
x = np.linspace(-2, 2, 20)

# Define different y-coordinates/functions of x
#
# y = x^3
y1 = x ** 3
print(y1)
#
# y = sin(pi x)
y2 = np.sin(np.pi * x)
print(y2)
#
# y = sqrt(x + 2)
y3 = np.sqrt(x + 2)
print(y3)
#
# y = sin(pi x) / x
y4 = np.sin(np.pi * x) / x
print(y4)
