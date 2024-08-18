# Write a function that returns only the decimal part of the given number.
#
# You only have to handle valid numbers, not Infinity, NaN, or similar. Always return a positive decimal part.
#
# Examples
# get_decimal(2.4)  # 0.4
# get_decimal(-0.2) # 0.2
# FUNDAMENTALS
# Solution
def get_decimal(n):
    return abs(n) % 1