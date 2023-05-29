import os.path
from datetime import datetime

from definitions import ROOT_DIR
from exporters.primes_in_range_exporter import primes_in_range_exporter
from generators.fibonacci import fibonacci_range, fibonacci_gen
from generators.summatory import sums_range
from mappers.primes_in_range_mapper import primes_in_range_mapper
from utils.fibonacci_range_round import fibonacci_range_round
from utils.list_ranges import list_ranges
from utils.prime_range_generator import prime_range_generator

f_dimension_start = 42
f_dimension_end = 43
now = datetime.now()

date_time = now.strftime("%m%d%Y%H%M%S")
# fibonacci_nums = fibonacci_range_round(f_dimension_start, f_dimension_end)

# print('Fibonacci dimension start {}, end {}'.format(f_dimension_start, f_dimension_end))
# print('Fibonacci nums {}'.format(fibonacci_nums))
# fibonacci_sums = sums_range(f_dimension_start, f_dimension_end, fibonacci_nums)

# fibonacci_sums_ranges = list_ranges(fibonacci_sums)

# print(fibonacci_sums_ranges[-1])

# primes_below = prime_range_generator(fibonacci_sums_ranges[-1][0])
# primes_upto = prime_range_generator(fibonacci_sums_ranges[-1][-1])
upto = 32951280098
print('START COUNTER UPTO {}'.format(upto))
primes_upto = prime_range_generator(upto)

print('PRIMES upto {} is {}'.format(upto, len(primes_upto)))

later_time = datetime.now()
delta_time = (later_time - now).total_seconds()
print('END took {} seconds'.format(delta_time))
