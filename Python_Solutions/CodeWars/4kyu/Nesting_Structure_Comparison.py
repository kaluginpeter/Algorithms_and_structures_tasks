# Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.
#
# For example:
#
# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
#
# # should return False
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
#
# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )
#
# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
# ARRAYSALGORITHMS
# Solution
def same_structure_as(original,other):
    if isinstance(original, list) or isinstance(other, list):
        if type(original) != type(other):
                return False
        if len(original) != len(other):
            return False
    for i in range(len(original)):
        if isinstance(original[i], list) or isinstance(other[i], list):
            if type(original[i]) != type(other[i]):
                return False
            return same_structure_as(original[i], other[i])
    return True