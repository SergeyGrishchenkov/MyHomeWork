# Write a class TypeDecorators which has several methods for
# converting results of functions to a specified type (if it's possible):
# methods:
# to_int
# to_str
# to_bool
# to_float
#---

class TypeDecorators:
    @staticmethod
    def to_int(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except:
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return str(result)
            except:
                return result
        return wrapper

    @staticmethod
    def to_bool(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return bool(result)
            except:
                return result
        return wrapper

    @staticmethod
    def to_float(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except:
                return result
        return wrapper

@TypeDecorators.to_int
def do_int_from_str(string: str):
    return string

@TypeDecorators.to_bool
def do_bool_from_smth(item):
    return item

@TypeDecorators.to_str
def do_str_from_smth(item):
    return item

@TypeDecorators.to_float
def do_float_from_smth(item):
    return item


assert do_int_from_str('25') == 25
assert do_int_from_str(25.5) == 25
assert do_int_from_str(True) == 1.0
assert do_int_from_str('ttt') == 'ttt'

assert do_bool_from_smth('True') is True
assert do_bool_from_smth(0) is False
assert do_bool_from_smth('ttt') is True

assert do_str_from_smth(0) == '0'
assert do_str_from_smth(4.2) == '4.2'
assert do_str_from_smth('ttt') == 'ttt'

assert do_float_from_smth('4.2') == 4.2
assert do_float_from_smth(4) == 4.0
assert do_float_from_smth('ttt') == 'ttt'
