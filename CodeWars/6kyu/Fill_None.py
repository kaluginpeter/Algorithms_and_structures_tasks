# Task
# Write a function that accepts a list that can contain missing data, and an integer representing the method on how to fill the missing data if there is any. Missing data is represented as None. The list will only contain integers and None values.
#
# Note that depending on the language you attempt this kata with, None corresponds to:
#
# None (Python)
# undefined (Javascript)
# Nothing (Haskell)
# The fill method rules are outlined below:
#
# Fill method:
#   -1: backwards
#    0: nearest
#    1: forwards
# Example
# arr = [None, 1, None, None, None, 2, None]
#
# fill(arr, -1) == [1, 1, 2, 2, 2, 2, None]  # None replaced by closest int on the right
# fill(arr,  0) == [1, 1, 1, 1, 2, 2, 2]     # None replaced by closest int. If equidistant, choose the smallest int
# fill(arr,  1) == [None, 1, 1, 1, 1, 2, 2]  # None replaced by closest int on the left
# Notes
# [] should return []
# [None] should return [None]
# Arrays will only contain integers and None values
# FUNDAMENTALS