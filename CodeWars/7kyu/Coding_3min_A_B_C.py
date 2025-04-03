# This is the simple version of Fastest Code series. If you need some challenges, please try the Performance version
#
# Task:
# Give you a number array numbers and a number c.
#
# Find out a pair of numbers(we called them number a and number b) from the array numbers, let a*b=c, result format is an array [a,b]
#
# The array numbers is a sorted array, value range: -100...100
#
# The result will be the first pair of numbers, for example,findAB([1,2,3,4,5,6],6) should return [1,6], instead of [2,3]
#
# Please see more example in testcases.
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
# PuzzlesGames
# Solution
def find_a_b(numbers, c):
    num_to_idx: dict[int, int] = dict()
    answer: list[int, int] = []
    for i in range(len(numbers)):
        if numbers[i] and c / numbers[i] in num_to_idx:
            if not answer or (num_to_idx[c / numbers[i]] < num_to_idx[answer[0]]):
                answer = [c // numbers[i], numbers[i]]
        if not numbers[i] and not c:
            if len(numbers) == 1: return None
            if i: return [numbers[0], 0]
            else: return [0, numbers[i + 1]]
        if numbers[i] not in num_to_idx:
            num_to_idx[numbers[i]] = i
    return answer or None