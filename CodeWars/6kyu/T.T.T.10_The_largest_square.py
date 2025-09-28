# Task
# Give you a 2D array wall:
#
# [
# ["X"," "," "," "," "," "],
# [" "," "," "," "," "," "],
# [" "," "," "," "," "," "],
# [" "," "," "," "," "," "],
# [" "," "," "," "," "," "],
# [" "," "," "," "," "," "]
# ]
# " " is the blank part, "X" is the hole in the wall, please find the largest square (no hole) on the wall, return its area.
#
# The above example should return 25, because the maximum square that can be found is 5X5
#
# Please see more example in testcases.
#
# PuzzlesGames
# Solution
def _max(wall):
    n: int = len(wall)
    m: int = len(wall[0])
    dp: list[list[int]] = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if wall[i][j] == 'X': continue
            dp[i][j] = min(
                (dp[i][j - 1] if j else 0),
                (dp[i - 1][j] if i else 0),
                (dp[i - 1][j - 1] if i and j else 0)
            ) + 1
    return max((max(row, default=0) for row in dp), default=0)**2