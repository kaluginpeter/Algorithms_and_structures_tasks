# Task
# Write a function that checks if two non-negative integers make an "interlocking binary pair".
#
# Interlock ?
# numbers can be interlocked if their binary representations have no 1's in the same place
# comparisons are made by bit position, starting from right to left (see the examples below)
# when representations are of different lengths, the unmatched left-most bits are ignored
# Examples
# a = 9, b = 4
# Stacking representations shows how they can interlock.
#
#  9    1001
#  4     100
# Here, no 1's share any position, so the function returns true.
#
# a = 3, b = 6
# These representations do not interlock.
#
#  3      11
#  6     110
# Finding they both have a 1 in the same position, the function returns false.
#
# Input
# Two non-negative integers.
#
# Output
# Boolean true or false whether or not these integers are interlockable.
#
# Enjoy!
# Consider one of the following kata to solve next:
#
# Playing With Toy Blocks ~ Can you build a 4x4 square?
# Four Letter Words ~ Mutations
# Crossword Puzzle! (2x2)
# Is Sator Square?
# Nota Bene:
# This kata is accepting of translations for any languages other than: Java, JavaScript, CoffeeScript, TypeScript, Go, Groovy, Julia, Dart, and Kotlin; as those are currently underway by the author. Thank you!
#
# BINARYBITSALGORITHMS
# Solution
def interlockable(a, b):
    return not a & b