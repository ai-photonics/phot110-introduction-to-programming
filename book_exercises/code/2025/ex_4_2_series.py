# Exercise 2: Decreasing series of numbers

# Parameters
n = 1

# Loop and output
t = 1 / n**4
while t > 0.0001:
    n += 1
    print(t)
    t = 1 / n**4
