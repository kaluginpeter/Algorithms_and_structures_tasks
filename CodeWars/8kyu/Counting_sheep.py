# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
#
# For example,
#
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
#
# Hint: Don't forget to check for bad values like null/undefined
#
# ARRAYSFUNDAMENTALS
# Solution
def count_sheeps(sheep):
    count = 0
    for elem in sheep:
        if elem == True:
            count += 1
    return count