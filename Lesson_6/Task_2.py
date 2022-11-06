# Task 2
#
# Exclusive common numbers.
#
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
#
# Constraints: use only while loop and random module to generate numbers

from random import randint

list_test1 = []
list_test2 = []
list_test3 = []
i = 0
while i < 10:
    list_test1.append(randint(1, 10))
    list_test2.append(randint(1, 10))
    i += 1
print(list_test1)
print(list_test2)
for item in list_test1:
    if item in list_test2 and item not in list_test3:
        list_test3.append(item)
print(f'The list, containing the common integers between the 2 initial lists without any duplicates, is :\n {list_test3}')

