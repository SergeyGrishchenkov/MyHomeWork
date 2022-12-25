# Write a class TypeDecorators which has several methods for
# converting results of functions to a specified type (if it's possible):
# methods:
# to_int
# to_str
# to_bool
# to_float
import functools

def singleton(cls):
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


class TypeDecorators:

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.f_result = None


    @classmethod
    def to_int(self, *args, **kwargs):
        print('w')

    @singleton
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


@TypeDecorators
def do_nothing(string: str):
    return string


# @TypeDecorators.to_bool
# def do_something(string: str):
#     return string

s = do_nothing('25')
print(type(s))
# assert do_nothing('25') == 25

# assert do_something('True') is True