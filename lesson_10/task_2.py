# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def sqw_divide_number(a, b):
    successfully = False
    try:
        result = (float(a) ** 2) / float(b)
        successfully = True
        return result
    except ZeroDivisionError:
        #print(ZeroDivisionError.__doc__)
        print('')
    except TypeError:
        #print(TypeError.__doc__)
        print('')
    except:
        print('--')
    finally:
        if not successfully:
            print('You should be more careful when entering the value!!!')

def main():
    first_arg = input("Input first number:\n")
    second_arg = input("Input second number:\n")
    result = sqw_divide_number(first_arg, second_arg)
    print(f'You have such result: {result}')

if __name__ == '__main__':
    main()

