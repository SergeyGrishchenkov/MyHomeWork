# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
class Mathematician:
    def square_nums(self, my_list: list):
        try:
            return list(map(lambda i: i**2, my_list))
        except TypeError("Non integer members"):
            return my_list
        except Exception("Truble!"):
            return my_list

    def remove_positives(self, my_list: list):
        try:
            return list(filter(lambda i: i <= 0, my_list))
        except TypeError("Non integer members"):
            return my_list
        except Exception("Truble!"):
            return my_list

    def filter_leaps(self, my_list: list):
        try:
            return list(filter(lambda i: i % 4 == 0 and i % 100 != 0, my_list))
        except TypeError("Non integer members"):
            return my_list
        except Exception("Truble!"):
            return my_list


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
print(m.square_nums([7, 11, 5, 4]))
print('*'*20)
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
print(m.remove_positives([26, -11, -8, 13, -90]))
print('*'*20)
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
