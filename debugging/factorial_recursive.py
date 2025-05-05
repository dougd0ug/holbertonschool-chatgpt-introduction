#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer n.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of n (n!), or 1 if n == 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Retrieve the first command-line argument, convert it to an integer,
# compute its factorial, and print the result.
f = factorial(int(sys.argv[1]))
print(f)
