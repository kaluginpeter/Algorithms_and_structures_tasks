# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.
#
# This is the first kata in series:
#
# Find the unique number (this kata)
# Find the unique string
# Find The Unique
# FUNDAMENTALSALGORITHMSARRAYS
# Solution
def find_uniq(arr):
    found = set()
    found_again = set()

    for a in arr:
        if a in found_again:
            continue
        if a in found:
            found.remove(a)
            found_again.add(a)
        else:
            found.add(a)
    res = list(found)
    return (res[0])