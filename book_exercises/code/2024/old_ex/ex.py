# Integrate x^3 - x/3 over interval [0, 2]
#
import numpy as np

A = 0; B = 2
N = 10
dx = (B - A) / N
xs = np.linspace(A, B, N) + dx/2
xs = xs[:-1]
# print(xs)
ys = xs ** 3 - xs/3
# print(ys)

area = np.sum(dx*ys)
print(f"Integral = {area}")
print(f"Error = {10/3 - area}")

area_trapz = np.trapz(ys, xs)
print(f"Integral using np.trapz = {area_trapz}")
print(f"Error = {10/3 - area_trapz}")
