# Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

list_test = [(item, pow(item, 2)) for item in range(1, 11)]
print(list_test)