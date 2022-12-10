# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку
# для дробів (+, -, /, *) з належною перевіркою й обробкою помилок.
# Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

class Fraction:
    def __init__(self, nominator: int, denominator: int):
        self.nominator = nominator
        self.denominator = denominator

    def reduction(self):
        den = min(self.nominator, self.denominator) // 2


    def intermediate_calculation(self, other):
        return [self.nominator * other.denominator,
                other.nominator * self.denominator,
                other.denominator * self.denominator,
                (self.denominator if self.denominator < other.denominator else other.denominator)]

    def __add__(self, other):
        items = self.intermediate_calculation(other)
        return Fraction((items[0] + items[1]) / items[3], items[2] / items[3])

    def __sub__(self, other):
        items = self.intermediate_calculation(other)
        return Fraction((items[0] - items[1]) / items[3], items[2] / items[3])

    def __mul__(self, other):
        return Fraction()

    def __truediv__(self, other):
        pass

f1 = Fraction(3, 8)
f2 = Fraction(5, 4)
f3 = f1 - f2
print(f3.__dict__)