# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.
#
# the array can't be empty
# only non-negative, single digit integers are allowed
# Return nil (or your language's equivalent) for invalid inputs.
#
# Examples
# Valid arrays
#
# [4, 3, 2, 5] would return [4, 3, 2, 6]
# [1, 2, 3, 9] would return [1, 2, 4, 0]
# [9, 9, 9, 9] would return [1, 0, 0, 0, 0]
# [0, 1, 3, 7] would return [0, 1, 3, 8]
#
# Invalid arrays
#
# [1, -9] is invalid because -9 is not a non-negative integer
#
# [1, 2, 33] is invalid because 33 is not a single-digit integer
#
# FUNDAMENTALSARRAYSALGORITHMS
# Solution
def up_array(arr):
    integer = ''
    list = []
    print(arr)
    if len(arr) < 1:
        return None
    elif len(arr) == 1 and arr[0] <= 9:
        return [1]
    for i in arr:
        if len(str(i)) > 1 or i < 0:
            return None
    else:
        for elem in arr:
            if str(elem) in '1234567890':
                integer += str(elem)
    if integer[0] == '0' and integer[1] != '0':
        integer = int(integer[1:]) + 1
        integer = '0' + str(integer)
    elif integer[0] == '0' and integer[1] == '0':
        integer = int(integer[2:]) + 1
        integer = '00' + str(integer)
    elif integer[0] != '0':
        integer = str(int(integer) + 1)
    for char in integer:
        list.append(int(char))
    return list