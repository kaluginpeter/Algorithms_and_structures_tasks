# Context
# In Dungeons and Dragons, a tabletop roleplaying game, movement is limited in combat. Characters can only move a set amount of distance per turn, meaning the distance you travel is very important.
#
# In the 5th edition of the rulebook, the board is commonly organized into a grid, but for ease of counting, movement is non-euclidian. Each square is 5 ft, and moving diagonally counts the same as moving in a cardinal direction.
#
# +------------------------+
# | 10 | 10 | 10 | 10 | 10 |
# +------------------------+
# | 10 |  5 |  5 |  5 | 10 |
# +------------------------+
# | 10 |  5 | :) |  5 | 10 |
# +------------------------+
# | 10 |  5 |  5 |  5 | 10 |
# +------------------------+
# | 10 | 10 | 10 | 10 | 10 |
# +------------------------+
# Distance of each grid cell from the player, in feet
# Your task
# Create an algorithm to calculate the distance of a movement path. You will be provided with the path as a series of absolute grid points (x, y, z). Take in to account both horizontal (x, y) as well as vertical (z) movement. Vertical movement is governed by the same rules, for the sake of simplicity.
#
# ALGORITHMSDATA STRUCTURES
# Solution
def calc_distance(path):
    ans: int = 0
    start = path[0]
    for i in path[1:]:
        ans += max(abs(x - y) for x, y in zip(start, i)) * 5
        start = i
    return ans