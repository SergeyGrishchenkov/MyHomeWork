# import math
# from functools import wraps
#
# # def get_h(h):
# #     def get_r(r):
# #         return math.pi * r ** 2 * h
# #     return get_r
# #
# # res = get_h(10)
# # print(res(5))
#
#
# def first_dec(st = 1):
#     """my first dec"""
#     def second_dec(func):
#         @wraps(func)
#         def wrap(*agrs, **kwargs):
#             print('asgdgsh')
#             args1 = []
#             for item in agrs:
#                 args1.append(item * st)
#             return(func(*tuple(item for item in args1 ), **kwargs))
#             print('eeee')
#         return wrap
#     return second_dec
#
#
# @first_dec(10)
# def my_test(a, b):
#     return a + b
#
# print(my_test(2, 3))
# persona_dict = dict(first_name='', last_name='', full_name='', phone_numbers='', state='', city='')
# d1 = dict(_1='1', _2='2')
# d2 = dict(_1='1', _2=2)
# print(d1 == d2)
# print(d1)
# d1[3] = 33
# print(d1)
f = open('t.txt', 'w')
f.readable()
print(f.readlines())

# print(issubclass(f, _io.TextIOWrapper))

