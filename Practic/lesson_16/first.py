import self as self


class Geom:
    name = "Geom"
    def set_attr(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def drow(self):
        print("simple")

class Rect(Geom):
    name = "Rect"
    def drow(self):
        print("rectangle")

# r = Rect()
# r.set_attr(1,1,2,2)
# print(r.__dict__)
# print(r.name)
# r.drow()
#--------
# my_list = [item for item in range(0, 6)]
# print('\n'.join(map(str, my_list)))
# import datetime
#
# x = datetime.datetime.now()
# print(type(repr(x)))
# print(type(str(x)))
#
# print(eval(repr(x)))
# print(str(x))
#
# help(eval)

class SC:
    def pr(self):
        print(type(super()))
        print('sdf')

    def ref(self):
        self.do_act()

class Sub(SC):

    pass

p = Sub()
p.pr()
