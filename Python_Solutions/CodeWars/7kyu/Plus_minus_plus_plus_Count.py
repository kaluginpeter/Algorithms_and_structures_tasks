# Count how often sign changes in array.
#
# result
# number from 0 to ... . Empty array returns 0
#
# example
# const arr = [1, -3, -4, 0, 5];
#
# /*
# | elem | count |
# |------|-------|
# |  1   |  0    |
# | -3   |  1    |
# | -4   |  1    |
# |  0   |  2    |
# |  5   |  2    |
# */
#
# catchSignChange(arr) == 2;
# FUNDAMENTALS
# Solution
def catch_sign_change(lst):
    return sum((x>=0)!=(y>=0) for x, y in zip(lst,lst[1:]))