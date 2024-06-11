# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The testcases are generated so that the answer will be less than or equal to 2 * 109.
#
#
#
# Example 1:
#
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:
#
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
# Constraints:
#
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.
# Solution Dynamic Programming Bottom Up O(N*M) O(M)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1: return 0
        prev_row = [0] * n
        prev_row[n - 1] = 1
        for row in range(m - 1, -1, -1):
            current_row = [0] * n
            current_row[n - 1] = 0 if obstacleGrid[row][n - 1] == 1 else prev_row[n - 1]
            for col in range(n - 2, -1, -1):
                if obstacleGrid[row][col] == 1: continue
                current_row[col] = current_row[col + 1] + prev_row[col]
            prev_row = current_row
        return prev_row[0]