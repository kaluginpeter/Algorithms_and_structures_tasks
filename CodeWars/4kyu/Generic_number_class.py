# Your task in this kata is to implement the function create_number_class which will take a string parameter alphabet and return a class representing a number composed of this alphabet.
#
# The class number will implement the four classical arithmetic operations (+, -, *, //), a method to convert itself to string, and a convert_to method which will take another class number as parameter and will return the value of the actual class number converted to the equivalent value with tha alphabet of the parameter class (return a new instance of this one).
#
# Example:
#
# BinClass = create_number_class('01')
# HexClass = create_number_class('0123456789ABCDEF')
#
# x = BinClass('1010')
# y = BinClass('10')
#
# print(x+y)                   => '1100'
# isinstance(x+y, BinClass)    => True
# print(x.convert_to(HexClass) => 'A'
# Notes:
#
# Only positives integers will be used (either as parameters or results of calculations).
# You'll never encounter invalid calculations (divisions by zero or things like that).
# Alphabets will contain at least 2 characters.
# MathematicsMetaprogrammingAlgorithms
# Solution
def create_number_class(alphabet):
    base = len(alphabet)
    char_to_value = {ch: i for i, ch in enumerate(alphabet)}

    class Number:
        __slots__ = ("value",)
        def __init__(self, s):
            if isinstance(s, int): self.value = s
            else:
                val = 0
                for ch in s: val = val * base + char_to_value[ch]
                self.value = val

        def __str__(self):
            if self.value == 0: return alphabet[0]
            val = self.value
            digits = []
            while val > 0:
                val, rem = divmod(val, base)
                digits.append(alphabet[rem])
            return ''.join(reversed(digits))

        def __add__(self, other):
            return Number(self.value + other.value)

        def __sub__(self, other):
            return Number(self.value - other.value)

        def __mul__(self, other):
            return Number(self.value * other.value)

        def __floordiv__(self, other):
            return Number(self.value // other.value)

        def convert_to(self, other_instance):
            target_class = other_instance if isinstance(other_instance, type) else type(other_instance)
            return target_class(self.value)

    return Number