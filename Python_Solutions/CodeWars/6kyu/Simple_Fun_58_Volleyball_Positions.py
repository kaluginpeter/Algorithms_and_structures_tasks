# Task
# You are watching a volleyball tournament, but you missed the beginning of the very first game of your favorite team. Now you're curious about how the coach arranged the players on the field at the start of the game.
#
# The team you favor plays in the following formation:
#
# 0 3 0
# 4 0 2
# 0 6 0
# 5 0 1
# where positive numbers represent positions occupied by players. After the team gains the serve, its members rotate one position in a clockwise direction, so the player in position 2 moves to position 1, the player in position 3 moves to position 2, and so on, with the player in position 1 moving to position 6.
#
# Here's how the players change their positions:
#
#
#
# Given the current formation of the team and the number of times k it gained the serve, find the initial position of each player in it.
#
# Example
# For
#
# formation = [["empty",   "Player5", "empty"],
#              ["Player4", "empty",   "Player2"],
#              ["empty",   "Player3", "empty"],
#              ["Player6", "empty",   "Player1"]]
# and k = 2
# the output should be
#
# [
#     ["empty",   "Player1", "empty"],
#     ["Player2", "empty",   "Player3"],
#     ["empty",   "Player4", "empty"],
#     ["Player5", "empty",   "Player6"]
# ]
# For
#
# formation = [["empty", "Alice", "empty"],
#              ["Bob",   "empty", "Charlie"],
#              ["empty", "Dave",  "empty"],
#              ["Eve",   "empty", "Frank"]]
# and k = 6
# the output should be
#
#   [
#     ["empty", "Alice", "empty"],
#     ["Bob",   "empty", "Charlie"],
#     ["empty", "Dave",  "empty"],
#     ["Eve",   "empty", "Frank"]
# ]
# Input
# 2D string array formation
#
# A 4 × 3 array of strings representing names of the players in the positions corresponding to those in the schema above.
#
# It is guaranteed that for each empty position the corresponding element of formation is "empty".
#
# It is also guaranteed that there is no player called "empty" in the team.
#
# Integer k
#
# The number of times the team gained the serve.
#
# Constraints: 0 ≤ k ≤ 1000000000.
#
# Output
# 2D string array
#
# Team arrangement at the start of the game.
#
# PUZZLES
# Solution
def volleyball_positions(formation, k):
    steps: int = k % 6
    mtrx_moves: list = [[3, 2], [2, 1], [3, 0], [1, 0], [0, 1], [1, 2]]
    new_mtrx: list = list()
    for rows in range(4):
        top: list = list()
        for columns in range(3):
            if formation[rows][columns] != 'empty':
                idx: int = (mtrx_moves.index([rows, columns]) + steps)
                if idx > 5:
                    idx %= 6
                top.append(formation[mtrx_moves[idx][0]][mtrx_moves[idx][1]])
            else:
                top.append(formation[rows][columns])
        new_mtrx.append(top)
    return new_mtrx