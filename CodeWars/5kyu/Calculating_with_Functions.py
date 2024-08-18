# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))
# Solution
def zero(integer = None):
    return 0 if integer is None else int(integer(0))
def one(integer = None):
    return 1 if integer is None else int(integer(1))
def two(integer = None):
    return 2 if integer is None else int(integer(2))
def three(integer = None):
    return 3 if integer is None else int(integer(3))
def four(integer = None):
    return 4 if integer is None else int(integer(4))
def five(integer = None):
    return 5 if integer is None else int(integer(5))
def six(integer = None):
    return 6 if integer is None else int(integer(6))
def seven(integer = None):
    return 7 if integer is None else int(integer(7))
def eight(integer = None):
    return 8 if integer is None else int(integer(8))
def nine(integer = None):
    return 9 if integer is None else int(integer(9))

def plus(second_integer):
    return lambda integer: integer + second_integer
def minus(second_integer):
    return lambda integer: integer - second_integer
def times(second_integer):
    return lambda integer: integer * second_integer
def divided_by(second_integer):
    return lambda integer: integer / second_integer