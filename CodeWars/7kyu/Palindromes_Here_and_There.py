# An array is given with palindromic and non-palindromic numbers. A palindromic number is a number that is the same from a reversed order. For example 122 is not a palindromic number, but 202 is one.
#
# Your task is to write a function that returns an array with only 1s and 0s, where all palindromic numbers are replaced with a 1 and all non-palindromic numbers are replaced with a 0.
#
# For example:
#
# [101, 2, 85, 33, 14014]  ==>  [1, 1, 0, 1, 0]
# [45, 21, 303, 56]        ==>  [0, 0, 1, 0]
# ALGORITHMS
# Solution
def convert_palindromes(numbers):
    return [1 if str(i) == str(i)[::-1] else 0 for i in numbers]