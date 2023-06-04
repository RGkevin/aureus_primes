import math
import numpy


def positional_primes_generator(upto=1000000):
    max_prime_idx = int(math.sqrt(upto)) // 2
    print('positional_primes_generator.upto {} max_prime_idx {}'.format(upto, max_prime_idx))

    possible_primes = numpy.arange(3, upto + 1, 2)
    positional_primes = numpy.ones((upto - 1) // 2, dtype=bool)
    # print('positional_primes_generator.possible_primes \n', possible_primes)
    factors_range = possible_primes[:max_prime_idx]
    # print('positional_primes_generator.factors_range', factors_range)
    for factor in factors_range:
        half_factor_idx = (factor - 2) // 2
        half_factor_is_prime = positional_primes[half_factor_idx]
        # print('positional_primes_generator.half_factor_idx {} half_factor_is_prime {}'.format(half_factor_idx,
        #                                                                                       half_factor_is_prime))
        if half_factor_is_prime:
            composites_start_idx = (factor * 3 - 2) // 2
            # print('positional_primes_generator.composites_start_idx {} every {}'.format(composites_start_idx, factor))
            positional_primes[composites_start_idx::factor] = False
        # print('positional_primes_generator.positional_primes \n', positional_primes)

    return positional_primes
