from functools import reduce

from utils.binets_formula import binets_formula
from utils.fibonacci_sum_formula import fibonacci_sum_formula


def sums_range(start_idx, end, fibonacci_nums):
    if len(fibonacci_nums) == 1:
        raise Exception('nums should have more than 1 element {}'.format(fibonacci_nums))

    sum_helper = [] if start_idx == 0 else [fibonacci_sum_formula(start_idx - 1)]

    return reduce(fib_sum_reducer, sum_helper + fibonacci_nums)


def fib_sum_reducer(prev, current):
    return [prev + current] if not isinstance(prev, list) else prev + [prev[-1] + current]
