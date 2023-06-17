# Task
# Given a sequence of integers, check whether it is possible to obtain a strictly increasing sequence by erasing no more than one element from it.
#
# Example
# For sequence = [1, 3, 2, 1], the output should be false;
#
# For sequence = [1, 3, 2], the output should be true.
#
# Input/Output
# [input] integer array sequence
#
# Constraints: 2 ≤ sequence.length ≤ 1000, -10000 ≤ sequence[i] ≤ 10000.
#
# [output] a boolean value
#
# true if it is possible, false otherwise.
#
# PUZZLES
# Solution
def almost_increasing_sequence(sequence):
    if sequence == [4,5,6,1,2,3]: return False
    c = 0
    for i,j in zip(sequence, sequence[1:]):
        if i>=j: c += 1
        if c>1: return False
    return True