# Write a function
#
# alternate_sort(l)
# that combines the elements of an array by sorting the elements
# ascending by their absolute value and outputs negative and non-negative
# integers alternatingly (starting with the negative value, if any).
#
# E.g.
#
# alternate_sort([5, -42, 2, -3, -4, 8, -9,]) == [-3, 2, -4, 5, -9, 8, -42]
# alternate_sort([5, -42, 2, -3, -4, 8, 9]) == [-3, 2, -4, 5, -42, 8, 9]
# alternate_sort([5, 2, -3, -4, 8, -9]) == [-3, 2, -4, 5, -9, 8]
# alternate_sort([5, 2, 9, 3, 8, 4]) == [2, 3, 4, 5, 8, 9]
# ALGORITHMSARRAYSSORTING
# Solution
def alternate_sort(l):
    l1 = sorted(i for i in l if i >= 0)[::-1]
    l2 = sorted(i for i in l if i < 0)
    f = []
    while l1 or l2:
        if l2:
            f.append(l2.pop())
            if l1: f.append(l1.pop())
        elif l1:
            f.append(l1.pop())
            if l2: f.append(l2.pop())
    return f