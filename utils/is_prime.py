from math import sqrt

from utils.last_digit import last_digit


def is_prime(n: int) -> bool:
    """A Python program to check if a given number n is prime,
    using the (6k+-1) rule."""

    if n <= 1:
        return False

    if n in (2, 3, 5):
        return True

    # n_last_digit = last_digit(n)
    # if n_last_digit not in (1, 3, 7, 9):
    #     print('last_digit IS NOT A PRIME CANDIDATE', n, n_last_digit)
    #     return False

    if n % 6 not in (1, 5):
        return False

    # for f in range(5, int(n ** 1 / 2) + 1, 6):
    #     if not n % f or not n % (f + 2):
    #         return False

    for x in range(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True
