# def sq(a):
#     return a ** 2
#
# def sq1(a):
#     return 'eeeeeee'
#
# tup1 = (1, 2, 3, 4, 5)
# tup2 = tuple(map(lambda x: x+3, tup1))
# print(tup2)
#
# tup2 = tuple(map(sq, tup1))
# print(tup2)
#
# tup2 = tuple(map(sq1, tup1))
# print(tup2)
#
# print(type(range(1, 10, 2)))

tup1 = ('aaaaa', 'bb')
list1 = list(filter(lambda x: len(x) > 3, tup1))
print(list1)