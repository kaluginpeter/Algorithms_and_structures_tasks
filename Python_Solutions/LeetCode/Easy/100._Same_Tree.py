# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
#
#
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if (p is None and q) or (p and q is None): return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
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
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        current_p_nodes: list[TreeNode] = [p]
        current_q_nodes: list[TreeNode] = [q]

        next_p_nodes: list[TreeNode] = []
        next_q_nodes: list[TreeNode] = []
        while current_p_nodes and current_q_nodes:
            for _ in range(len(current_p_nodes)):
                p_node, q_node = current_p_nodes.pop(), current_q_nodes.pop()
                if p_node == q_node == None: continue
                if (p_node is None and q_node) or (p_node and q_node is None):
                    return False
                if p_node.val != q_node.val: return False

                next_p_nodes.append(p_node.left)
                next_p_nodes.append(p_node.right)
                next_q_nodes.append(q_node.left)
                next_q_nodes.append(q_node.right)

            current_p_nodes = next_p_nodes
            current_q_nodes = next_q_nodes

        return current_p_nodes == current_q_nodes