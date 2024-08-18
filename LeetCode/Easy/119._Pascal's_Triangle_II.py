# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Example 1:
#
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
#
# Input: rowIndex = 0
# Output: [1]
# Example 3:
#
# Input: rowIndex = 1
# Output: [1,1]
#
# Constraints:
# 0 <= rowIndex <= 33
#
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
# Solution
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row = [sum(x) for x in zip([0] + row, row + [0])]
        return row
# Solution 2
class Solution(object):
    def getRow(self, r):
        ans = [1]*(r+1);
        up = r
        down = 1
        for i in range(1, r):
            ans[i] = int(ans[i-1]*up/down);
            up = up - 1
            down = down + 1
        return ans;
# Solution 3 Speed O(N), Memory O(1)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row = [x + y for x,y in zip([0] + row, row + [0])]
        return row