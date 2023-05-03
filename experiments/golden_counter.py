import os.path
from datetime import datetime

from definitions import ROOT_DIR
from exporters.primes_in_range_exporter import primes_in_range_exporter
from generators.fibonacci import fibonacci_range
from generators.summatory import sums_range
from mappers.primes_in_range_mapper import primes_in_range_mapper
from utils.list_ranges import list_ranges

f_dimension = 44
now = datetime.now()
date_time = now.strftime("%m%d%Y%H%M%S")
csv_file_path = os.path.join(ROOT_DIR, 'dist/golden_counter_{}_{}.csv'.format(f_dimension, date_time))
print(csv_file_path)

fibonacci_nums = fibonacci_range(f_dimension)

fibonacci_sums = sums_range(fibonacci_nums)

fibonacci_sums_ranges = list_ranges(fibonacci_sums)

primes_in_fib_sums_ranges = list(map(primes_in_range_mapper, fibonacci_sums_ranges))

print('fibonacci_nums: {} generated'.format(len(fibonacci_nums)))
print('fibonacci_sums_ranges: {} generated'.format(len(fibonacci_sums_ranges)))
print('primes_in_fib_sums_ranges: {} generated'.format(len(primes_in_fib_sums_ranges)))

primes_in_range_exporter(csv_file_path, fibonacci_nums, primes_in_fib_sums_ranges)

later_time = datetime.now()
difference = later_time - now
print('END took {} seconds'.format(difference.total_seconds()))
