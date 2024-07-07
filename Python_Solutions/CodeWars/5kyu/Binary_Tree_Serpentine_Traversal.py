# Given the root node of a binary tree, write a function that will traverse the tree in a serpentine fashion. You could also think of this as a zig-zag.
#
# We want to visit the first level from left to right, the second level from right to left, third level from left to right, and so on...
#
# The function will return a list of the visited nodes in serpentine order.
#
# The tree is not necessarily balanced. It is very important that you start the first level from left to right!
#
# A Node has 3 properties: data (a number or string) left (a reference to the left child) right (a refencence to the right child)
#
# The empty reference if there is no child is undefined (JS) / None (Python)
#
# Example:
#
#     A
#    /\
#   B  C
#  /\  /\
# D E F G
# Should result in ["A", "C", "B", "D", "E", "F", "G"]
#
# BINARY TREESTREESRECURSIONALGORITHMS
# Solution BFS O(N) O(N)
from preloaded import Node

def serpentine_traversal(root_node : Node) -> list:
    reverse: bool = False
    current_nodes: list[Node] = [root_node]
    next_nodes: list[Node] = []
    output: list[Node] = []
    while current_nodes:
        for node in current_nodes[::-1]:
            if node is None: continue
            output.append(node.data)
            if reverse is False:
                if node.left is not None: next_nodes.append(node.left)
                if node.right is not None: next_nodes.append(node.right)
            else:
                if node.right is not None: next_nodes.append(node.right)
                if node.left is not None: next_nodes.append(node.left)
        reverse = not reverse
        current_nodes = next_nodes
        next_nodes = []
    return output