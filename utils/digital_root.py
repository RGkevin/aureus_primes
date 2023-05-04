def digital_root(n: int) -> int:
    n_str = str(n)
    list_of_number = list(map(int, n_str.strip()))
    return sum(list_of_number)