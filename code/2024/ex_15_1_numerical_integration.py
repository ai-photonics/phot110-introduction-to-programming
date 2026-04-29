import numpy as np


## -------- (1-2)
# Parameters
B = 2; A = 0
N = 10

# Integral calculation
dx = (B - A) / N
x = [A + (i - 1 / 2) * dx for i in range(1, N + 1)]
x = np.array(x)
y = x ** 3 - x / 3
#
I_approx1 = np.sum(y * dx)
I_exact = 10/3

print("Exercise 15.1 (1-2):")
print(f"Riemann rule integral = {I_approx1:6.6} for N = {N}, exact integral = 10/3 = {I_exact:6.6}")

## -------- (3)
dx = (B - A) / N
x = [A + i * dx for i in range(0, N + 1)]  # This is the same as np.linspace(A, B, N+1)
x = np.array(x)
y = x ** 3 - x / 3
I_approx2 = np.sum((y[1:] + y[:-1]) * dx / 2)

print("Exercise 15.1 (3):")
print(f"Trapezium rule integral = {I_approx2:6.6} for N = {N}, exact integral = 10/3 = {I_exact:6.6}")

## -------- (4)
I_approx3 = np.trapezoid(y=y, dx=dx)

print("Exercise 15.1 (4):")
print(f"Trapezium (Numpy) rule integral = {I_approx3:6.6} for N = {N}, exact integral = 10/3 = {I_exact:6.6}")
