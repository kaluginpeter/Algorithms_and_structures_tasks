# Write a function with the signature shown below:
#
# def is_int_array(arr):
#     return True
# returns true  / True if every element in an array is an integer or a float with no decimals.
# returns true  / True if array is empty.
# returns false / False for every other input.
# ARRAYSFUNDAMENTALS
# Solution
def is_int_array(arr):
    try:
        return arr == list(map(int, arr))
    except:
        return False