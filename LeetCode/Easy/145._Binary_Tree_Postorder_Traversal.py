# Given the root of a binary tree, return the postorder traversal of its nodes' values.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [3,2,1]
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
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
# Solution
# Recursive way
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
    def postorderTraversal(self, root: Optional[TreeNode], order: list[int] = None) -> List[int]:
        if order is None:
            order = []
        if not root: return order
        self.postorderTraversal(root.left, order)
        self.postorderTraversal(root.right, order)
        order.append(root.val)
        return order

# Iterative way
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order: list[int] = []
        queue: list[TreeNode] = [(root, False)]
        while queue:
            cur_root, seen = queue.pop()
            if cur_root and not seen:
                queue += [(cur_root, True), (cur_root.right, False), (cur_root.left, False)]
            elif cur_root:
                order.append(cur_root.val)
        return order