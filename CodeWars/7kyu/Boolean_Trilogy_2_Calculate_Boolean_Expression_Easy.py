# Task
# You get a Boolean expression and the values of its variables as input. Your task is to calculate this Boolean expression with a given set of variable values.
#
# Details
# The input expression consists of variables represented by uppercase letters A-F and operations "&" (logical AND) and "|" (logical OR).
# Parentheses and other operations are missing from the expression.
# Variables can be repeated and placed in any order.
# The expression contains at least one variable
# Variable values are represented as a dictionary {name: value}.
# Example
# calculate("A & B & C", {"A": 0, "B": 1, "C": 0})   # returns 0
# # A & B & C = 0 & 1 & 0 = 0
#
# calculate("B & A | C", {"A": 1, "B": 0, "C": 1})   # returns 1
# # B & A | C = 0 & 1 | 1 = 0 | 1 = 1
# Fundamentals
# Solution
def calculate(expr: str, values: dict[str, int]) -> int:
    for letter, value in values.items():
        expr = expr.replace(letter, str(value))
    expr = expr.replace('&', 'and').replace('|', 'or')
    return eval(expr)