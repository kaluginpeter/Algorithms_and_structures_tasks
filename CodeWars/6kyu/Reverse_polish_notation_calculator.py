# Your job is to create a calculator which evaluates expressions in Reverse Polish notation.
#
# For example expression 5 1 2 + 4 * + 3 -
# (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
#
# For your convenience, the input is formatted such that a space is provided between every token.
#
# Empty expression should evaluate to 0.
#
# Valid operations are +, -, *, /.
#
# You may assume that there won't be exceptional situations (like stack underflow or division by zero).
#
# ALGORITHMSMATHEMATICSINTERPRETERSPARSINGSTRINGS
# Solution
import operator
def calc(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    s = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = s.pop(), s.pop()
            s.append(OPERATORS[token](op1,op2))
        elif token:
            s.append(float(token))
    return s.pop()