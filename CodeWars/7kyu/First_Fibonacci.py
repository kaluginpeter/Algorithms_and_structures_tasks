# First Fibonacci
# What is the Fibonacci sequence
# The Fibonacci sequence starts with the numbers 0 and 1, and the next number is given by adding the previous two together. So 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, etc.
#
# The challenge
# Your challenge is, given two numbers in a Fibonacci-like sequence (where the next number is found by adding the two previous numbers), to find the lowest possible non-negative numbers that the sequence originates from. For example, if you are given the numbers 398 and 644, which come from this sequence: 2, 6, 8, 14, 22, 36, 58, 94, 152, 246, 398, 644
#
# Then you would return 2 and 6, as they are the numbers which started the sequence.
#
# Note that 8 and 14, while they also start a sequence containing 398 and 644, are not correct as only the lowest possible sequence start is accepted.
#
# Notes
# For the purposes of this puzzle, Fibonacci-like sequences don't decrease. This means that the following sequence is not considered a Fibonacci-like sequence and 4 and 2 are NOT solutions to the puzzle. 4, 2, 6, 8, 14, 22, 36, 58, 94, 152, 246, 398, 644
# Good luck!
#
# Mathematics
# Solution
def solution(first, second):
    while second - first >= 0 and second - first <= first:
        first, second = second - first, first
    return first, second