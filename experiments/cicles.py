import datetime
import math
import random

from converters.base9 import nums_base9
from converters.digital_root import digital_root_range
from converters.initials import nums_initials
from generators.fibonacci import fibonacci_range
from generators.lucas import lucas_range
from generators.summatory import sums_range

fibonacci_nums = fibonacci_range(61)
fibonacci_sums = sums_range(fibonacci_nums)
fibonacci_initials = nums_initials(fibonacci_nums)
fibonacci_roots = digital_root_range(fibonacci_nums)
fibonacci_base9 = nums_base9(fibonacci_nums)

# print(fibonacci_nums)
print(fibonacci_sums)
print(fibonacci_initials)
print(fibonacci_roots)
print(fibonacci_base9)

# digital root

# base 10

# base 5

lucas_nums = lucas_range(10)
print(lucas_nums)
