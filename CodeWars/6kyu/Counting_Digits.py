# This kata is inspired by the British gameshow Only Connect, specifically the clue that stumped the contestants seen here
#
# Your goal is to write a function that receives an integer and then repeatedly counts the occurrences of each digit (the number of rounds will be given as a positive integer).
#
# Note
# The order is important, the result should list the digits in the order they first appeared (from left to right).
#
# Examples
# Simple 1 round example:
# num = 141, rounds = 1
# ROUND 1: 141 --> [21, 14]
# # Reading left to right, 1 was encountered first (two 1), then 4 (one 4)
# So the solution is [21, 14]
#
# Simple 1 round example with a larger number:
# num = 1221313, rounds = 1
# ROUND 1: 1221313 --> [31, 22, 23]
# # Reading left to right, 1 was encountered first, then 2, then 3
# So the solution is [31, 22, 23]
#
# More complex 3 round example:
# num = 5, rounds = 3
# ROUND 1: 5 --> [15]
# ROUND 2: 15 --> [11, 15]
# ROUND 3: 1115 --> [31, 15]
# So the solution is [31, 15]
#
# Fundamentals