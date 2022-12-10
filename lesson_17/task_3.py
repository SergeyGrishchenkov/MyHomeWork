# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку
# для дробів (+, -, /, *) з належною перевіркою й обробкою помилок.
# Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

class Fraction:
    def __init__(self, nominator: int, denominator: int):
        self.nominator = nominator
        self.denominator = denominator

    def __add__(self, other):
        nominator_1 = self.nominator * other.denominator
        nominator_2 = other.nominator * self.denominator
        denominator_common = other.denominator * self.denominator
        return Fraction((nominator_1 + nominator_2) / (self.denominator if self.denominator < other.denominator else other.denominator), denominator_common / (self.denominator if self.denominator < other.denominator else other.denominator))

f1 = Fraction(3, 8)
f2 = Fraction(5, 4)
f3 = f1 + f2
print(f3.__dict__)