from datetime import datetime

# from utils.prime_couter_fn import is_prime


# def prime_counter(n: int) -> int:
#     """A Python program to count the number of prime numbers
#     less than a given non-negative number n."""
# 
#     return(sum(1 for i in range(2, n) if is_prime(i)))
from utils.prime_counter_range import prime_counter_range

now = datetime.now()
primes_in_range = prime_counter_range([13, 23])
print(primes_in_range)
later_time = datetime.now()
difference = later_time - now
print('took {}'.format(difference.total_seconds()))
