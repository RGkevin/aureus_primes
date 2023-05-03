import csv


def primes_in_range_exporter(file_path, fibonacci_nums, primes_in_range):
    header = [
        'index', 'f_num', 'f_sum', 'range_start', 'range_end', 'n_nums_in_range', 'primes_in_range', 'index', 'n.len / p.len']
    data = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for idx, p_range in enumerate(primes_in_range):
        index = idx + 1
        f_num = fibonacci_nums[index]
        f_sum = p_range[0]
        n_nums_in_range = p_range[1]
        p_in_range = p_range[-1]
        np_division = (n_nums_in_range / p_in_range) if p_in_range != 0 else 0
        f_sum_range = p_range[2]
        data += [[index, f_num, f_sum, f_sum_range[0], f_sum_range[-1], n_nums_in_range, p_in_range, index, np_division]]

    with open(file_path, 'w') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
        f.close()