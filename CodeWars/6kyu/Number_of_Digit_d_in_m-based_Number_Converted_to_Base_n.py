# You have a number x in base m (xm). Count the number of digits d after converting xm to base n.
#
# Representation of numbers
# base = 2: 0, 1
# base = 3: 0, 1, 2
# ...
# base = 10: 0, 1, ... 8, 9
# base = 11: 0 ... , 8, 9, a
# base = 12: 0 ... , 8, 9, a, b
# ...
# base = 16: 0 ... , 8, 9, a, ..., e, f
# base = 36: 0 ..., 8, 9, a, ..., y, z
# Preconditions
# 2 <= m <= 36
# 2 <= n <= 36
# xm is always a valid non-negative m-based number.
# d is always a valid digit for base n
# Examples
# # Function defintion
#
# count_digit(number, digit, base=10, from_base=10)
#
# # number    -> xm (str)
# # digit     -> d  (str)
# # base      -> n  (int)
# # from_base -> m  (int)
#
# count_digit("133", "3") == 2
# count_digit("10", "a", base=11) == 1
# count_digit("1100101110101", "d", base=15, from_base=2) == 1
# FUNDAMENTALS
# Solution
def count_digit(number, digit, base=10, from_base=10):
    c = '0123456789abcdefghijklmnopqrstuvwxyz'
    f = lambda x: c[x] if x<base else f(x//base) + c[x%base]
    return f(int(number, from_base)).count(digit)