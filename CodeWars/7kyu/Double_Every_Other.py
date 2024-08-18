# Write a function that doubles every second integer in a list, starting from the left.
#
# Example:
#
# For input array/list :
#
# [1,2,3,4]
# the function should return :
#
# [1,4,3,8]
# FUNDAMENTALSLISTSARRAYSALGORITHMS
# Solution
def double_every_other(lst):
    return [i*2 if lst.index(i)%2!=0 else i for i in lst]