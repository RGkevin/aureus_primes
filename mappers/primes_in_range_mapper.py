import sympy

from utils.prime_counter_range import prime_counter_range


def primes_in_range_mapper(num_range):
    start = num_range[0]
    end = num_range[1]
    p_in_range = prime_counter_range([start, end])

    print('primes_in_range_mapper num_range {} primes: {}'
          .format(num_range, p_in_range))

    n_nums_in_range = num_range[-1] - num_range[0] + 1
    return [num_range[1], n_nums_in_range, num_range, p_in_range]
