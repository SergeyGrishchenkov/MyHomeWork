# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку
# для дробів (+, -, /, *) з належною перевіркою й обробкою помилок.
# Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

class Fraction:
    def __init__(self, nominator: int, denominator: int):
        self.nominator = nominator
        self.denominator = denominator

    @staticmethod
    def reduction(new_nom, new_denom):
        den = min(abs(new_nom), abs(new_denom)) // 2
        for item in range(den, 0, -1):
            if new_nom % item == 0 and new_denom % item == 0:
                return item
        return 1

    def inter_calc(self, other):
        return [self.nominator * other.denominator,
                other.nominator * self.denominator,
                other.denominator * self.denominator]

    def __add__(self, other):
        items = self.inter_calc(other)
        new_nom = (items[0] + items[1])
        new_denom = items[2]
        reduce = self.reduction(new_nom, new_denom)
        return Fraction((new_nom / reduce), (new_denom / reduce))

    def __sub__(self, other):
        items = self.inter_calc(other)
        new_nom = (items[0] - items[1])
        new_denom = items[2]
        reduce = self.reduction(new_nom, new_denom)
        return Fraction((new_nom / reduce), (new_denom / reduce))

    def __mul__(self, other):
        new_nom = self.nominator * other.nominator
        new_denom = self.denominator * other.denominator
        reduce = self.reduction(new_nom, new_denom)
        return Fraction((new_nom / reduce), (new_denom / reduce))

    def __truediv__(self, other):
        new_nom = self.nominator * other.denominator
        new_denom = self.denominator * other.nominator
        reduce = self.reduction(new_nom, new_denom)
        return Fraction((new_nom / reduce), (new_denom / reduce))


f1 = Fraction(4, 7)
f2 = Fraction(2, 5)
f3 = f1 / f2
print(f3.__dict__)

