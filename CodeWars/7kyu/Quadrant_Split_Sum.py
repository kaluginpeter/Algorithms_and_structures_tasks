# Overview
# A field is about to be divided into 4 equal sections by two perpendicular roads crossing through the center.
#
# The field is represented by a rectangular grid of integers, where each number represents the land value of a parcel.
#
# Task
# Given a grid area (list[list[int]]), return the maximum total land value among the four sections.
#
# Any parcel occupied by the roads is not part of any section.
#
# For odd dimensions, the middle row/column is occupied by the roads.
# For even dimensions, the roads pass between the two middle rows/columns.
# Notes
# The grid is guaranteed to be rectangular
# Input constraints : 2 <= grid rows, grid columns <= 100
# Values can be negative
# Example
# 1. [[4,6,7,2],          4 6 | 7 2
#     [0,3,7,6],    =>    0 3 | 7 6
#     [7,9,4,2],          ----+-----
#     [1,1,2,0]]          7 9 | 4 2
#                         1 1 | 2 0
#
#     Output : 22 (7+2+7+6)
#
# 2. [[0,0,3,4,1],        0 0 | 4 1
#     [6,8,9,1,4],        6 8 | 1 4
#     [9,0,3,6,1],   =>   ----+----
#     [8,2,4,6,3],        8 2 | 6 3
#     [1,6,3,7,8]]        1 6 | 7 8
#
#     Output : 24 (6+3+7+8)
#
# 3. [[2,5,1,0,4,5],      2 5 1 | 0 4 5
#     [5,6,8,1,3,0],      5 6 8 | 1 3 0
#     [5,9,1,3,7,4],  =>  ------+------
#     [8,9,1,2,4,5],      8 9 1 | 2 4 5
#     [3,5,7,0,1,2]]      3 5 7 | 0 1 2
#
#     Output : 33 (8+9+1+3+5+7)
#
# FundamentalsArraysMatrix
# Solution
def max_land_value(area : list[list[int]]) -> int :
    n: int = len(area)
    m: int = len(area[0])
    bucket: list[list[int]] = [[0, 0], [0, 0]]
    for i in range(n):
        if (n & 1) and i == (n >> 1): continue
        for j in range(m):
            if (m & 1) and j == (m >> 1): continue
            x: int = i >= (n >> 1)
            y: int = j >= (m >> 1)
            bucket[x][y] += area[i][j]
    return max(iter(max(quad) for quad in bucket), default=0)