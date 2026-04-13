# The Santa Express
# Story
# You have been hired by Santa's Workshop Inc. Specifically, you work in the package delivery branch, internally nicknamed as The Santa Express. It is a delivery service with many elves, each delivering to a certain neighbourhood. This is more efficient than Santa delivering all the presents, and keeps his stress levels down.
#
# Your role is to analyse the neighbourhoods and find the optimal delivery route for each neighbourhood.
#
# Task
# Your task is to write a function that takes in a list of houses whose coordinates are in the form (x, y) and returns any of the shortest delivery route to deliver all the presents in time for Christmas, using Euclidean distance. The route should start and end at Santa's workshop, i.e. (0, 0), and the list will always start with this. You should not modify the input.
#
#
# Constraints
# 2 ≤ length of houses ≤ 13
# Expected Time Complexity:
# O
# (
# 2
# n
# ⋅
# n
# 2
# )
# O(2
# n
#  ⋅n
# 2
#  )
# Examples
# [(0, 0), (2, 5), (5, 6)] -> [(0, 0), (2, 5), (5, 6), (0, 0)]
# [(0, 0), (1, 3), (2, 4), (3, 5), (2, 5)] -> [(0, 0), (1, 3), (2, 5), (3, 5), (2, 4), (0, 0)]
# [(0, 0), (3, 7)] -> [(0, 0), (3, 7), (0, 0)]
# Notes
# There is an Euclidean distance function preloaded for you that takes in 2 coordinates of the form (x, y) and returns the Euclidean distance between them.
# There is always at least 2 possible routes.
# There will never be duplicates in the list of houses.
# CombinatoricsPerformance