# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
# Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            if not isinstance(curr, TreeNode):
                res.append(curr)
                continue
            if curr.right is not None:
                stack.append(curr.right)
            stack.append(curr.val)
            if curr.left is not None:
                stack.append(curr.left)
        return res


# Solution 2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []