#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.

    Parameters:
        n (int): The integer whose factorial is to be calculated.

    Returns:
        int: The factorial of n.
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Fix: decrement n to avoid infinite loop
    return result

if __name__ == "__main__":
    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            f = factorial(number)
            print(f)
    except (IndexError, ValueError):
        print("Usage: ./factorial.py <non-negative integer>")
