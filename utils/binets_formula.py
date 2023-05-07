import math

# pre-calculate sqrt(5) as we use it 3 times
from resources.fibonacci_nums import fibonacci_nums

sqrt5 = math.sqrt(5)


def binets_formula(n):
    """
    The central function implementing Binet's Formula
    """
    return fibonacci_nums[n + 1]

    # f_n = int((((1 + sqrt5) ** n - (1 - sqrt5) ** n) / (2 ** n * sqrt5)))

    # return f_n
