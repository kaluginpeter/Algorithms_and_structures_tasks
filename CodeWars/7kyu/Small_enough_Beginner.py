# You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.
#
# You can assume all values in the array are numbers.
#
# FUNDAMENTALSARRAYS
# Solution
def small_enough(array, limit):
    for elem in array:
        if elem > limit:
            return False
    return True