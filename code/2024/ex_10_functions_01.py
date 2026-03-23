# Exercises on functions (exercise 1)
# Exercise 1: Calculate the factorial of a number
#
#   Calculate the value of the factorial of a number: n!
#   by defining a new function: "factorial(n)".

def factorial(n):
    """
    Calculate the factorial of natural number n

    :param n: integer >= 0
    :return: factorial as an integer
    """
    f = 1
    for i in range(2, n+1):
        f = i * f

    return f


# Parameter(s)
n = 5
# print the factorial
print(f"The value of {n}! = {factorial(n)}")
