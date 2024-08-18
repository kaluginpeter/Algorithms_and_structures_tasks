# You are given a binary tree. Implement a function that returns the maximum sum of a route from root to leaf.
#
# For example, given the following tree:
#
#     17
#    /  \
#   3   -10
#  /    /  \
# 2    16   1
#          /
#         13
# The function should return 23, since 17 -> -10 -> 16 is the route from root to leaf with the maximum sum.
#
# Return 0 if the tree is empty.
#
# Please note that you are not to find the best possible route in the tree, but the best possible route from root to leaf, e.g. for the following tree, you cannot skip the leaves and return 5 + 10 = 15: the expected answer is 5 + 4 + -60 = -51
#
#         5
#       /   \
#     4      10
#    / \     /
# -80 -60 -90
# A tree node type is preloaded for you:
#
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
# This kata is part of fun with trees series:
#
# Fun with trees: max sum
# Fun with trees: array to tree
# Fun with trees: is perfect
# TREESRECURSIONBINARY TREESBINARY SEARCH TREESDATA STRUCTURESALGORITHMS
# Solution
from preloaded import TreeNode

def max_sum(root: TreeNode) -> int:
    ans: int = float('-inf')
    def dfs(root, top: int = 0):
        if not root:
            return
        if not root.left and not root.right:
            nonlocal ans
            ans = max(ans, top + root.value)
        if root.left:
            dfs(root.left, top + root.value)
        if root.right:
            dfs(root.right, top + root.value)
    dfs(root)
    return ans if root else 0