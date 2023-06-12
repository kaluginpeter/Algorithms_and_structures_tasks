# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
# Example 1:
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
# Follow up: Could you solve it both recursively and iteratively?
# Solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        def dfs_left(root, res):
            if root is None:
                res.append(None)
                return
            res.append(root.val)
            dfs_left(root.left, res)
            dfs_left(root.right, res)
            return res
        def dfs_right(root, res):
            if root is None:
                res.append(None)
                return
            res.append(root.val)
            dfs_right(root.right, res)
            dfs_right(root.left, res)
            return res
        return dfs_left(root.left, [])==dfs_right(root.right, [])