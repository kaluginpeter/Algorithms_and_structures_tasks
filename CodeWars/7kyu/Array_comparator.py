# You have two arrays in this kata, every array contains unique elements only. Your task is to calculate number of elements in the first array which are also present in the second array.
#
# ARRAYSFUNDAMENTALS
# Solution
def match_arrays(v, r):
    return sum(1 for i in v if i in r)