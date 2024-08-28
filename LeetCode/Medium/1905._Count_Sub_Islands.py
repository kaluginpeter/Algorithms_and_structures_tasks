# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
#
# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
#
# Return the number of islands in grid2 that are considered sub-islands.
#
#
#
# Example 1:
#
#
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
# Example 2:
#
#
# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
#
#
# Constraints:
#
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] and grid2[i][j] are either 0 or 1.
# Solution Depth First Search Memoization O(NM) O(NM)
class Solution:
    def sub_islands(self, pos, mtrx, seen, points: list[tuple[int, int]]) -> None:
        if (
                pos in seen or
                not (0 <= pos[0] < len(mtrx)) or
                not (0 <= pos[1] < len(mtrx[0])) or
                mtrx[pos[0]][pos[1]] == 0
        ):
            return
        seen.add(pos)
        points.append((pos[0], pos[1]))
        next_row: int = pos[0]
        next_col: int = pos[1]
        self.sub_islands((next_row - 1, next_col), mtrx, seen, points)
        self.sub_islands((next_row + 1, next_col), mtrx, seen, points)
        self.sub_islands((next_row, next_col - 1), mtrx, seen, points)
        self.sub_islands((next_row, next_col + 1), mtrx, seen, points)

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        seen: set[int] = set()
        valid_sub_islands: int = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and (row, col) not in seen:
                    points: list[tuple[int, int]] = []
                    self.sub_islands((row, col), grid2, seen, points)
                    valid_sub_islands += all(grid1[r][c] == 1 for r, c in points)
        return valid_sub_islands