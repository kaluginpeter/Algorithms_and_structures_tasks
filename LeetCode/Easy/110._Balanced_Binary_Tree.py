# Given a binary tree, determine if it is
# height-balanced
# .
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:
#
# Input: root = []
# Output: true
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104
# Solution DFS O(N) O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root: return 0
        left_subtree = self.dfs(root.left)
        right_subtree = self.dfs(root.right)
        if left_subtree < 0 or right_subtree < 0 or abs(left_subtree - right_subtree) > 1:
            return -1
        return max(left_subtree, right_subtree) + 1

    def isBalanced(self, root: Optional[TreeNode], current_depth: int = 0) -> bool:
        return self.dfs(root) >= 0