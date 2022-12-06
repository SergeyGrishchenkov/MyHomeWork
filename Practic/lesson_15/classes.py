import accessify as a

class Test:
    a = 5
    b = 6
    def __new__(cls):

    def __init__(self, x=0, y=0):
        print('gdgjhk')
        self.x = x
        self.y = y

    def __del__(self):
        print('finish')

x = Test()
print(x.__dict__)