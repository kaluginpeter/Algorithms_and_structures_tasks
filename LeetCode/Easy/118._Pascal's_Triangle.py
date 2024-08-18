# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Example 1:
#
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
#
# Input: numRows = 1
# Output: [[1]]
#
# Constraints:
# 1 <= numRows <= 30
# Solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row, l = [1], [[1]]
        for i in range(numRows - 1):
            row = [sum(i) for i in zip([0] + row, row + [0])]
            l.append(row)
        return l
# Solution 2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row, triangle = [1], [[1]]
        for i in range(numRows-1):
            row = [x + y for x, y in zip([0] + row, row + [0])]
            triangle.append(row)
        return triangle