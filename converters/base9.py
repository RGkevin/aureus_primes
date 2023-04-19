def nums_base9(nums):
    return list(map(num_base9, nums))


def num_base9(n):
    return n % 9
