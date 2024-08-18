# Write a function that appends the items from sequence 2 onto sequence 1, returning the newly formed sequence. Your function should also be able to handle nested sequences.
#
# All inputs will be arrays/nested arrays.
#
# For example:
#
# ['a','b','c'], [1,2,3]     --> ['a','b','c',1,2,3]
# [['x','x'],'B'], ['c','D'] --> [['x','x'],'B','c','D']
# ARRAYSFUNDAMENTALS
# Solution
def append_arrays(seq1, seq2):
    return seq1 + seq2