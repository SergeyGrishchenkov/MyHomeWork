# Create your custom exception named `CustomException`, you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named `logs.txt`.
# Tips: Use __init__ method to extend functionality for saving messages to file

import time
class CustomException(Exception):
    __file_name = 'log.txt'
    def __init__(self, msg):
        self.msg = f'Time: {time.asctime()} exception: {msg}\n'
        self.write_ex(self.msg)

    def write_ex(self, msg):
        with open(self.__file_name, 'a+') as f:
            f.write(msg)

def test_func(l: list):
    result = 0
    try:
        for item in l:
            result += item
    except:
        CustomException(f'Function:{test_func.__name__} - {Exception.__context__.__dir__()}')


list = [1, 2, 3, '7']

test_func(list)
