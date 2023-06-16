# Write
#
# function biggest(nums)
# that given an array of numbers >= 0, will arrange them such that they form the biggest number.
#
# For example:
#
# biggest([1, 2, 3]) === '321'
# biggest([3, 30, 34, 5, 9]) === '9534330'
# The results will be large so make sure to return a string.
#
# STRINGSARRAYSALGORITHMS
# Solution
def biggest(nums):
    return str(int(''.join(sorted(map(str,nums),key=lambda x:3*x)[::-1])))