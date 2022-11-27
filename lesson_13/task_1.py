# Write a Python program to detect the number of local variables declared in a function.

# TEST CASE OF FUNCTIONS
# 1. contain None
# 2. contain several int variables
# 3. contain several str variables
# 4. contain several int and str variables
# 5. use global and local variables

g_var = 100

def f1():
    pass
    return ('contain None')

def f2():
    a, b, c = 1, 2, 3
    return ('contain 3 int variables')

def f3():
    a, b, c = 'str1', 'str2', 'str3'
    return ('contain 2 str variables')

def f4():
    a, b, c = 1, 2, 'str3'
    return ('contain 2 int 1 str variables')

def f5():
    global g_var

    return ('use global and local variables')