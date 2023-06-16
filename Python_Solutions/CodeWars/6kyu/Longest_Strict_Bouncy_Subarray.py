# This kata was seen in programming competitions with a wide range of variations.
# A strict bouncy array of numbers, of length three or longer,
# is an array that each term (neither the first nor the last element) is strictly higher or lower than its neighbours.
#
# For example, the array:
#
# arr = [7,9,6,10,5,11,10,12,13,4,2,5,1,6,4,8] (length = 16)
# The two longest bouncy subarrays of arr are
#
# [7,9,6,10,5,11,10,12] (length = 8) and [4,2,5,1,6,4,8] (length = 7)
# According to the given definition, the arrays [8,1,4,6,7], [1,2,2,1,4,5], are not bouncy.
#
# For the special case of length 2 arrays, we will consider them strict bouncy if the two elements are different.
#
# The arrays [-1,4] and [0,-10] are both bouncy, while [0,0] is not.
#
# An array of length 1 will be considered strict bouncy itself.
#
# You will be given an array of integers and you should output the longest strict bouncy subarray.
#
# In the case of having more than one bouncy subarray of same length,
# it should be output the subarray with its first term of lowest index in the original array.
#
# Let's see the result for the first given example.
#
# arr = [7,9,6,10,5,11,10,12,13,4,2,5,1,6,4,8]
# longest_bouncy_list(arr) === [7,9,6,10,5,11,10,12]
# See more examples in the example tests box.
#
# Features of the random tests
#
# length of the array inputs up to 1000
# -500 <= arr[i] <= 500
# Enjoy it!
#
# PERFORMANCEALGORITHMSMATHEMATICSDATA STRUCTURESARRAYS
# Solution
def longest_bouncy_list(arr):
    l, s = [], []
    for v in arr:
        if not l or v!=l[-1] and (len(l)==1 or (l[-1]-l[-2]) * (l[-1]-v) > 0):
            l.append(v)
        else: l = l[-1:] + [v] if v != l[-1] else [v]
        if len(l)>len(s): s = l
    return s