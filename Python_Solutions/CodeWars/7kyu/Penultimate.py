A# Find the second-to-last element of a list.
#
# The input list will always contain at least two elements.
#
# Example:
#
# penultimate([1,2,3,4])            # => 3
# penultimate("Python is dynamic") # => 'i'
# (courtesy of haskell.org)
#
# LISTSFUNDAMENTALS
# Solution
def penultimate(a):
    return a[-2]