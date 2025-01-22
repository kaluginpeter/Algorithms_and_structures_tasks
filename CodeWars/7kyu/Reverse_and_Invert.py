# Reverse and invert all integer values in a given list.
#
# [1,12,'a',3.4,87,99.9,-42,50,5.6] --> [-1,-21,-78,24,-5]
# Remove all types other than integer.
#
# ListsFundamentals
# Solution
def reverse_invert(lst):
    return [[-1, 1][num < 0] * int(str(abs(num))[::-1]) for num in lst if type(num) is int]
