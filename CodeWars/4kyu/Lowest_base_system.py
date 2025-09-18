# Your task is determine the lowest number base system in which the input n ( base 10 ), expressed in this number base system, is all 1s in its digits.
#
# See some examples:
#
# 7 in base 2 is 111 - fits! answer is 2
#
# 21 in base 2 is 10101 - contains 0, does not fit
# 21 in base 3 is 210 - contains 0 and 2, does not fit
# 21 in base 4 is 111 - contains only 1 it fits! answer is 4
#
# n is always less than Number.MAX_SAFE_INTEGER or equivalent.
#
# Performance