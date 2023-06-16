# Write a function that takes an array/list of numbers and returns a number.
#
# See the examples and try to guess the pattern:
#
# even_odd([1,2,6,1,6,3,1,9,6]) => 393
# even_odd([1,2,3]) => 5
# even_odd([0,2,3]) => 3
# even_odd([1,0,3]) => 3
# even_odd([3,2])   => 6
# LOGICARRAYSMATHEMATICSPUZZLES
# Solution
def even_odd(arr):
    c = 0
    for k, v in enumerate(arr):
        if k % 2: c *= v
        else: c += v
    return c