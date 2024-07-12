# You are given a binary tree:
#
# class Node:
#     def __init__(self, L, R, n):
#         self.left = L
#         self.right = R
#         self.value = n
# Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.
#
# Return empty list if root is None.
#
# Example 1 - following tree:
#
#                  2
#             8        9
#           1  3     4   5
# Should return following list:
#
# [2,8,9,1,3,4,5]
# Example 2 - following tree:
#
#                  1
#             8        4
#               3        5
#                          7
# Should return following list:
#
# [1,8,4,3,5,7]
# TREESBINARY TREESPERFORMANCEALGORITHMSSORTING
# Solution BFS O(N) O(N)
def tree_by_levels(node):
    output: list[int] = []
    current_nodes: list = [node]
    next_nodes: list = []
    while current_nodes:
        for current_node in current_nodes:
            if current_node is None: continue
            output.append(current_node.value)
            if current_node.left is not None: next_nodes.append(current_node.left)
            if current_node.right is not None: next_nodes.append(current_node.right)
        current_nodes = next_nodes
        next_nodes = []
    return output