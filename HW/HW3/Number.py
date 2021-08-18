
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

        m = self.__p * other.__q + self.__q * other.__p
        n = self.__q * other.__q
        return Rational(m, n)

    def __sub__(self, other):
        if isinstance(other, Integer):
            other = other.to_rational(1)

        m = self.__p * other.__q - self.__q * other.__p
        n = self.__q * other.__q
        return Rational(m, n)

    def __mul__(self, other):
        if isinstance(other, Integer):
            other = other.to_rational(1)

        m = self.__p * other.__p
        n = self.__q * other.__q
        return Rational(m, n)

    def __truediv__(self, other):
        if isinstance(other, Integer):
            other = other.to_rational(1)

        m = self.__p * other.__q
        n = self.__q * other.__p
        return Rational(m, n)

    def __eq__(self, other):
        if isinstance(other, Integer):
            other = other.to_rational(1)

        return self.__p / self.__q == other.__p / other.__q

    def __str__(self):
        return f'{self.__p}/{self.__q}'

    @staticmethod
    def operations(r1, r2):
        return f'{r1} + {r2} = {r1 + r2}\n' \
               f'{r1} - {r2} = {r1 - r2}\n' \
               f'{r1} x {r2} = {r1 * r2}\n' \
               f'{r1} / {r2} = {r1 / r2}'


class Integer(Number):
    def __init__(self, number):
        assert type(number) == int, TypeError
        self.__number = number

    def __add__(self, other):
        return Integer(self.__number + other.__number)

    def __sub__(self, other):
        return Integer(self.__number - other.__number)

    def __mul__(self, other):
        return Integer(self.__number * other.__number)

    def __truediv__(self, other):
        pass

    def to_rational(self, q):
        return Rational(self.__number, q)

    def __str__(self):
        return f'{self.__number}'


if __name__ == '__main__':
    q1 = Rational(11, 7)
    q2 = Rational(8, 5)
    n1 = Integer(4)

    print(q1.operations(q1, q1), '\n')
    print(q1.operations(q1, n1))  # Supports only operations with INT from left
