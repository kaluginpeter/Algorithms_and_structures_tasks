# Given a string, remove any characters that are unique from the string.
#
# Example:
#
# input: "abccdefee"
#
# output: "cceee"
#
# FUNDAMENTALSSTRINGSALGORITHMS
# Solution
def only_duplicates(string):
    return ''.join(i for i in string if string.count(i) > 1)