import csv


def primes_in_range_exporter(start, file_path, fibonacci_nums, primes_in_range):
    header = [
        'index', 'f_num', 'f_sum', 'range_start', 'range_end', 'n_nums_in_range', 'primes_in_range', 'index',
        'n.len / p.len', 'f_dim_i', 'increment']
    data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for p_range in primes_in_range:
        index = 0
        f_num = fibonacci_nums[index]
        f_sum = p_range[0]
        n_nums_in_range = p_range[1]
        p_in_range = p_range[-1]
        np_division = (n_nums_in_range / p_in_range) if p_in_range != 0 else 0
        f_sum_range = p_range[2]
        display_index = index + start
        increment = np_division - (data[index - 1][8] if index > 1 else np_division)

        data += [
            [display_index, f_num, f_sum, f_sum_range[0], f_sum_range[-1], n_nums_in_range, p_in_range, display_index,
             np_division, display_index, increment]]

    with open(file_path, 'w') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
        f.close()
