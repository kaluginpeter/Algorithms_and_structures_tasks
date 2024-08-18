# This is the simple version of Shortest Code series. If you need some challenges, please try the challenge version
#
# Task
# Your apple has a virus, and the infection is spreading.
#
# The apple is a two-dimensional array, containing strings "V" (virus)
# and "A" (uninfected parts). For each hour, the infection spreads one space up, down, left and right.
#
# Input: 2D array apple and number n (n >= 0).
#
# Output: 2D array showing the apple after n hours.
#
# Series:
# Bug in Apple
# Father and Son
# Jumping Dutch act
# Planting Trees
# Give me the equation
# Find the murderer
# Reading a Book
# Eat watermelon
# Special factor
# Guess the Hat
# Symmetric Sort
# Are they symmetrical?
# Max Value
# Trypophobia
# Virus in Apple
# Balance Attraction
# Remove screws I
# Remove screws II
# Regular expression compression
# Collatz Array(Split or merge)
# Tidy up the room
# Waiting for a Bus
# PUZZLESGAMES
# Solution
def infect_apple(apple, n):
    h, w = range(len(apple)), range(len(apple[0]))
    v = [(i, j) for i in h for j in w if apple[i][j] == "V"]
    return [["A" if all(n < abs(y - j) + abs(x - i) for y, x in v) else "V" for i in w] for j in h]