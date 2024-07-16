# You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
#
# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
#
# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.
#
#
#
# Example 1:
#
#
# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
# Example 2:
#
#
# Input: root = [2,1], startValue = 2, destValue = 1
# Output: "L"
# Explanation: The shortest path is: 2 → 1.
#
#
# Constraints:
#
# The number of nodes in the tree is n.
# 2 <= n <= 105
# 1 <= Node.val <= n
# All the values in the tree are unique.
# 1 <= startValue, destValue <= n
# startValue != destValue

# Iterative DFS
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, target):
        callstack: list = [(root, '')]
        while callstack:
            cur_node, path = callstack.pop()
            if cur_node.val == target:
                return path
            if cur_node.left:
                callstack.append((cur_node.left, path + 'L'))
            if cur_node.right:
                callstack.append((cur_node.right, path + 'R'))

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start: str = self.dfs(root, startValue)
        end: str = self.dfs(root, destValue)
        idx: int = 0
        while idx < len(start) and idx < len(end) and start[idx] == end[idx]:
            idx += 1
        return 'U' * len(start[idx:]) + end[idx:]

# Recursive DFS
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, target, path):
        if not root: return False
        elif root.val == target:
            return True

        path.append('L')
        if self.dfs(root.left, target, path):
            return True
        path.pop()

        path.append('R')
        if self.dfs(root.right, target, path):
            return True
        path.pop()

        return False

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path_to_start_node: list[str] = []
        self.dfs(root, startValue, path_to_start_node)
        path_to_end_node: list[str] = []
        self.dfs(root, destValue, path_to_end_node)
        idx: int = 0
        while (
            idx < len(path_to_start_node)
            and idx < len(path_to_end_node)
            and path_to_start_node[idx] == path_to_end_node[idx]
        ):
            idx += 1
        return 'U' * len(path_to_start_node[idx:]) + ''.join(path_to_end_node[idx:])