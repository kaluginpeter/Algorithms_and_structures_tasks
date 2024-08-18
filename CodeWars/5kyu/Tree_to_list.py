# Given the root of a tree with an arbitrary number of child nodes, return a list containing the nodes' data in breadth-first order (left to right, top to bottom).
#
# Child nodes are stored in a list. An empty tree is represented by an empty list.
#
# Example:
#
#            1
#           / \
#          2   3  -> [1,2,3,4,5,6,7]
#         /|\   \
#        4 5 6   7
# TREESFUNDAMENTALS
# Solution Breadth First Search O(N) O(N)
class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = [] if child_nodes is None else child_nodes

def tree_to_list(tree_root):
    current: list = [tree_root]
    nxt: list = list()
    answer: list = list()
    while current:
        for node in current:
            if not node: continue
            answer.append(node.data)
            nxt.extend(node.child_nodes)
        current = nxt
        nxt = []
    return answer