
def fibonacci_range(end):
    res = [0, 1]
    if end <= 2:
        return res

    for i in range(end - 2):
        curr_index = i + 2
        sum_res = res[curr_index - 2] + res[curr_index - 1]
        res.append(sum_res)

    return res


def fibonacci_sums(fib_nums):
    res = []
    for idx, x in enumerate(xs):
        print(idx, x)

    return fib
