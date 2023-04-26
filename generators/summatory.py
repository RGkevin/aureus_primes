
def sums_range(nums):
    sums = []
    for idx, num in enumerate(nums):
        prev = sums[idx - 1] if idx > 0 else 0
        res = prev + num
        sums.append(res)

    return sums
