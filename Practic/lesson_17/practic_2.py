class Car:
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        self.__color = color

    def move_forvard(self, speed):
        pass


d = {'22': 77}
r = dict(filter(lambda k: k[0] == '22', d.items()))
print(r)