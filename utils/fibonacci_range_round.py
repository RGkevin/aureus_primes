from typing import List

from utils.binets_formula import binets_formula


def fibonacci_range_round(begin: int, finish: int) -> List[int]:
    fib_nums = []
    # inclusive range
    diff = finish - begin + 1
    for idx in range(diff):
        fib_nums.append(binets_formula(begin + idx))

    return fib_nums
