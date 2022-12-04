# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
from functools import wraps
def arg_rules(type_: type, max_length: int, contains: list):
    def stop_words_decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            truble_list = []
            if type(args[0]) != type_:
                truble_list.append('The argument does not match the rule of type\n')
                print('\n'.join(truble_list))
                return False
            if len(args[0]) > max_length:
                truble_list.append('The argument does not match the rule of maximum length\n')
            for item in contains:
                if item not in args[0]:
                    truble_list.append('The argument does not match the rule of containing symbol ' + str(item) + '\n')
            if len(truble_list) > 0:
                print('\n'.join(truble_list))
                return False
            result = func(*args)
            return result
        return wrap
    return stop_words_decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan(22) is False
assert create_slogan('jofgsdfhfhdsddhngmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'