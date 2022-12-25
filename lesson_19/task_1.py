# Create your own implementation of a built-in function enumerate, named `with_index`,
# which takes two parameters:
# `iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function
from typing import List


def with_index(iterable, start=0):
    if not isinstance(start, int):
        raise TypeError("Start of enumerate must be INT")
    for item in iterable:
        yield start, item
        start += 1

my_list = [1, 2, 3, 4, 5, '33']

print(f'{"*"*10} Using class enumerate {"*"*20}')
for count, elem in enumerate(my_list, 4):
    print(count, elem)

print(f'{"*"*10} Using own implementation {"*"*20}')
for count, elem in with_index(my_list, 4):
    print(count, elem)
