# Exercises on functions (exercise 2)
# Exercise 2: Calculate the number of combinations without replacement
#
#   The number of combinations of k items out of a set of n objects is
#   defined in statistics as

#       C(n, k) = n! / ((n-k)! * k!) with k <= n
#
# - Use the function `factorial(n)` which you created in previous
#       exercise 1 to calculate the number of combinations C(5, 3).
# - Afterwards create a function `combinations(n, k)` to compute the
#       combinations.

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


def combinations(n, k):
    """
    Calculate the number of combinations of 3 items out of a set of n objects
    :param n: size of the set [integer]
    :param k: number of items chosen [integer]
    :return: number of combinations
    """
    n_combinations = factorial(n) / (factorial(n-k) * factorial(k))

    return n_combinations


# Script of exercise 2
n = 5
k = 3
n_combinations = factorial(n) / (factorial(n-k) * factorial(k))
print(f"The number of combinations C(5, 3) = {n_combinations}")
# Now with using the function combinations(n, k)
print(f"The number of combinations C(6, 2) = {combinations(6, 2)} (using the function)")
