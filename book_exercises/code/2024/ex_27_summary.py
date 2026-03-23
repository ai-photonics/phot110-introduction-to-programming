# Exercises on function definitions:
import numpy as np
import matplotlib.pyplot as plt


def fct_name(x, y):
    z = x + y
    return z


# Exercise (2)
def fct_2(x):
    z = x ** 2 + 5
    return z


# Exercise (3)
def fct_3(x):
    z = np.sin(2 * np.pi * x) / (x + 3)
    return z


# Exercise (3)
def fct_4(x):
    z = np.zeros_like(x)
    z[x > 0] = x[x > 0]
    z[x <= 0] = 0
    return z


def fct_5(x):
    if x < 0:
        print("The number is smaller than zero")
    else:
        print("The number is larger or equal to zero")
    return None


def fct_6(x):
    if x < 0:
        print("The number is smaller than zero")
    else:
        print("The number is larger or equal to zero")
    return None


#fct_5(-34)

# Run functions:
# (1)
#z = fct_name(4, 5)
#print(f"fct_name(4,5) = {z}")

# (2) example for x = 6
#z = fct_2(6)
#print(f"z(6) = {z}")

# (3)
#x = np.linspace(0, 5, 100)
#z = fct_3(x)
#print(f"z(6) = {z}")
#plt.plot(z)

# (4)
#x = np.linspace(-1,1, 100)
#z = fct_4(x)
#plt.plot(z)

#plt.show()

# (5)
#import module_numbers as mn

#mn.larger_or_not(56)

# (6)
class NumberGym:

    def __init__(self, number):
        self.number = number

    def print_larger_than(self, x):
        if x < self.number:
            print(f"The number is smaller than {self.number}")
        else:
            print(f"The given number is larger or equal to {self.number}")
        return None

n = NumberGym(7)
print(n)

n.print_larger_than(8)
