from functools import reduce

from utils.binets_formula import binets_formula


def sums_range(start, end, fibonacci_nums):
    if len(fibonacci_nums) == 1:
        raise Exception('nums should have more than 1 element {}'.format(fibonacci_nums))

    sum_helper = [] if start == 0 else [binets_formula(start - 1)]

    return reduce(fib_sum_reducer, sum_helper + fibonacci_nums)


def fib_sum_reducer(prev, current):
    return [prev + current] if not isinstance(prev, list) else prev + [prev[-1] + current]
