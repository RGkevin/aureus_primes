import math
from datetime import datetime

import numpy

from generators.prime_range_generator import positional_primes_generator
from utils.possible_primes import possible_primes
from utils.prime_counter import prime_counter


now = datetime.now()
fromTo = 50000
upto = 32951280098

max_prime_idx = int(math.sqrt(upto)) // 2
possible_primes_calculated = possible_primes(upto)
positional_counter_primes = numpy.ones((upto - 1) // 2, dtype=bool)
positional_primes_generator(possible_primes_calculated, positional_counter_primes, max_prime_idx)

total_primes = positional_counter_primes.sum() + 1
print('total_primes upto {} is {}'.format(upto, total_primes))

later_time = datetime.now()
difference = later_time - now
print('took {}'.format(difference.total_seconds()))
