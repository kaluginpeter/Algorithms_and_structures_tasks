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
    def dfs(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return root1 == root2 == None
        if root1.val != root2.val:
            return False
        left_side: bool = self.dfs(root1.left, root2.right)
        right_side: bool = self.dfs(root1.right, root2.left)
        return left_side and right_side

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)

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

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack: list[TreeNode] = [root.right, root.left]
        while stack:
            current_left: TreeNode = stack.pop()
            current_right: TreeNode = stack.pop()
            if current_left is None or current_right is None:
                if current_left == current_right == None:
                    continue
                return False
            elif current_left.val != current_right.val:
                return False
            stack.append(current_right.right)
            stack.append(current_left.left)
            stack.append(current_right.left)
            stack.append(current_left.right)

        return True