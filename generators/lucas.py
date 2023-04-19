
def lucas_range(end):
    res = [2, 1]
    if end <= 2:
        return res

    for i in range(end - 2):
        curr_index = i + 2
        sum_res = res[curr_index - 2] + res[curr_index - 1]
        res.append(sum_res)

    return res
