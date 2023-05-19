import math

# pre-calculate sqrt(5) as we use it 3 times
from resources.fibonacci_nums import fibonacci_nums

sqrt5 = math.sqrt(5)


def binets_formula(n):
    """
    The central function implementing Binet's Formula
    """
    return fibonacci_nums[n + 1]
