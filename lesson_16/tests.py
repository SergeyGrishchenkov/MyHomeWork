import itertools

first_ten = (itertools.islice((x for x in range(1000000000) if x % 2 == 0), 10))

print(list(first_ten))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]