import os.path
from datetime import datetime

from definitions import ROOT_DIR
from exporters.primes_in_range_exporter import primes_in_range_exporter
from generators.fibonacci import fibonacci_range, fibonacci_gen
from generators.summatory import sums_range
from mappers.primes_in_range_mapper import primes_in_range_mapper
from utils.list_ranges import list_ranges

f_dimension_start = 15
f_dimension_end = 20
now = datetime.now()
date_time = now.strftime("%m%d%Y%H%M%S")

fib_nums = fibonacci_gen(f_dimension_end + 1)
fibonacci_nums = fibonacci_range(f_dimension_start, f_dimension_end, fib_nums)

fibonacci_sums = sums_range(f_dimension_start, f_dimension_end, fib_nums)

fibonacci_sums_ranges = list_ranges(fibonacci_sums)

primes_in_fib_sums_ranges = list(map(primes_in_range_mapper, fibonacci_sums_ranges))

later_time = datetime.now()
delta_time = (later_time - now).total_seconds()
csv_file_path = os.path.join(ROOT_DIR, 'dist/golden_counter_{}-{}_s{}_{}.csv'.format(f_dimension_start, f_dimension_end, round(delta_time), date_time))

print('fibonacci_nums: {} generated'.format(f_dimension_end - f_dimension_start + 1))
print('fibonacci_sums_ranges: {} generated'.format(len(fibonacci_sums_ranges)))
print('primes_in_fib_sums_ranges: {} generated'.format(len(primes_in_fib_sums_ranges)))

primes_in_range_exporter(f_dimension_start, csv_file_path, fibonacci_nums, primes_in_fib_sums_ranges)

print('END took {} seconds'.format(delta_time))
print(csv_file_path)
