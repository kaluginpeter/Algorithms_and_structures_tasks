# Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.
#
# Return as a number.
#
# FUNDAMENTALSSTRINGSARRAYS
# Solution
def div_con(x):
    return sum(list(i if type(i) == int else 0 for i in x)) - sum(list(int(i) if type(i) == str else 0 for i in x ))