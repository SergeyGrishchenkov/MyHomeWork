
# •Create a Set
# •Add elements
# •Remove elements (remove(), discard(), clear(), pop())
# •Union and Intersection
# •Difference of sets
# •Copying
# •Iterating
# •Find maximum from set of ints (отредактировано)

# #Яыное создание
# test1 = {1,2,3,4,5,4}
# print(test1)
# #Через конструктор
# st = 'dsgtrt'
# test2 = set(st)
# print(test2)

# #
# first_set = {1, 2, 3, 4, 5}
# first_set_2 = {1, 2, 3, 4, 6}
# # print(first_set)
# # print(first_set_2)
# # first_set.add((1, 2, 3))
# # print(first_set)
#
# first_set.discard(9) # discard игнорирует элемент в множестве
# first_set.remove(5) # remove удаляет элемент  в множестве
# print(first_set)
# item_pop = first_set.pop()
# print(item_pop)
# print(first_set)
# first_set.add(item_pop)
# print(first_set)
# print(first_set)
# first_set_2.clear()
# print(first_set_2)
# print(first_set_2)

# •Union and Intersection
# set1 = {1, 2, 3, 4, 98, 11, 23, 4}
# set2 = {5, 6, 7, 4, 8, 98}
# set3 = set1.union(set2) #объединение
# print(set1)
# print(set2)
# print(set3)
# set3 = set1 | set2  #объединение
# set3 = set1 & set2  #пересечение
# set4 = set1 .intersection(set2)  #пересечение
# print(set1)
# print(set2)
# print(set3)
# print(set4)

# •Difference of sets

# set1 = {222, 1, 2, 3, 4}
# # set2 = {3, 4, 5, 6, 7, 4, 8}
# # set4 = set1.difference(set2)
# # set5 = set2.difference(set1)
# # print(set4, set5)
#
#
# #Copying
# # set3 = set1.copy()
# # #set1.add(105)
# # print(set1, set3)
#
#
# #Iterating
# for i in set1:
#     print(i)
#
# #Find maximum from set of ints
# print(max(set1))

a = frozenset([0, 1, 2, 3, 4])
# The following is not allowed:
a.add(5)
# a.remove(1)
# a.discard(1)
# a.clear()
# Also no update methods are allowed:
# a.update([1,2,3])
# Other set operations work
odds = frozenset({1, 3, 5, 7, 9})
evens = frozenset({0, 2, 4, 6, 8})
print(odds.union(evens))
print(odds.intersection(evens))
print(odds.difference(evens))

