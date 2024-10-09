import math
import dataclasses

# @dataclasses.dataclass(frozen=True)
class Fraction:


    def __init__(self, numerator: int, denominator: int):
        self.num = numerator

        if denominator == 0:
            raise ZeroDivisionError
        else:
            self.denom = denominator
        self.simplify()

    def simplify(self):
        gcd_2 = math.gcd(self.num, self.denom)
        self.num //= gcd_2
        self.denom //= gcd_2

        if self.num < 0 and self.denom < 0:
            self.num = -1 * self.num
            self.denom = -1 * self.denom

        if self.denom < 0 and self.num > 0:
            self.denom = -1 * self.denom
            self.num = -1 * self.num



    def __str__(self) -> str:
        if self.num > self.denom:
            temp = None
            temp = self.num // self.denom
            self.num = self.num - temp * self.denom
            return f"{temp}, {self.num} / {self.denom}"

        elif self.num < 0 and self.num < self.denom:
            self.num = -1 * self.num
            return f"- {self.num} / {self.denom} "

        elif self.num == 0:
            return "0"

        elif (self.num < 0 < self.denom) or (self.num > 0 > self.denom):
            if self.num > self.denom:
                temp = None
                temp = self.num // self.denom
                self.num = self.num - temp * self.denom
                return f"- {temp}, {self.num} / {self.denom}"
            return f"- {self.num} / {self.denom}"

        elif self.num < 0 and self.denom < 0:
            if self.num > self.denom:
                temp = None
                temp = self.num // self.denom
                self.num = self.num - temp * self.denom
                return f"- {temp}, {self.num} / {self.denom}"
            return f"{self.num} / {self.denom}"

        return f"{self.num} / {self.denom}"

    def __repr__(self) -> str:
        return f"Fraction {self.num} / {self.denom}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Second argument must be Fraction type")
        temp = math.lcm(self.denom, other.denom)
        new_num = (temp // self.denom) * self.num + (temp // other.denom) * other.num
        new_denom = temp
        self.simplify()
        return Fraction(new_num, new_denom)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Second argument must be Fraction type")
        temp = math.lcm(self.denom, other.denom)
        new_num = (temp // self.denom) * self.num - (temp // other.denom) * other.num
        new_denom = temp
        self.simplify()
        return Fraction(new_num, new_denom)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Second argument must be Fraction type")
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        self.simplify()
        return Fraction(new_num, new_denom)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Second argument must be Fraction type")
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        self.simplify()
        return Fraction(new_num, new_denom)

    def __eq__(self, other):
        self.simplify()
        if not isinstance(other, Fraction):
            return False
        return self.num == other.num and self.denom == other.denom

    def __ne__(self, other):
        self.simplify()
        if not isinstance(other, Fraction):
            return False
        return not (self.num == other.num and self.denom == other.denom)

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Second argument must be Fraction type")
        elif self.num * other.denom < self.denom * other.num:
            return True
        return False

    def __le__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Second argument must be Fraction type")
        if self.num * other.denom <= self.denom * other.num:
            return True
        return False

    def __gt__(self, other):
        self.simplify()
        other.simplify()
        if not isinstance(other, Fraction):
            raise TypeError("Second argument must be Fraction type")
        if self.num * other.denom > self.denom * other.num:
            return True
        return False

    def __ge__(self, other):
        self.simplify()
        other.simplify()
        if not isinstance(other, Fraction):
            raise TypeError("Second argument must be Fraction type")
        if self.num * other.denom >= self.denom * other.num:
            return True
        return False

    def __hash__(self):
        if isinstance(self, Fraction):
            return hash((self.num, self.denom))
        raise TypeError("Second argument must be Fraction type")

    def __float__(self) -> float:
        if isinstance(self, Fraction):
            return self.num / self.denom
        raise TypeError("Second argument must be Fraction type")

    def __int__(self) -> int:
        if isinstance(self, Fraction):
            return self.num // self.denom
        raise TypeError("Second argument must be Fraction type")

    def __iadd__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Second argument must be Fraction type")
        temp = math.lcm(self.denom, other.denom)
        self.num = (temp // self.denom) * self.num + (temp // other.denom) * other.num
        self.denom = temp
        self.simplify()
        return self

    def __isub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Second argument must be Fraction type")
        temp = math.lcm(self.denom, other.denom)
        self.num = ((temp // self.denom) * self.num) - ((temp // other.denom) * other.num)
        self.denom = temp
        self.simplify()
        return self


a = Fraction(-1, 2)
b = Fraction(1, 3)
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a <= b)
# print(a >= b)
# print(a.__float__())
# print(b.__float__())
# print(a.__int__())
# a += b
# print(a)
# a -=b
# print(a)
# a-=b
# print(a)

