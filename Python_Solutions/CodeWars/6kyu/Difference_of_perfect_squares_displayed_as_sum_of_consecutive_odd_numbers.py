# This kata will return a string that represents the difference of two perfect
# squares as the sum of consecutive odd numbers.
#
# Specifications:
#
# • The first input minus the second input reveals the exact number of consecutive odd numbers
# required for the solution - you can check this in the examples below.
#
# • The first input will always be larger than the second.
#
# • All inputs will be valid so no need for error checking.
#
# • Outputs will always be positive.
#
# • Inputs will range between 0 and 200, (inclusive).
#
# • In the returned string there are spaces before and after the plus sign,
# the minus sign and the equals sign but nowhere else.
#
# Examples:
#
# squaresToOdd(9, 5) --> "9^2 - 5^2 = 11 + 13 + 15 + 17 = 56"
#
# squaresToOdd(10, 7) --> "10^2 - 7^2 = 15 + 17 + 19 = 51"
#
# squaresToOdd(100, 98) --> "100^2 - 98^2 = 197 + 199 = 396"
#
# squaresToOdd(100, 99) --> "100^2 - 99^2 = 199 = 199"
#
# ALGORITHMSMATHEMATICS
# Solution
def squares_to_odd(a, b):
    return f'{a}^2 - {b}^2 = {" + ".join(map(str, range(2 * b + 1, 2 * a, 2)))} = {a ** 2 - b ** 2}'