# Given the root of a binary tree, each node in the tree has a distinct value.
#
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
#
# Return the roots of the trees in the remaining forest. You may return the result in any order.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# Example 2:
#
# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
#
#
# Constraints:
#
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.
# Solutions

# HashTable
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
    nodes: dict[int, TreeNode] = {}

    def dfs(self, root: TreeNode, to_delete: set[int]):
        if not root: return
        if root.val in to_delete:
            if root.val in self.nodes:
                del self.nodes[root.val]
            if root.left:
                self.nodes[root.left.val] = root.left
            if root.right:
                self.nodes[root.right.val] = root.right
            self.dfs(root.left, to_delete)
            self.dfs(root.right, to_delete)
            return None
        else:
            root.left = self.dfs(root.left, to_delete)
            root.right = self.dfs(root.right, to_delete)
            return root

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.nodes.clear()
        to_delete: set[int] = set(to_delete)
        if root.val not in to_delete:
            self.nodes[root.val] = root
        self.dfs(root, to_delete)

        return self.nodes.values()

# Array
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
    nodes: list[TreeNode] = []

    def dfs(self, root: TreeNode, to_delete: bool, targets: set[int]):
        if not root: return
        to_be_deleted: bool = root.val in targets
        if to_delete and not to_be_deleted:
            self.nodes.append(root)
        root.left = self.dfs(root.left, to_be_deleted, targets)
        root.right = self.dfs(root.right, to_be_deleted, targets)
        return None if to_be_deleted else root

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.nodes.clear()
        targets = set(to_delete)
        self.dfs(root, True, targets)

        return self.nodes