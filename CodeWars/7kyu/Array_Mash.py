# Mash 2 arrays together so that the returning array has alternating elements of the 2 arrays . Both arrays will always be the same length.
#
# eg. [1,2,3] + ['a','b','c'] = [1, 'a', 2, 'b', 3, 'c']
#
# ARRAYSSTRINGSFUNDAMENTALS
# Solution
def array_mash(a, b):
    l = []
    while a or b:
        l.append(a.pop(0))
        l.append(b.pop(0))
    return l