# Find the difference between two collections. The difference means that either the character is present in one collection or it is present in other, but not in both. Return a sorted list with the difference.
#
# The collections can contain any character and can contain duplicates.
#
# Example
# A = [a, a, t, e, f, i, j]
#
# B = [t, g, g, i, k, f]
#
# difference = [a, e, g, j, k]
# FUNDAMENTALSARRAYSALGORITHMS
# Solution
def diff(a, b):
    return sorted(list(set([i for i in a if i not in b] + [i for i in b if i not in a])))