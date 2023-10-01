# For every good kata idea there seem to be quite a few bad ones!
#
# In this kata you need to check the provided 2 dimensional array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.
#
# The sub arrays may not be the same length.
#
# The solution should be case insensitive (ie good, GOOD and gOOd all count as a good idea). All inputs may not be strings.
#
# FUNDAMENTALSARRAYSSTRINGS
# Solution
def well(arr):
    l = [j.lower() if type(j) == str else j for i in arr for j in i]
    con = l.count('good')
    return 'Fail!' if con == 0 else 'Publish!' if 1 <= con <= 2 else 'I smell a series!'