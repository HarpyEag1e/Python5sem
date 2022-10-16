from math import gcd, copysign

class Rational:
    def __init__(self, x: int = 0, y: int = 1):
        if   y == 0:
            raise ValueError("Denominator can't be zero!")
        elif x == 0:
            self.x = 0
            self.y = 1
        else:
            # gcd - greatest common divisor (наибольший общий делитель)
            # I want my denominator to stay positive
            self.x = int(copysign(1,y)) * x // gcd(x, y)
            self.y = int(copysign(1,y)) * y // gcd(x, y)

    def __str__(self) -> str:
        return f'{self.x}/{self.y}'

    def __repr__(self) -> str:
        return f'Rational({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x * other.y + self.y * other.x
        y = self.y * other.y
        return Rational(x, y)

    def __sub__(self, other):
        x = self.x * other.y - self.y * other.x
        y = self.y * other.y
        return Rational(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Rational(x, y)

    def __truediv__(self, other):
        x = self.x * other.y
        y = self.y * other.x
        return Rational(x, y)

    def __float__(self):
        return self.x / self.y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def from_string(string: str) -> float:
        slash_pos = string.find('/')
        if slash_pos == -1:
            raise ValueError("Wrong format! Must be 'm/n'!")
        elif string[0:slash_pos].lstrip('-').isnumeric() == False:
            raise ValueError("Wrong format (before slash)! Must be 'm/n'!")
        elif string[slash_pos + 1:].lstrip('-').isnumeric() == False:
            raise ValueError("Wrong format (after slash)! Must be 'm/n'!")

        return float(string[0:slash_pos]) / float(string[slash_pos + 1:])


def test_operations():
    assert Rational( 1, 2) + Rational( 1, 2) == Rational( 1, 1)
    assert Rational( 3, 8) - Rational( 1, 4) == Rational( 1, 8)
    assert Rational(-9, 4) * Rational( 2, 3) == Rational(-3, 2)
    assert Rational(-3, 7) / Rational( 2,14) == Rational(-3, 1)

def test_cast_to_float():
    assert float(Rational(3, 4)) == 3/4
    assert float(Rational(3,-9)) == 3/-9

def test_parse_from_string():
    assert Rational.from_string("-5/7") == -5/7
    assert Rational.from_string("4/-9") ==  4/-9


if __name__ == "__main__":
    test_operations()
    test_cast_to_float()
    test_parse_from_string()
