# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
# Solution
# Dfs recursive way
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
    def preorderTraversal(self, root: Optional[TreeNode], order: list[int] = None) -> List[int]:
        if order is None: order = []
        if not root: return order
        order += [root.val]
        self.preorderTraversal(root.left, order)
        self.preorderTraversal(root.right, order)
        return order

# Dfs iterative way
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
    def preorderTraversal(self, root: Optional[TreeNode], order: list[int] = None) -> List[int]:
        order: list[int] = []
        queue: list[TreeNode] = [root]
        while queue:
            cur_root: TreeNode = queue.pop()
            if not cur_root: continue
            order.append(cur_root.val)
            queue.append(cur_root.right)
            queue.append(cur_root.left)
        return order