# Create a list of dictionaries with name, surname and age of each person.
# Write a python program using lambda function to sort the order of names based on its alphabet sequence.
# Write another program to sort by age. Write result to JSON file.
from functools import wraps

a = [1, 2, 3, 4, 5]


def _pr(f):
    @wraps(f)
    def wr(l):
        print(f'len is {len(l)}')
        f(l)
    return wr

@_pr
def pr(l):
    print(l)


pr(a)
