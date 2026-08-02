# Create a function that accepts a parameter mat, where mat is a matrix (a list of lists) containing only zeros except for a single cell that contains a 1.
#
# After calling this function with the matrix, it should return another function that can be called repeatedly with string commands:
#
# "up" → Move the 1 one position up.
# "down" → Move the 1 one position down.
# "left" → Move the 1 one position to the left.
# "right" → Move the 1 one position to the right.
# "stop" → Return the final state of the matrix.
# Examples
# one = [[1]]
#
# two = [[1, 0],
#        [0, 0]]
#
# # It should also work for a 1×1 matrix:
# move(one)("up")("stop") ➞ [[1]]
#
# # The `1` should wrap around the matrix edges:
# move(two)("left")("stop") ➞ [[0, 1],
#                               [0, 0]]
#
# # It should handle multiple commands in sequence:
# move(two)("right")("down")("stop") ➞ [[0, 0],
#                                        [0, 1]]
# # The function `move` itself should return a callable:
# callable(move(two)) ➞ True
# Notes
# The matrix can be any size m × n, where m ≥ 1 and n ≥ 1.
# Movement wraps around: going off one edge should bring the 1 to the opposite side.
# The returned function should support being called repeatedly any number of times before "stop" is issued.
# Arrays