# Clean Nesting Tree
# Task:
#
# You are given a main list that may contain nested lists of arbitrary depth. Imagine this structure as a tree, where each list is a node and its elements are child nodes.
#
# Your task is to implement a function that checks whether the entire structure follows the nesting rule:
#
# At each level (depth) of the tree, each node's children must all either be:
#
# dead ends (empty lists [])
#
# nested lists
#
# Examples:
#
# [ [ [[]], [[]], [[]]  ], [[]] , [[]]  ] -> True
#
# [] -> True
#
# [ [], [] ] -> True
#
# [ [ [], [], []  ] , [ [], [[]]  ] ]  -> False
#
# Explanation:
#
# look at the array at index 1 in the main array [ [], [[]]  ] . There are 2 arrays in it [], [[]]. One nested and one deadend. This violates the nesting rule
#
# [ [ [ [[]],[[]]  ], [[]] ] , [ [] ] ]  -> True
#
# [ [ [ [[]], [[]], []  ], [[]] ] , [ [] ] ]  -> False
#
# Explanation:
#
# first 2 arrays in the main list are both nested, so they are okay. We then check the first one at index 0 [ [ [[]], [[]], []  ], [[]] ]. It has 2 arrays: [ [[]], [[]], []  ] and [[]]. Both nested, so they are fine. We go deeper into the first one out of these two. It has three arrays: [[]], [[]], []. This violates the rule because first two are nested but the last one is deadend. They must be all either nested or deadends.
#
# [ [], [[], [], []] , [] ] -> False
# Explanation:
#
# there are three arrays in the main array [], [[], [], []] , []. 2 are dead ends but one is nested, which is inconsistent.
#
# Please, be sure to check out my other katas:
#
# Highest Average Depth,
# The Hackers' Taunt,
# Sorting Singularly Nested Lists by Depth
# ListsArraysRecursionTrees
# Solution
def is_cleanly_nested(arr):
    if not arr: return True
    kinds = set()
    for child in arr:
        if not isinstance(child, list): return False
        kinds.add(bool(child))
    if len(kinds) > 1: return False
    return all(is_cleanly_nested(child) for child in arr)