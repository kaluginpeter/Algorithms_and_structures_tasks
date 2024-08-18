# You're familiar with list slicing in Python and know, for example, that:
#
# >>> ages = [12, 14, 63, 72, 55, 24]
# >>> ages[2:4]
# [63, 72]
# >>> ages[2:]
# [63, 72, 55, 24]
# >>> ages[:3]
# [12, 14, 63]
# write a function inverse_slice() that takes three arguments: a list items, an integer a and an integer b. The function should return a new list with the slice specified by items[a:b] excluded. For example:
#
# >>>inverse_slice([12, 14, 63, 72, 55, 24], 2, 4)
# [12, 14, 55, 24]
# The input will always be a valid list, a and b will always be different integers equal to or greater than zero, but they may be zero or be larger than the length of the list.
#
# FUNDAMENTALSLISTS
# Solution
def inverse_slice(items, a, b):
    return items[:a] + items[b:] if b <= len(items)-1 else items[:a]