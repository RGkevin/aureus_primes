from typing import List


def fibonacci_gen(end):
    res = [0, 1]
    if end <= 2:
        return res

    for i in range(end - 2):
        curr_index = i + 2
        sum_res = res[curr_index - 2] + res[curr_index - 1]
        res.append(sum_res)

    return res


def fibonacci_range(start_dim, end_dim, fib_nums) -> List[int]:
    if start_dim > end_dim or start_dim == end_dim:
        raise Exception('Start {} dimension should be less than End {}'.format(start_dim, end_dim))

    # fib_nums = fibonacci_gen(end_dim + 1)
    return [fib_nums[len(fib_nums) - 1]] if start_dim == end_dim else fib_nums[start_dim:end_dim + 1]
