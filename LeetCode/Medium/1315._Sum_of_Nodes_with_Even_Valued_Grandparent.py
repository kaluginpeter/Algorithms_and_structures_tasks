# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.
#
# A grandparent of a node is the parent of its parent if it exists.
#
#
#
# Example 1:
#
#
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
# Example 2:
#
#
# Input: root = [1]
# Output: 0
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100
# Solution

# DFS
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
    sum_even_nodes: int = 0

    def dfs(self, root, is_even: bool) -> None:
        if root is None: return
        if is_even:
            if root.left: self.sum_even_nodes += root.left.val
            if root.right: self.sum_even_nodes += root.right.val
        self.dfs(root.left, root.val & 1 == 0)
        self.dfs(root.right, root.val & 1 == 0)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs(root, False)
        return self.sum_even_nodes

# BFS
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
from collections import deque
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        grandparents = deque()
        current_nodes = deque()
        current_nodes.append(root)
        sum_even_nodes: int = 0
        while current_nodes:
            grandparent: bool = bool(grandparents and grandparents.popleft() & 1 == 0)
            current_node = current_nodes.popleft()
            if current_node:
                if current_node.left:
                    if grandparent: sum_even_nodes += current_node.left.val
                    grandparents.append(current_node.val)
                    current_nodes.append(current_node.left)
                if current_node.right:
                    if grandparent: sum_even_nodes += current_node.right.val
                    grandparents.append(current_node.val)
                    current_nodes.append(current_node.right)
        return sum_even_nodes