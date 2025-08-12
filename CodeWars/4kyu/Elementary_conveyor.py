# The conveyor can move parts in four directions: right(r), left(l), up(u) and down(d), wrapping around the border of the grid. There is also one element that is the output of the conveyor(f).
#
# The conveyor is represented by a rectangular list of strings, as shown below:
#
# ["rdfrd",
#  "uluul"]
# During the step, the part moves along the conveyor to an adjacent cell according to the specified direction.
# For each conveyor cell, it is necessary to calculate the number of steps for which the element will reach the output tile f (-1 if this is not possible). The result is returned as a 2D array of integers.
#
# Example:
#
# ["rfl"]   =>  [[1, 0, 1]]
#
# ["rdfrd", =>  [[-1, -1, 0, -1, -1],
#  "uluul"]      [-1, -1, 1, -1, -1]]
#
# ["lfl"]   =>  [[2, 0, 1]]
# Random test parameters:
#
# 102 small tests where 5 <= width, height < 12
# 125 large tests where 200 <= width, height < 220
# PerformanceFundamentals