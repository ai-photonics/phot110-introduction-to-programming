# Practical 3: Exercise 2.3
from math import sqrt, floor

N = int(input("Give a positive integer N: "))
n_max = sqrt(N)
is_prime = True
for n in range(2, floor(n_max) + 1):
    if N % n == 0:
        print(f"The number {N} can be divided by {n}")
        is_prime = False

if is_prime:
    print(f"The number {N} is prime")
else:
    print(f"The number {N} is not prime")
