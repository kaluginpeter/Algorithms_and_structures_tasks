# Check that the two provided arrays both contain the same number of different unique items,
# regardless of order. For example in the following:
#
# [a,a,a,a,b,b] and [c,c,c,d,c,d]
# Both arrays have four of one item and two of another, so balance should return true.
#
# #Have fun!
#
# FUNDAMENTALS
# Solution
from collections import Counter
def balance(arr1, arr2):
    s1, s2 = sorted(Counter(arr1).values()), sorted(Counter(arr2).values())
    return all(i == j for i, j in zip(s1, s2)) and len(s1) == len(s2)