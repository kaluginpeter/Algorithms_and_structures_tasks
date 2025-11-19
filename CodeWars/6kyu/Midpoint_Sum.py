# Midpoint Sum
# For a given list of integers, return the index of the element where the sums of the integers to the left and right of the current element are equal.
#
# Ex:
#
# ints = [4, 1, 7, 9, 3, 9]
# # Since 4 + 1 + 7 = 12 and 3 + 9 = 12, the returned index would be 3
#
# ints = [1, 0, -1]
# # Returns None/nil/undefined/etc (depending on the language) as there
# # are no indices where the left and right sums are equal
# Here are the 2 important rules:
#
# The element at the index to be returned is not included in either of the sum calculations!
# Both the first and last index cannot be considered as a "midpoint" (So None for [X] and [X, X]) ```if:python
# For python, return -1 if there exists no such index ```
# ListsFundamentals