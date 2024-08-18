# Given an array containing only integers, add all the elements and return the binary equivalent of that sum.
#
# If the array contains any non-integer element (e.g. an object, a float, a string and so on), return false.
#
# Note: The sum of an empty array is zero.
#
# arr2bin([1,2]) == '11'
# arr2bin([1,2,'a']) == False
# FUNDAMENTALS
# Solution
def arr2bin(arr):
    return bin(sum(arr))[2:] if all(type(i) == int for i in arr) else False