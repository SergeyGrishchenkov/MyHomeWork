# Extracting numbers.
#
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5,
# and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

list_test1 = [item for item in range(1, 100)]
list_test2 = []

i = 0
while i < len(list_test1):
    if list_test1[i] % 7 == 0 and list_test1[i] % 5 != 0:
        list_test2.append(list_test1[i])
    i +=1
print(list_test1)
print(list_test2)
