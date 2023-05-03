from datetime import datetime

from utils.prime_counter import prime_counter


now = datetime.now()

print(prime_counter(100000))
later_time = datetime.now()
difference = later_time - now
print('took {}'.format(difference.total_seconds()))
