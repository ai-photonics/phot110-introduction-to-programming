# Exercise 2.2: Fibonacci series

# Initialize first 2 numbers and current
f1 = 1  # Initialize the first number of the series to one
f2 = 1  # Initialize the second number of the series to one
f = 0  # Initialize the current integer to zero

# Loop to generate series up to 1000 (and one times more)
while f < 1000:
    f = f1 + f2
    print(f"F = {f}")
    f1 = f2
    f2 = f
