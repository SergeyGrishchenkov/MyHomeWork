# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
from functools import wraps

stop_list = ['pepsi', 'BMW']


def stop_words(words: list):
    def stop_words_decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            result = func(*args)
            for item in words:
                result =result.replace(item, '*')
            return result
        return wrap
    return stop_words_decorator

@stop_words(stop_list)
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print(create_slogan("Steve"))
