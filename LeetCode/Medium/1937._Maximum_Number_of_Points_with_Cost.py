# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
#
# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
#
# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
#
# Return the maximum number of points you can achieve.
#
# abs(x) is defined as:
#
# x for x >= 0.
# -x for x < 0.
#
#
# Example 1:
#
#
# Input: points = [[1,2,3],[1,5,1],[3,1,1]]
# Output: 9
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
# You add 3 + 5 + 3 = 11 to your score.
# However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
# Your final score is 11 - 2 = 9.
# Example 2:
#
#
# Input: points = [[1,5],[2,3],[4,2]]
# Output: 11
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
# You add 5 + 3 + 4 = 12 to your score.
# However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
# Your final score is 12 - 1 = 11.
#
#
# Constraints:
#
# m == points.length
# n == points[r].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 0 <= points[r][c] <= 105
# Solution Dynamic Programming O(NM) O(M)
# Suggested problems:
# 121. Best Time to Buy and Sell Stock
# 1014. Best Sightseeing Pair
# 931. Minimum Falling Path Sum
# Complexity
# Time complexity: O(NM)
# Space complexity: O(M)
# Code
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        r, c = len(points), len(points[0])
        for row in range(1, r):
            # Best points from rightmost to left
            right: list[int] = [0] * c
            right[-1] = points[row - 1][-1]
            for col in range(c - 2, -1, -1):
                right[col] = max(right[col + 1] - 1, points[row - 1][col])
            # Best poitns from leftmost to right
            left: int = points[row - 1][0]
            # First element either with first left or first right points
            points[row][0] += max(left, right[0])

            for col in range(1, c):
                # Prev max point will be decrease by one every iteration
                # Choose max from either descreased prev max or point above
                left = max(left - 1, points[row - 1][col])
                # Add maximum point to current ceil
                points[row][col] += max(left, right[col])

        return max(points[-1])