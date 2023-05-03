from typing import List

from utils.is_prime import is_prime


def prime_counter_range(real_range: List[int]) -> int:
    # will count how many primes are inside given range
    generated_range = range(real_range[0], real_range[-1] + 1)
    print('prime_counter_range.real_range {} generated_range {}'.format(real_range, list(generated_range)))
    return sum(1 for i in generated_range if is_prime(i))
