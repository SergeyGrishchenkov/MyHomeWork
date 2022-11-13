# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def sqw_divide_number():
    successfully = False
    first_arg = input("Input first number:\n")
    second_arg = input("Input second number:\n")
    try:
        if not first_arg.isdigit() or not second_arg.isdigit():
            raise TypeError('Input arguments are not digit.')
        result = (int(first_arg) ** 2) / int(second_arg)
        successfully = True
        return result
    except ZeroDivisionError:
        print(ZeroDivisionError.__doc__)
    except TypeError:
        print(TypeError.__doc__)
    finally:
        if not successfully:
            print('You should be more careful when entering the value!!!')

def main():
    result = sqw_divide_number()
    print(f'You have such result: {result}')

if __name__ == '__main__':
    main()

