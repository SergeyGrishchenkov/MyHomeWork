# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except state­ment to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def oops(type_error):
    raise type_error


def check_oops(test_case_tuple: object) -> object:
    for case in test_case_tuple:
        print(f'We raise exception {case} and catch the certain IndexError')
        try:
            oops(case)
        except IndexError:
            print(f'Congratulation!!! We have just caught:\n {IndexError.__doc__}\n\n')


def main():
    test_case_tuple = (IndexError, KeyError)
    check_oops(test_case_tuple)


if __name__ == '__main__':
    main()
