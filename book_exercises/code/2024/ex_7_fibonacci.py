# Script which exemplifies the advantage of using a range: Fibonacci series
#
import numpy as np
import matplotlib.pyplot as plt

F0 = 0
F1 = 1
N = 1000
M = 10
ys = []
xs = []
for i in range(N):
    F = F0 + F1
    F0 = F1
    F1 = F
    if i % M == 0:
        xs.append(i)
        ys.append(F)
        print(F)

plt.semilogy(xs, ys)

ns = np.arange(N)
Fs = np.zeros((N, 1))
F0 = 0
F1 = 1
for i in ns:
    F = F0 + F1
    F0 = F1
    F1 = F
    Fs[i] = F
    if i % M == 0:
        print(F)

plt.semilogy(ns, Fs)
plt.show()
