# Write a class TypeDecorators which has several methods for
# converting results of functions to a specified type (if it's possible):
# methods:
# to_int
# to_str
# to_bool
# to_float

class TypeDecorators:
    pass


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True