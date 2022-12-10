class Point:
    GL = 9

    @classmethod
    def my_st(cls):
        return cls.GL < 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def my_s(x, v):
        return x + v

s = Point(1, 2)
