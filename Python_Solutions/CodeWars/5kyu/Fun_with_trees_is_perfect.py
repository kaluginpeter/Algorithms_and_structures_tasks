# A perfect binary tree is a binary tree in which all interior nodes have two children and all leaves have the same depth or same level.
#
# You are given a class called TreeNode. Implement the method isPerfect which determines if a given tree denoted by its root node is perfect.
#
# Note: TreeNode class contains helper methods for tree creation, which might be handy for your solution. Feel free to update those methods, but make sure you keep their signatures intact (since they are used from within test cases).
#
# You can (and should) add more tests to validate your solution, since not all cases are covered in the example test cases.
#
# This kata is part of fun with trees series:
#
# Fun with trees: max sum
# Fun with trees: array to tree
# Fun with trees: is perfect
# TREESRECURSIONBINARY TREESBINARY SEARCH TREESDATA STRUCTURESALGORITHMS
# Solution BFS(Breadth-First-Search) Math O(N) O(M) where M is length of layer nodes
from preloaded import TreeNode
# preloaded TreeNode class:
"""
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left  = left
        self.right = right
"""
def is_perfect(tree : TreeNode) -> bool:
    current_nodes = [tree]
    next_nodes = []
    while current_nodes:
        count_parent_nodes: int = len(current_nodes)
        for parent_node in current_nodes:
            if parent_node is None: continue
            if parent_node.left is not None: next_nodes.append(parent_node.left)
            if parent_node.right is not None: next_nodes.append(parent_node.right)
        if count_parent_nodes * 2 != len(next_nodes) and next_nodes: return False
        current_nodes = next_nodes
        next_nodes = []
    return True