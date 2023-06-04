import logging
import os
import sys
from datetime import datetime

from definitions import ROOT_DIR
from generators.prime_range_generator import positional_primes_generator
from generators.summatory import sums_range
from utils.end_experiment import end_experiment
from utils.fibonacci_range_round import fibonacci_range_round
from utils.logger_parser import logger_parser
from utils.logging_setup import logging_setup
from utils.prime_range_generator import prime_range_generator

logging_setup()

dimension_start_idx = 5
dimension_end_idx = 10
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
positional_primes = positional_primes_generator(upto)
primes_upto = positional_primes.sum() + 1

logger_parser('IN_PROGRESS.EXPERIMENT.fibonacci_counter', 'primes_upto {} is {}', [upto, primes_upto])

end_experiment(now, 'fibonacci_counter')
