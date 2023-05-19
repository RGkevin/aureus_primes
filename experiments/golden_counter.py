import os.path
from datetime import datetime

from definitions import ROOT_DIR
from exporters.primes_in_range_exporter import primes_in_range_exporter
from generators.fibonacci import fibonacci_range, fibonacci_gen
from generators.summatory import sums_range
from mappers.primes_in_range_mapper import primes_in_range_mapper
from utils.fibonacci_range_round import fibonacci_range_round
from utils.list_ranges import list_ranges

record = 43
f_dimension_start = 30
f_dimension_end = 32
now = datetime.now()
date_time = now.strftime("%m%d%Y%H%M%S")

print('START start {}, end {}'.format(f_dimension_start, f_dimension_end))

fibonacci_nums = fibonacci_range_round(f_dimension_start, f_dimension_end)
fibonacci_sums = sums_range(f_dimension_start, f_dimension_end, fibonacci_nums)

fibonacci_sums_ranges = list_ranges(fibonacci_sums)

primes_in_fib_sums_ranges = map(primes_in_range_mapper, fibonacci_sums_ranges)
csv_file_path = os.path.join(ROOT_DIR, 'dist/golden_counter_{}-{}_{}.csv'.format(f_dimension_start, f_dimension_end, date_time))
# for primes_sum in primes_in_fib_sums_ranges:
#     print('found: {}'.format(primes_sum))

print('fibonacci_nums: {} generated'.format(f_dimension_end - f_dimension_start + 1))
print('fibonacci_sums_ranges: {} generated'.format(len(fibonacci_sums_ranges)))
# print('primes_in_fib_sums_ranges: {} generated'.format(len(primes_in_fib_sums_ranges)))

primes_in_range_exporter(f_dimension_start, csv_file_path, fibonacci_nums, primes_in_fib_sums_ranges)

later_time = datetime.now()
delta_time = (later_time - now).total_seconds()
print('END took {} seconds'.format(delta_time))
print(csv_file_path)
