# Given the root of a binary tree, return the sum of values of its deepest leaves.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Example 2:
#
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100
# Solution
# Breath First Search (BFS)
# General idea
# Traverse through all layers of tree.
# At the each layer calculate sum of its leaves(variable "current_layer_leaves_sum") and
# if sum more than 0, just store it in global variable "sum_leaves".
# At the end return global variable "sum_leaves"
# Complexity
# Time complexity: O(N)
# Space complexity: O(M) where M is length of layer nodes
# Code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        current_nodes: list[TreeNode] = [root]
        next_nodes: list[TreeNode] = []
        sum_leaves: int = 0
        while current_nodes:
            current_layer_leaves_sum: int = 0
            for node in current_nodes:
                if node is None: continue
                if node.left is not None: next_nodes.append(node.left)
                if node.right is not None: next_nodes.append(node.right)
                if node.left is None and node.right is None:
                    current_layer_leaves_sum += node.val
            current_nodes = next_nodes
            next_nodes = []
            if current_layer_leaves_sum:
                sum_leaves = current_layer_leaves_sum
        return sum_leaves

# Depth First Search (DFS)
# General idea
# Traverse through all nodes of tree by "postorder" traverse.
# At the each node store variable represent current depth/level of tree and
# if current depth/level more than global variable "current_max_depth" - we should
# change value of "current_max_depth" on current depth and change sum
# global variable "sum_leaves" to current node value.
# If depth/level of current node is equal with "current_max_depth" - we just
# increment variable "sum_leaves" by current node value. At the end of DFS traversing, just return "sum_leaves"
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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        current_max_depth: int = 0
        sum_leaves: int = 0
        def dfs(root, depth):
            if root is None: return
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            nonlocal current_max_depth, sum_leaves
            if depth > current_max_depth:
                current_max_depth = depth
                sum_leaves = root.val
            elif depth == current_max_depth:
                sum_leaves += root.val
        dfs(root, depth=current_max_depth)
        return sum_leaves