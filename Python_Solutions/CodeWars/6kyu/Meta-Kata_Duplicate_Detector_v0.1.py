# Objective
# As the number of published katas on Codewars grows, so does the likelihood of a newly published kata being a duplicate of an existing one. This is most prevalent among the simpler white katas (those ranked 7 or 8 kyu). Concerned with the ever-increasing number of duplicates, you've decided to start work on an automated process that filters out beginner-level duplicate katas.
#
# Your goal is to write a function that will find the duplicates in a list of newly published katas. Your function will serve as a preliminary filter; it should identify the most obvious duplicates in a list by passing arguments to the authors' solutions and comparing the outputs.
#
# Input
# Your function will receive an array of functions. These functions are the authors' solutions for their newly published katas.
#
# Output
# Your function must return a 2D array. Each subarray will consist of the index values of the functions that are duplicates of each other. The array will be sorted in ascending order based on the index value of the first duplicate that appears for its respective group. If there are no duplicates, return an empty array.
#
# Technical Details
# Each function accepts only one argument - an integer value ranging from 0 to 255, inclusive.
# The functions are all pure functions, so there won't be instances of functions that involve Date methods or anything of the like.
# Maximum array length is 50
# Inputs will always be valid.
# Test Example
# function_list = [
#     lambda x: x * 2,
#     lambda x: x ** 2,
#     lambda x: x + 20,
#     lambda x: x / 1000,
#     lambda x: x * x,
#     lambda x: pow(x, 2),
#     lambda x: x % 2
# ]
#
# dupe_detect(function_list) # [[1, 4, 5]]
# If you enjoyed this kata, be sure to check out my other katas.
#
# FUNDAMENTALS
# Solution
from collections import Counter
def dupe_detect(functions):
    l = [tuple(map(f, range(256))) for f in functions]
    lr = [tup for tup, v in Counter(l).items() if v>1]
    return [[i for i, t in enumerate(l) if t==f] for f in lr]