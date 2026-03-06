# If you haven't already done so, you should do the 5x5 and 15x15 Nonogram solvers first.
#
# In this kata, you have to solve nonograms from any size up to one with an average side length of 50. The nonograms are not all square. However, they all will be valid and should only have one solution.
#
# I highly recommend not to try and use a brute force solution as some of the grids are very big. Also, you may not be able to solve all the grids by deduction alone so may have to guess one or two squares. :P
#
# You will be given three arguments: The clues, the width, and the height:
#
# # clues is given in the same format as the previous two nonogram katas:
# clues = (tuple((column_clues,) for column_clues in column),
#          tuple((row_clues,) for row_clues in row))
#
# # width is the width of the puzzle (distance from left to right)
# width = width_of_puzzle
#
# # height is the height of the puzzle (distance from top to bottom)
# height = height_of_puzzle
# and you will have to finish the function:
#
# def solve(clues, width, height):
#     pass
# You should return an array of arrays (or equivalent for your language) of the solved grid, see the tests for details.
#
# For example, the second example test case looks like:
#
# Img
#
# Therefore, you would be given the arguments:
#
# clues = (((3,), (4,), (2, 2, 2), (2, 4, 2), (6,), (3,)),
#          ((4,), (6,), (2, 2), (2, 2), (2,), (2,), (2,), (2,), (), (2,), (2,)))
# width = 6
# height = 11
# Zero will be given as an array (or equivalent).
#
# Test sizes:
# You will be given 60 random tests in total. There will be:
#
# 35 small tests: 3 < the average of the side lengths <= 25
# 15 medium tests: 25 < the average of the side lengths <= 35
# 10 big tests: 40 <= the average of the side lengths <= 50
# Good luck :)
#
# AlgorithmsLogicGamesGame Solvers