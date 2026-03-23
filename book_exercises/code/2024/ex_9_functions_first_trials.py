# Function exercises:
#
#   This script contains some examples of how to use functions in Python
#

# NOTE: When you import packages, you put them normally at the top, further, it is good to order the imports:
#   (1) import the built-in packages,
#   (2) then the ones which are not built-in (such as Numpy or Matplotlib)
#   (3) finally you import your own modules/packages you wrote (only locally available on your computer)
#
# import built-in packages
import math

# import external packages
import matplotlib.pyplot as plt
import matplotlib
# the following line belongs actually to after the import section but since we have small scripts we can get
# away with some small Python style abuse
matplotlib.use("WebAgg")

# import your own packages
# ... (we don't have our own modules/packages yet)

# NOTE: After the imports you normally define your functions, again here we will allow ourselves a little bit more
# freedom since we are giving multiple separate examples within the same script-file.

# NOTE: I made some mistakes against the programming style: calling a variable "a" is bad practice since it does not
# convey the meaning of the variable. This is only accepted if "a" would have a clear meaning, e.g. "a" is often used
# in (long) formulas as an abbreviation for "acceleration" and is in that case more clear than writing "acceleration"

# NOTE: during class I told you can use triple quotes (''' .. ''') for Docstrings but this need to be triple quotes
# of the other kind like this (""" .. """)
#


# EXAMPLE 1:

# Function definitions for example 1:
#
def subtract(a, b):
    """
    Subtracts two numbers: a - b

    :param a: first number [float]
    :param b: second number [float]

    :return: the subtracted value a - b
    """
    return a - b


def mul(a, b):
    """
    Multiply two numbers

    :param a: first number [float]
    :param b: second number [float]

    :return: the product of a and b
    """
    return a * b


# Script for example 1
#
print("Example 1:")
# Calling our new defined "subtract" function and printing its return value
print(subtract(3.4, 6))

# Calling our new defined "mul" function and printing its return value
print(mul(4, 5))

# We can use the result of one function as an parameter in another function:
formula = mul(subtract(5, 3), 5)
print(formula)
print("Example 1 END")


# EXAMPLE 2: showing the difference between using a variable defined locally in the function or from the outer variable
#   scope.

# Function definitions for example 2:
#
def increase_value_by_x_from_script(a):
    """
    Increases the value of parameter a by the value of x defined in the script
    variable scope

    :param a: a number [float]

    :return: a increased by x
    """
    a = a + x
    return a


def increase_value_by_x(a, x):
    """
    Increases the value of parameter a by the value of x

    :param a: first number [float]
    :param x: second number [float]

    :return: a increased by x
    """
    a = a + x
    return a


# Script for example 2: Although both functions perform the same sum they use either the variable "x" = 100 from the
#   script or the one defined as parameter "x" = 110
#
x = 100
print("Example 2:")
print(increase_value_by_x_from_script(40))
print(increase_value_by_x(40, 110))
print("Example 2 END")


# EXAMPLE 3: A function can also just perform a desired action and not returning a value (or the main result is not the
#   return value.

# Function definitions for example 3:
#
def print_product(a, b):
    """
    Print product of two numbers a and b

    :param a: first number [float]
    :param b: second number [float]

    :return: the product a * b
    """
    print(f"The product of a times b = {a*b}")


# Script for example 3: The function does not return anything (which leads to the return value = None). It's main goal
# is to print the product to the screen.
return_value = print_product(34, 2)
print(f"Example 3: the return value  = {return_value}")


# EXAMPLE 4: Here we define a slightly more complex function to show that functions can provide use with a simple recipe
#   to perform the same code-block multiple times. The function calculates the refracted angle theta_2 from an incident
#   light ray under theta_1.

# Function definitions for example 4:
#
def calculate_refraction_angle(theta1, n1, n2):
    """
    Calculates the refraction angle of an incident light ray
    with angle theta1 and media refraction indices n1, n2

    :param theta1: angle incident light in degrees
    :param n1: refraction index medium 1
    :param n2: refraction index medium 2

    :return: refracted angle theta2
    """
    theta1_rad = math.radians(theta1)
    theta2_rad = math.asin(n1/n2*math.sin(theta1_rad))
    theta2 = math.degrees(theta2_rad)
    return theta2


# Script for example 4:
#
# Parameters
n1 = 1
n2 = 1.5
theta1 = 60

# Call the function multiple times within a for loop
list_of_angles = [20, 40, 60, 80]
refracted_angles = []
for angle in list_of_angles:
    refracted_angles.append(calculate_refraction_angle(angle, n1, n2))

print(f"Example 4: The list of refracted angles = {refracted_angles}")

fig, ax = plt.subplots()
ax.plot(list_of_angles, refracted_angles)
plt.show()

# Usage of functions to structure a script:
theta1 = 50
n1 = 1
n2 = 1.55
n3 = 1.35
theta2 = calculate_refraction_angle(theta1, n1, n2)
theta3 = calculate_refraction_angle(theta2, n2, n3)
print(f"The outgoing angle = {theta3}")
