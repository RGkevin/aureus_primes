import logging
import math
import os
import sys
from datetime import datetime
from functools import reduce

import numpy
from numpy import where

from definitions import ROOT_DIR
from generators.prime_range_generator import positional_primes_generator
from generators.summatory import sums_range
from utils.end_experiment import end_experiment
from utils.fibonacci_range_round import fibonacci_range_round
from utils.list_ranges import list_ranges
from utils.logger_parser import logger_parser
from utils.logging_setup import logging_setup
from utils.possible_primes import possible_primes
from utils.prime_range_generator import prime_range_generator

logging_setup()

dimension_start_idx = 0
dimension_end_idx = 20
now = datetime.now()

fibonacci_nums = fibonacci_range_round(dimension_start_idx, dimension_end_idx)
logger_parser('SETUP.EXPERIMENT.fibonacci_counter', 'Dimension start {}({}) end {}({}) \n {}', [
    dimension_start_idx,
    fibonacci_nums[0],
    dimension_end_idx,
    fibonacci_nums[-1],
    fibonacci_nums,
])

fibonacci_sums = sums_range(dimension_start_idx, dimension_end_idx, fibonacci_nums)
logger_parser('SETUP.EXPERIMENT.fibonacci_counter', 'fibonacci_sums calculated \n {}', [fibonacci_sums])

upto = fibonacci_sums[-1]

max_prime_idx = int(math.sqrt(upto)) // 2
possible_primes_calculated = possible_primes(upto)
sums_to_reduce = fibonacci_sums if dimension_start_idx > 1 else fibonacci_sums[2:]
logger_parser('SETUP.EXPERIMENT.fibonacci_counter', 'sums_to_reduce \n {}', [sums_to_reduce])

positional_counter_primes = numpy.ones((upto - 1) // 2, dtype=bool)

positional_primes_generator(possible_primes_calculated, positional_counter_primes, max_prime_idx)

# NOTE: requires a lot of memory
# primes = possible_primes_calculated[positional_counter_primes]

# count primes using fibonacci ranges
fibonacci_sums_ranges = list_ranges(fibonacci_sums)
start_possible_prime = sums_to_reduce[0] + 1 if sums_to_reduce[0] % 2 == 0 else sums_to_reduce[0]
logger_parser('IN_PROGRESS.EXPERIMENT.fibonacci_counter', 'start_possible_prime {}', [start_possible_prime])


def sum_primes_in_range(start_idx, end):
    # start_idx = possible_primes_calculated
    total = 0
    latest_idx = start_idx
    latest_odd_num = possible_primes_calculated[start_idx]

    while latest_odd_num <= end:
        if positional_counter_primes[latest_idx]:
            total += 1

        latest_idx += 1
        latest_odd_num += 2

    res = [start_idx, latest_idx, total]
    logger_parser('IN_PROGRESS.EXPERIMENT.fibonacci_counter', 'sum_primes_in_range result {}', [res])

    return res


def fib_ranges_sum_reducer(prev, current):
    start = prev if not isinstance(prev, list) else prev[-1][1]
    end = current
    start_idx = where(possible_primes_calculated == start_possible_prime)[0][0] \
        if not isinstance(prev, list) else prev[-1][-1][1]
    primes_in_range = sum_primes_in_range(start_idx, end)
    res = [start, end, primes_in_range]

    logger_parser('IN_PROGRESS.EXPERIMENT.fibonacci_counter', 'fib_ranges_sum_reducer range({}) primes sum is {}',
                  [res[:2], res[2]])

    return [res] if not isinstance(prev, list) else prev + [res]


fib_range_primes_sum = reduce(fib_ranges_sum_reducer, sums_to_reduce)
main_result = fib_range_primes_sum
if dimension_start_idx <= 1:
    main_result = [[2, 4, [0, 0, 1]]] + main_result
    if dimension_start_idx < 1:
        main_result = [[1, 2, [0, 0, 1]]] + main_result

logger_parser('END.EXPERIMENT.fibonacci_counter', 'main_result \n{}', [main_result])


# if you want to sum all primes up to
primes_upto = positional_counter_primes.sum() + 1
logger_parser('IN_PROGRESS.EXPERIMENT.fibonacci_counter', 'primes_upto {} is {}', [upto, primes_upto])

fib_total_sum = 0
for sub_total in main_result:
    fib_total_sum += sub_total[-1][-1]

print('fib_total_sum', fib_total_sum, primes_upto)
end_experiment(now, 'fibonacci_counter')
