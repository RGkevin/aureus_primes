def nums_initials(nums):
    return list(map(num_initial, nums))


def num_initial(n):
    return n % 10
