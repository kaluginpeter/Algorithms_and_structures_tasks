# Find the last element of the given argument(s).
#
# Examples
# last([1, 2, 3, 4]) ==>  4
# last("xyz")        ==> "z"
# last(1, 2, 3, 4)   ==>  4
# In javascript and CoffeeScript a list will be an array, a string or the list of arguments.
#
# (courtesy of haskell.org)
#
# LISTSFUNDAMENTALS
# Solution
def last(*args):
    try:
        return [args][-1][-1][-1]
    except:
        return args[-1]