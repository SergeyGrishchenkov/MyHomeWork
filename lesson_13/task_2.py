# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def func_1(x: int):
    def func_2(y: int) -> object:
        """
        :rtype: int
        """
        return x ** y

    return func_2


# two function calls
first = func_1(5)
result = first(3)

print(result)

# one function call
result = func_1(5)(3)

print(result)
