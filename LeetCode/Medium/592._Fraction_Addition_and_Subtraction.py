# Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.
#
# The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.
#
#
#
# Example 1:
#
# Input: expression = "-1/2+1/2"
# Output: "0/1"
# Example 2:
#
# Input: expression = "-1/2+1/2+1/3"
# Output: "1/3"
# Example 3:
#
# Input: expression = "1/3-1/2"
# Output: "-1/6"
#
#
# Constraints:
#
# The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
# Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
# The number of given fractions will be in the range [1, 10].
# The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
# Solution Math Simulation O(NlogD) O(N)
class Solution:
    def parse_expression(self, expression: str) -> list[list[int, int]]:
        """
        Parse expression into fractions and return them.
        Time Complexity O(N)
        Memory Complexity O(N)
        """
        if expression[0] != '-':
            expression = '+' + expression

        fractions: list[list[int, int]] = []
        modules: dict[str, int] = {'+': 1, '-': -1}
        current_module: int = None
        numerator = denominator = 0
        numerator_flag: bool = False
        for char in expression:
            if char in '+-':
                if current_module is not None:
                    fractions.append([current_module * numerator, denominator])
                    numerator = denominator = 0
                current_module = modules[char]
                numerator_flag = not numerator_flag
            elif char == '/':
                numerator_flag = False
            else:
                if numerator_flag:
                    numerator = numerator * 10 + int(char)
                else:
                    denominator = denominator * 10 + int(char)

        fractions.append([current_module * numerator, denominator])
        return fractions

    def get_gcd(self, x: int, y: int) -> int:
        """
        Euclidean algorithm.
        Time Complexity O(log(min(x, y)))
        Memory Complexity O(1)
        """
        while x != 0:
            x, y = y % x, x
        return y

    def get_lcd(self, x: int, y: int) -> int:
        """
        Find Least Common Denominator of two integers.
        Time Complexity O(log(min(x, y)))
        Memory Complexity O(1)
        """
        return x * y // self.get_gcd(x, y)

    def simplify_fraction(self, numerator: int, denominator: int) -> list[int, int]:
        """
        Simplify fraction to irreducible fraction.
        Time Complexity O(log(min(x, y)))
        Memory Complexiy O(1)
        """
        negative: bool = numerator < 0 or denominator < 0
        numerator, denominator = abs(numerator), abs(denominator)
        gcd: int = self.get_gcd(numerator, denominator)
        return [(-1 if negative else 1) * (numerator // gcd), denominator // gcd]

    def operation_fractions(self, x: list[int, int], y: list[int, int]) -> list[int, int]:
        """
        Make addition or subtraction between two fractions and simplify the output.
        Time Complexity O(log(min(x, y)))
        Memory Complexity O(1)
        """
        if x[1] == y[1]:
            return [x[0] + y[0], x[1]]
        lcd: int = self.get_lcd(x[1], y[1])
        numerator: int = x[0] * (lcd // x[1]) + y[0] * (lcd // y[1])
        denominator: int = lcd
        numerator_denominator: list[int, int] = self.simplify_fraction(numerator, denominator)
        return numerator_denominator

    def fractionAddition(self, expression: str) -> str:
        """
        Solve expression of addition and subtraction fractions
        and return irreducible fraction.
        Time Complexity O(NlogD) where D is denominator of the fractions
        Memory Complexity O(N)
        """
        fractions: list[list[int, int]] = self.parse_expression(expression)

        current_fraction: list[int, int] = fractions[0]
        for idx in range(1, len(fractions)):
            next_fraction: list[int, int] = fractions[idx]
            current_fraction = self.operation_fractions(current_fraction, next_fraction)
        current_fraction = self.simplify_fraction(*current_fraction)

        return f'{current_fraction[0]}/{current_fraction[1]}'