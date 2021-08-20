from copy import deepcopy


class Number:

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __eq__(self, other):
        pass


class Rational(Number):

    def __init__(self, p, q):
        assert q != 0, ZeroDivisionError
        assert type(p) == int and type(q) == int, TypeError
        self.__p = p
        self.__q = q

    def __add__(self, other):
        if isinstance(other, Integer):
            other = other.to_rational(1)

        self.__p = self.__p * other.__q + self.__q * other.__p
        self.__q = self.__q * other.__q
        # return Rational(m, n)

    def __sub__(self, other):
        if isinstance(other, Integer):
            other = other.to_rational(1)

        self.__p = self.__p * other.__q - self.__q * other.__p
        self.__q = self.__q * other.__q

    def __mul__(self, other):
        if isinstance(other, Integer):
            other = other.to_rational(1)

        self.__p = self.__p * other.__p
        self.__q = self.__q * other.__q

    def __truediv__(self, other):
        if isinstance(other, Integer):
            other = other.to_rational(1)

        self.__p = self.__p * other.__q
        self.__q = self.__q * other.__p

    def __eq__(self, other):
        if isinstance(other, Integer):
            other = other.to_rational(1)

        return self.__p / self.__q == other.__p / other.__q

    def __str__(self):
        return f'{self.__p}/{self.__q}'

    @staticmethod
    def Addition(r1, r2):
        r1 = deepcopy(r1)
        r1 + r2
        return r1

    @staticmethod
    def Subtraction(r1, r2):
        r1 = deepcopy(r1)
        r1 - r2
        return r1

    @staticmethod
    def Multiplication(r1, r2):
        r1 = deepcopy(r1)
        r1 * r2
        return r1

    @staticmethod
    def Division(r1, r2):
        r1 = deepcopy(r1)
        r1 / r2
        return r1

    @staticmethod
    def operations(r1, r2):
        r1 = deepcopy(r1)
        return f'{r1} + {r2} = {Rational.Addition(r1, r2)}\n' \
               f'{r1} - {r2} = {Rational.Subtraction(r1, r2)}\n' \
               f'{r1} x {r2} = {Rational.Multiplication(r1, r2)}\n' \
               f'{r1} / {r2} = {Rational.Division(r1, r2)}'


class Integer(Number):
    def __init__(self, number):
        assert type(number) == int, TypeError
        self.__number = number

    def __add__(self, other):
        self.__number += other.__number

    def __sub__(self, other):
        self.__number -= other.__number

    def __mul__(self, other):
        self.__number *= other.__number

    def __truediv__(self, other):
        new_number = self.__number / other.__number
        assert new_number == int(new_number), f'{new_number} does not belong to Z'
        self.__number //= other.__number

    def to_rational(self, q):
        return Rational(self.__number, q)

    def __str__(self):
        return f'{self.__number}'


def tst_operations():
    r1, r2 = Rational(1, 10), Rational(-2, 5)
    orig_r1, orig_r2 = r1, r2
    Rational.Addition(r1, r2)
    Rational.Subtraction(r2, r1)

    assert r1 == orig_r1 and r2 == orig_r2, 'Something\'s wrong!'


if __name__ == '__main__':
    q1 = Rational(-11, 7)
    q2 = Rational(8, 5)
    n1 = Integer(6)
    n2 = Integer(3)


# Tests
    tst_operations()
    print(q1, '\n')
    print(Rational.operations(q1, q2))
    print(Rational.Addition(q1, n1), '\n')  # With Integer
    print(q1)  # Shouldn't change

    print(n1)
    n1 / n2  # Inplace as required
    print(n1)
