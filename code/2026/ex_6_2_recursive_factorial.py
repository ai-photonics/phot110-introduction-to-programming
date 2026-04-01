def standard_factorial(N):
    """Calculates the factorial of N:   N! = N(N-1)(N-2) ... 2 1

    :param N: integer
    """
    f = 1
    for i in range(2, N+1):
        f = f * i
    
    return f


def recursive_factorial(N):
    """Calculates the factorial of N:   N! = N(N-1)(N-2) ... 2 1
    This is a recursive function.
    
    :param N: integer
    """
    if N > 1:
        return N * recursive_factorial(N-1)
    else:
        return 1
    

# Script
N = 5
print(f"standard_factorial({N}) = {standard_factorial(N)}")
print(f"recursive_factorial({N}) = {recursive_factorial(N)}")
