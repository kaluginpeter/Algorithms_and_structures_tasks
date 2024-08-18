# Find the number with the most digits.
#
# If two numbers in the argument array have the same number of digits, return the first one in the array.
#
# STRINGSFUNDAMENTALS
# Solution
def find_longest(arr):
    arr_len = [len(str(n)) for n in arr];
    return arr[arr_len.index(max(arr_len))];