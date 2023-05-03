def is_prime(n: int) -> bool:
    """A Python program to check if a given number n is prime,
    using the (6k+-1) rule."""

    if type(n) != int:
        raise TypeError('n must be int')

    if n <= 1:
        raise ValueError('n must be >= 2')

    if n in (2, 3, 5):
        return True

    if n % 6 not in (1, 5):
        return False

    for f in range(5, int(n ** 1 / 2) + 1, 6):
        if not n % f or not n % (f + 2):
            return False

    return True
