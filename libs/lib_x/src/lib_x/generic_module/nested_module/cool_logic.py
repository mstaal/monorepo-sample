import math


def square_root(x):
    """Returns the square root of a number."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)