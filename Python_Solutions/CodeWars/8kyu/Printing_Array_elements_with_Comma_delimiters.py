# Input: Array of elements
#
# ["h","o","l","a"]
#
# Output: String with comma delimited elements of the array in th same order.
#
# "h,o,l,a"
#
# Note: if this seems too simple for you try the next level
#
# ARRAYSFUNDAMENTALS
# Solution
def print_array(arr):
    return ','.join([str(i) for i in arr])