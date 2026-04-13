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
# Solution
from math import dist  # Euclidean distance function


def delivery_route(houses: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Find the optimal route between all points in the array."""
    n = len(houses)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)): continue
            for v in range(n):
                if mask & (1 << v): continue
                new_mask = mask | (1 << v)
                new_cost = dp[mask][u] + dist(houses[u], houses[v])
                if new_cost < dp[new_mask][v]:
                    dp[new_mask][v] = new_cost
                    parent[new_mask][v] = u
    full_mask = (1 << n) - 1
    best_cost = float('inf')
    last = -1
    for i in range(1, n):
        cost = dp[full_mask][i] + dist(houses[i], houses[0])
        if cost < best_cost:
            best_cost = cost
            last = i
    path = []
    mask = full_mask
    while last != -1:
        path.append(last)
        prev = parent[mask][last]
        mask ^= (1 << last)
        last = prev
    path.reverse()
    return [houses[i] for i in path] + [houses[0]]