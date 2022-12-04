# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
from functools import wraps


def logger(func):
    @wraps(func)
    def warp(*args):
        arguments = ', '.join(map(str, args))
        print(f'{func.__name__} called with {arguments}')
        result = func(*args)
        return result

    return warp


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


result1 = add(2, 2)
print(f'result is: {result1}')
result2 = square_all(2, 3, 4)
print(f'result is: {result2}')
