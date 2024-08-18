# In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.
#
# solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
# -- We sort by highest frequency to lowest frequency.
# -- If two elements have same frequency, we sort by increasing value.
# More examples in test cases.
#
# Good luck!
#
# Please also try Simple time difference
#
# ALGORITHMSSORTINGARRAYS
# Solution
def solve(arr):
    return sorted(arr, key= lambda x: (-arr.count(x), x))