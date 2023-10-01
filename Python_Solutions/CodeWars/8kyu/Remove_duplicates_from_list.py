# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.
#
# The order of the sequence has to stay the same.
#
# Examples:
#
# Input -> Output
# [1, 1, 2] -> [1, 2]
# [1, 2, 1, 1, 3, 2] -> [1, 2, 3]
# FUNDAMENTALSARRAYSLISTS
# Solution
def distinct(seq):
    new_list = []
    for elem in seq:
        if elem not in new_list:
            new_list.append(elem)
    return new_list