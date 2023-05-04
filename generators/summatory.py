
def sums_range(start, end, nums):
    if len(nums) == 1:
        raise Exception('nums should have more than 1 element {}'.format(nums))
    sums = []
    for idx, num in enumerate(nums):
        prev = sums[idx - 1] if idx > 0 else 0
        res = prev + num
        sums.append(res)

    return sums[start: end + 1]
