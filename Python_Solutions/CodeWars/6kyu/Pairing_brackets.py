# Write a function which outputs the positions of matching bracket pairs.
# The output should be a dictionary with keys the positions of the open brackets
# '(' and values the corresponding positions of the closing brackets ')'.
#
# For example: input = "(first)and(second)" should return {0:6, 10:17}
#
# If brackets cannot be paired or if the order is invalid (e.g. ')(') return False.
# In this kata we care only about the positions of round brackets '()', other types of brackets should be ignored.
#
# STRINGSPARSINGALGORITHMS
# Solution
def bracket_pairs(string):
    d, l = {}, []
    for k, v in enumerate(string):
        if v == '(':l.append(k)
        elif v == ')':
            if not l:return False
            d[l.pop()] = k
    return False if l else d