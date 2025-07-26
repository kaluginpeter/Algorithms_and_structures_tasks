# Description
# Below is described a skill tree:
#
# Tree
# The array that describes this skill tree is as follows:
#
# [
#  0, # 0 is the root and does not depend on any skill.
#  0, # 1 is unlocked by skill 0 (skill at index 0).
#  0, # 2 is unlocked by skill 0.
#  1, # 3 is unlocked by skill 1.
#  3, # 4 is unlocked by skill 3.
#  3, # 5 is unlocked by skill 3.
#  2  # 6 is unlocked by skill 2.
# ]
# In another words, each skill is identified by its index in the array, and its value identifies the skill that unlocks it.
#
# Your Task:
# Given a skill tree described as an array and a set of required skills, return the total number of skills needed to learn all of the required skills.
#
# Intuition: In the example's tree, if I want to learn skill 6, I first need to learn skills 0 and 2 - a total of 3 skills learned.
#
# Examples:
# count_skills([ 0, 0, 0, 1, 3, 3, 2 ], { 6 })     -> 3
# count_skills([ 0, 0, 0, 1, 3, 3, 2 ], set())     -> 0
# count_skills([ 0, 0, 0, 1, 3, 3, 2 ], { 1, 2 })  -> 3
# Constraints:
# Each skill is only unlocked by exactly one skill!
# Skills can unlock any number of skills.
# Inputs are always valid and each skill can be unlocked by some other skill, except 0.
# 0
# ≤
# l
# e
# n
# (
# t
# r
# e
# e
# )
# ≤
# 200
#  
# 000
# 0≤len(tree)≤200000
# 0
# ≤
# l
# e
# n
# (
# r
# e
# q
# u
# i
# r
# e
# d
# )
# ≤
# l
# e
# n
# (
# t
# r
# e
# e
# )
# 0≤len(required)≤len(tree)
# Notes:
# You need to be somewhat efficient with your approach.
# You are provided with 2 functions in preloaded to help you debug:
# build_tree/buildTree - convert a tree array into a dict/Map describing which skills each skill unlocks.
# visualize_tree/visualiseTree/visualizeTree - get a visual representation of the given tree array.
# AlgorithmsData StructuresGraph TheoryTrees