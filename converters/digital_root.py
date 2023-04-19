def digital_root_range(nums):
    return list(map(digital_root, nums))


def digital_root(n):
    if n < 10:
        return n
    n = n%10+digital_root(n//10)
    return digital_root(n)
