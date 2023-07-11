# If you have not ever heard the term Arithmetic Progression,
# refer to: http://www.codewars.com/kata/find-the-missing-term-in-an-arithmetic-progression/python
#
# And here is an unordered version. Try if you can survive lists
# of MASSIVE numbers (which means time limit should be considered). :D
#
# Note: Don't be afraid that the minimum or the maximum element
# in the list is missing, e.g. [4, 6, 3, 5, 2] is missing 1 or 7, but this case is excluded from the kata.
#
# Example:
#
# find([3, 9, 1, 11, 13, 5]) # => 7
# ALGORITHMSMATHEMATICSPERFORMANCE
# Solution
def find(seq):
    mi, ma, result = seq[0], seq[0], seq[0]
    for i in range(1, len(seq)):
        mi, ma, result = min(mi, seq[i]), max(ma, seq[i]), result ^ seq[i]
    if mi == ma:
        return mi
    differens = (ma - mi) // len(seq)
    while mi <= ma:
        result = result ^ mi
        mi += differens
    return result
# Solution 2
def find(seq):
  return (min(seq)+max(seq))*(len(seq)+1)/2-sum(seq)