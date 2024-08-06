# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
# 1 <= n <= 8
# Solution Backtracking Recursive O(4**N) O(4**N)
class Solution:
    def backtrack(self, n: int, left: int, right: int, output: list[str], result: list[str]) -> None:
        if left >= n and right >= n:
            result.append(''.join(output))

        if left < n:
            output.append('(')
            self.backtrack(n, left + 1, right, output, result)
            output.pop()
        if right < left:
            output.append(')')
            self.backtrack(n, left, right + 1, output, result)
            output.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        result: list[str] = []
        output: list[str] = []
        self.backtrack(n, 0, 0, output, result)
        return result