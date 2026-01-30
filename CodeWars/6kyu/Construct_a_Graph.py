# Task
# Given a list of points, construct a graph that includes all of those points and the position (0, 0).
#
# Points will be dictionaries like so: {"x": 1, "y": -1}.
#
# A graph should be represented as a 2d array.
#
# Example:
# Input:
# construct_graph([{"x": 2, "y": 2}, {"x": -2, "y": -2}])
#
# Output:
# [
#   [' ', ' ', '|', ' ', '*'],
#   [' ', ' ', '|', ' ', ' '],
#   ['-', '-', '+', '-', '-'],
#   [' ', ' ', '|', ' ', ' '],
#   ['*', ' ', '|', ' ', ' '],
# ]
# Points on the graph are represented as '*', and the position (0, 0) is represented by a '+'.
#
# All positions along the x axis should be '-', and all postions along the y axis should be '|'. The rest of the positions should be spaces: ' '.
#
# Also, if a point is on the x or y axis, the default char should be replaced with the point char: '*'.
#
# Example:
# Input:
# construct_graph([{"x": 0, "y": 0}, {"x": 1, "y": 4}])
#
# Output:
# [
#   ['|', '*']
#   ['|', ' '],
#   ['|', ' '],
#   ['|', ' '],
#   ['*', '-']
# ]#  ^
#  # this is (0, 0)
# Graphs should be as minimal as posible while still retaining a rectangular shape. They should be just large enough to include all the points and the position (0, 0).
#
# If no points are given, the graph should just include the position (0, 0). Points might have the same value sometimes.
#
# More Examples:
# Input:
# construct_graph([])
#
# Output:
# [['+']]
# Input:
# construct_graph([{"x": 1, "y": 2}, {"x": 1, "y": 2}])
#
# Output:
# [
#   ['|', '*'],
#   ['|', ' '],
#   ['+', '-']
# ]
# Input:
# construct_graph([{"x": 0, "y": 3}])
#
# Output:
# [
#   ['*'],
#   ['|'],
#   ['|'],
#   ['+']
# ]
# Input:
# construct_graph([{"x": -2, "y": -3}, {"x": 1, "y": -3}])
#
# Output:
# [
#   ['-', '-', '+', '-'],
#   [' ', ' ', '|', ' '],
#   [' ', ' ', '|', ' '],
#   ['*', ' ', '|', '*']
# ]
# GraphsASCII Art
# Solution
def construct_graph(points):
    point_coords = [(p["x"], p["y"]) for p in points]
    xs = [0] + [x for x, _ in point_coords]
    ys = [0] + [y for _, y in point_coords]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    def to_grid(x, y):
        col = x - min_x
        row = max_y - y
        return row, col
    if min_y <= 0 <= max_y:
        r, _ = to_grid(0, 0)
        for c in range(width): grid[r][c] = '-'
    if min_x <= 0 <= max_x:
        _, c = to_grid(0, 0)
        for r in range(height): grid[r][c] = '|'
    r0, c0 = to_grid(0, 0)
    grid[r0][c0] = '+'
    for x, y in point_coords:
        r, c = to_grid(x, y)
        grid[r][c] = '*'
    return grid