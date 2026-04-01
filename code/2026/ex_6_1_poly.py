# Practical 6: Exercise 1
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def get_roots(a=0, b=0, c=0):
    """Calculate real-valued roots of the quadratic equation:
        a*x^2 + b*x + c = 0

    :param a: coefficient second order term, defaults to 0
    :param b: coefficient first order term, defaults to 0
    :param c: coefficient constant term, defaults to 0
    :return: number of roots, list of roots 
    :rtype: int, [int]
    """
    D = b ** 2 - 4 * a * c
    if D < 0:
        return 0, []
    elif D == 0:
        return 1, [-b / (2.0 * a)]
    elif D > 0:
        x1 = (-b - sqrt(D)) / (2.0 * a)
        x2 = (-b + sqrt(D)) / (2.0 * a)
        return 2, [x1, x2]


def polynomial_intersection(a1=0, b1=0, c1=0, a2=0, b2=0, c2=0):
    """Find the intersecting (x, y)-coordinates of two polynomials

    :param a1: Polynomial 1, coefficient second order term, defaults to 0
    :param b1: Polynomial 1, coefficient first order term, defaults to 0
    :param c1: Polynomial 1, coefficient constant term, defaults to 0
    :param a2: Polynomial 1, coefficient second order term, defaults to 0
    :param b2: Polynomial 1, coefficient first order term, defaults to 0
    :param c2: Polynomial 1, coefficient constant term, defaults to 0
    :return: number of roots, list of x-coordinates, list of y-coordinates 
    :rtype: int, [int], [int]
    """
    n_roots, xs = get_roots(a1-a2, b1-b2, c1-c2)
    ys = [a1 * x ** 2 + b1 * x + c1 for x in xs]
    
    return n_roots, xs, ys


# Script
# Parameters of two polynomials
a1 = 2; b1 = 1; c1 = -4
a2 = 0; b2 = -3; c2 = 5

# Extract the intersecting points
n_roots, xs, ys = polynomial_intersection(a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2)

# Plot the curves and annotate the intersection points
if n_roots > 0:
    xx = np.linspace(xs[0]-1, xs[-1] + 1, 100)
else:
    xx = np.linspace(-2, 2, 100)

yy1 = a1 * xx ** 2 + b1 * xx + c1
yy2 = a2 * xx ** 2 + b2 * xx + c2
plt.plot(xx, yy1)
plt.plot(xx, yy2)
plt.scatter(xs, ys, color="green")
plt.show()
