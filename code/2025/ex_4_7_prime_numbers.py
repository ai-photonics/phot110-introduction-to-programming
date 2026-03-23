# Exercise 7: Prime numbers

# Import math for
from math import sqrt

# Input number
n = int(input("Please provide a positive number: "))

# Check whether the number is prime
is_prime = True
m_max = int(sqrt(n))
for m in range(2, m_max+1):
    if n % m == 0:
        is_prime = False

# Output
if is_prime:
    print(f"The number {n} is a prime number.")
else:
    print(f"The number {n} is not a prime number.")
