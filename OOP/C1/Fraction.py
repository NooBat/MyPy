def gcd(m, n):
    if m == 0:
        return n
    elif m == n:
        return m
    elif m > n:
        return gcd(n, m)
    
    return gcd(n % m, m)

class Fraction:
    def __init__(self, top, bottom):
        if type(top) != int or type(bottom) != int:
            raise ValueError("Numerator/Denominator must be an integer")
        if (bottom < 0):
            top = -top
            bottom = -bottom
        commonDiv = gcd(abs(top), abs(bottom))
        self.num = top // commonDiv
        self.den = bottom // commonDiv
    
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    def __repr__(self):
        return "Fraction({},{})".format(self.num, self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __eq__(self, other):
        return (True if self - other == 0 else False)

    def __add__(self, other):
        if type(other) != type(self):
            other = Fraction(other, 1)

        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        return self + Fraction(-other.num, other.den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        return self * Fraction(other.den, other.num)

    def __gt__(self, other):
        return (True if self - other > 0 else False)
    
    def __ge__(self, other):
        return (True if self - other >= 0 else False)

    def __lt__(self, other):
        return (True if self - other < 0 else False)

    def __le__(self, other):
        return (True if self - other <= 0 else False)

    def __ne__(self, other):
        return (True if self - other != 0 else False)

x = Fraction(2, 3)
x += 1
print(x)