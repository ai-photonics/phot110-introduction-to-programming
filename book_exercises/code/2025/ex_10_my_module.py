# This is an example module
#
# This module is used in lecture_13_ex_my_script to show
# how modules can be imported

def add(a, b):
    """ adds a + b """
    return a + b


def mul(a, b):
    """ multiplies a * b """
    return a * b


if __name__ == "__main__":
    # Testing the module functions
    x = 5
    y = 3
    print(f"The sum of {x} and {y} = {add(x, y)}")
    print(f"The product of {2} and {4} = {mul(5, 4)}")
