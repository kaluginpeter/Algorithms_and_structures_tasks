# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
#
#
# Example 1:
#
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:
#
# Input: matrix = [["0"]]
# Output: 0
# Example 3:
#
# Input: matrix = [["1"]]
# Output: 1
#
#
# Constraints:
#
# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.
# Solution Monotonic Stack O(N**2) O(N)
class Solution:
    def maximalRectangleInHistogram(self, arr: list[int]) -> int:
        arr.append(0)
        stack: list[int] = list()
        ans: int = 0
        for idx in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[idx]:
                h: int = arr[stack.pop()]
                w: int = idx if not stack else idx - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(idx)
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        stack: list[int] = [0] * len(matrix[0])
        ans: int = 0
        for rows in matrix:
            for cols in range(len(rows)):
                stack[cols] = 0 if rows[cols] == '0' else stack[cols] + int(rows[cols])
            ans = max(ans, self.maximalRectangleInHistogram(stack))
        return ans