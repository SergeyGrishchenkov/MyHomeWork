# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку
# для дробів (+, -, /, *) з належною перевіркою й обробкою помилок.
# Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

class Fraction:
    def __new__(cls, *args, **kwargs):
        if args[1] == 0:
            raise ZeroDivisionError("the denominator cannot be equal zero")
        instance = super().__new__(cls)
        return instance

    def __init__(self, nominator: int, denominator: int):
        self.nominator = nominator
        self.denominator = denominator

    @staticmethod
    def reduction(new_nom, new_denom):
        """определяем коэффициент сокращения числителя и знаменателя"""
        den = min(abs(new_nom), abs(new_denom))
        for item in range(den, 0, -1):
            if new_nom % item == 0 and new_denom % item == 0:
                return item
        return 1

    def inter_calc(self, other):
        """промежуточное вычисление для операций + и -"""
        return [self.nominator * other.denominator,
                other.nominator * self.denominator,
                other.denominator * self.denominator]

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('wrong type of argument')
        else:
            items = self.inter_calc(other)
            new_nom = (items[0] + items[1])
            new_denom = items[2]
            reduce = self.reduction(new_nom, new_denom)
        return Fraction((new_nom / reduce), (new_denom / reduce))

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('wrong type of argument')
        else:
            items = self.inter_calc(other)
            new_nom = (items[0] - items[1])
            new_denom = items[2]
            reduce = self.reduction(new_nom, new_denom)
        return Fraction((new_nom / reduce), (new_denom / reduce))

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('wrong type of argument')
        else:
            new_nom = self.nominator * other.nominator
            new_denom = self.denominator * other.denominator
            reduce = self.reduction(new_nom, new_denom)
        return Fraction((new_nom / reduce), (new_denom / reduce))

    def __truediv__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('wrong type of argument')
        else:
            if other.denominator == 0:
                raise ZeroDivisionError("for divide operator the nominator of second fractal cannot be zero")
            new_nom = self.nominator * other.denominator
            new_denom = self.denominator * other.nominator
            reduce = self.reduction(new_nom, new_denom)
        return Fraction((new_nom / reduce), (new_denom / reduce))

    def __eq__(self, other):
        if self.nominator == other.nominator and self.denominator == other.denominator:
            return True
        else:
            return False

def main():
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))
    print("*"*20)
    print(x - y == Fraction(1, 4))
    print("*"*20)
    x = Fraction(2, 5)
    y = Fraction(3, 4)
    print(x * y == Fraction(3, 10))
    print("*"*20)
    x = Fraction(4, 7)
    y = Fraction(2, 5)
    print(x / y == Fraction(10, 7))

if __name__ == "__main__":
    main()

