from functools import reduce


# generate a list of ranges, edges included
def list_ranges(nums):
    ranges = reduce(list_range_reducer, nums)
    return ranges


def list_range_reducer(prev, current):
    return [[prev + 1, current]] if not isinstance(prev, list) else prev + [[prev[-1][-1] + 1, current]]
