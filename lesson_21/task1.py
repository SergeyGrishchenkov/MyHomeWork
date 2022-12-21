# Create your own class, which can behave like a built-in function `open`.
# Also, you need to extend its functionality with counter and logging. Pay special attention to the implementation
# of `__exit__` method, which has to cover all the requirements to context managers mentioned here:
from contextlib import contextmanager

import datetime as dt


class ContextTextFile:
    __act_list = ['r', 'w', 'a']
    __counter = 0
    __log_file_name = 'lof.txt'

    @classmethod
    def get_count(cls):
        return cls.__counter

    @classmethod
    def set_counter(cls):
        cls.__counter += 1

    def __init__(self, file_name, type_act):
        if type_act not in self.__act_list:
            raise ValueError('Wrong additional attribute')
        self.err = None
        self.__file_name = file_name
        self.__type_act = type_act
        self.f = None

    def __enter__(self):
        try:
            self.f = open(self.__file_name, self.__type_act)
            return self.f
        except FileNotFoundError:
            self.err = FileNotFoundError

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.set_log(self.err, exc_val)
        if self.err is not None:
            print(self.err.__doc__)
            return True
        self.f.close()
        if exc_type is not None:
            raise exc_val
        ContextTextFile.set_counter()
        return True

    def set_log(self, err=None, exc_type=None):
        with open(ContextTextFile.__log_file_name, 'a') as lf:
            if err is None and exc_type is None:
                lf.write(
                    f"Good: file named \"{self.__file_name}\" was opened in mode \"{self.__type_act}\" "
                    f"at : {dt.datetime.now()}\n")
            else:
                truble_str = ("" if err is None else err.__doc__ + " / ") + ("" if exc_type is None else exc_type.args[0])
                lf.write(
                    f"Bad: file named \"{self.__file_name}\" it was tried to be open in mode \"{self.__type_act}\" "
                    f"at : {dt.datetime.now()}, but it had a truble: {truble_str}\n")


def main():
    f_name = 'test.txt'
    with ContextTextFile(f_name, 'w') as f:
        f.write('77777')

    print(f'The counter value is: {ContextTextFile.get_count()}')

    with ContextTextFile(f_name, 'r') as f:
        result = f.readlines()
        print(result)

    print(f'The counter value is: {ContextTextFile.get_count()}')

    with ContextTextFile(f_name, 'a') as f:
        result = f.write('\n77777')
        print(result)

    print(f'The counter value is: {ContextTextFile.get_count()}')




if __name__ == '__main__':
    main()
