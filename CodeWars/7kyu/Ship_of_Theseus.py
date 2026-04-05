# The "Ship of Theseus" is a classic philosophical thought experiment about identity over time.
#
# It asks: if every part of a ship is gradually replaced, one piece at a time, is it still the same ship in the end?
#
# This kata turns that idea into a simple validation problem.
#
# A ship is represented by a matrix of states.
#
# Each row shows the ship at a different moment in time.
#
# The ship is considered to remain the same only if, between every two consecutive rows, exactly one part of the ship has changed.
#
# Rules
# All rows must have the same length.
# Rows must be compared position by position.
# Between one row and the next, exactly one element (ship part) must be different.
# If any transition changes zero elements or more than one element, the process is invalid.
# Return true if the whole process is valid, otherwise return false.
#
# If the matrix has 0 or 1 row, return true.
#
# Example
# Initial values:
#
# [
#   ["a", "b", "c"],
#   ["x", "b", "c"],
#   ["x", "y", "c"],
#   ["x", "y", "z"]
# ]
# Step-by-step
# ["a", "b", "c"] -> ["x", "b", "c"] -> 1 change
# ["x", "b", "c"] -> ["x", "y", "c"] -> 1 change
# ["x", "y", "c"] -> ["x", "y", "z"] -> 1 change
# Result
# true
# Another example
# Initial values:
#
# [
#   ["a", "b", "c"],
#   ["x", "y", "c"]
# ]
# Step-by-step
# ["a", "b", "c"] -> ["x", "y", "c"] -> 2 changes
# Result
# false
# Different row lengths example
# Initial values:
#
# [
#   ["a", "b", "c"],
#   ["x", "b"]
# ]
# Step-by-step
# The rows have different lengths, so the process is invalid.
# Result
# false
# ArraysAlgorithmsLogicMatrix
# Solution
def ship_of_theseus(ship):
    if len(ship) <= 1: return True
    row_len = len(ship[0])
    for row in ship:
        if len(row) != row_len: return False
    for i in range(1, len(ship)):
        diff = 0
        for a, b in zip(ship[i - 1], ship[i]):
            if a != b:
                diff += 1
                if diff > 1: return False
        if diff != 1: return False
    return True