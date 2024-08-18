# A non-empty array a of length n is called an array of all possibilities if it contains all numbers between [0,a.length-1].Write a method named isAllPossibilities that accepts an integer array and returns true if the array is an array of all possibilities, else false.
#
# Example:
#
# a=[1,2,0,3]
# a.length-1=3
# a includes [0,3] ,hence the function should return true
# ARRAYSFUNDAMENTALS
# Solution
def is_all_possibilities(arr):
    return sorted(arr) == list(range(0, max(arr)+1)) if arr else False