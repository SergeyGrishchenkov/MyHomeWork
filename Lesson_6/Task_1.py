# Task 1
#
# The greatest number
#
# Write a Python program to get the largest number from a list of random numbers with the length of 10
#
# Constraints: use only while loop and random module to generate numbers

from random import randint

list_test = []
i = 0
while i < 10:
    list_test.append(randint(1, 20))
    i += 1
print(list_test)

max_in_list = max(list_test)
print(f'The maximum in list, which was printed before, is :\n {max_in_list}')