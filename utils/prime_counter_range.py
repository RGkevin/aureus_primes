from typing import List

from utils.digital_root import digital_root
from utils.is_prime import is_prime
from utils.last_digit import last_digit


def prime_counter_range(real_range: List[int]) -> int:
    # will count how many primes are inside given range
    is_even = real_range[0] % 2 == 0
    begin = real_range[0] + 1 if is_even else real_range[0]
    finish = real_range[1] if is_even else real_range[1] - 1
    generated_range = list(range(begin, real_range[-1] + 1, 2))
    filtered_gen_range = list(
        filter(lambda num: last_digit(num) in (1, 3, 7, 9), generated_range))

    print('prime_counter_range.real_range {} filtered_gen_range {}'.format(real_range, len(filtered_gen_range)))

    return sum(1 for i in filtered_gen_range if is_prime(i))
