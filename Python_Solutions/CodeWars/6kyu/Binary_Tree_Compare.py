# Given the node object:
#
# Node:
#   val: <int>,
#   left: <Node> or null,
#   right: <Node> or null
# write a function compare(a, b) which compares the two trees defined by Nodes a and b and returns true if they are equal in structure and in value and false otherwise.
#
# Examples:
#
# 1       1
# | \     | \
# 2  3    2  3
# => true
#
# 1       1
# | \     | \
# 3  3    2  3
# => false (values not the same 2 != 3)
#
# 1       1
# | \     |
# 2  3    2
#         |
#         3
# => false (structure not the same)
# BINARY TREESALGORITHMS
# Solution
def compare(a, b):
    if (a and not b) or (not a and b): return False
    a_current_nodes: list = [a]
    b_current_nodes: list = [b]
    a_next_nodes: list = []
    b_next_nodes: list = []
    while a_current_nodes or b_current_nodes:
        for x, y in zip(a_current_nodes, b_current_nodes):
            if x and y:
                if x.val != y.val: return False
                if not (bool(x.right) == bool(y.right) and bool(x.left) == bool(y.left)): return False
                if x.left: a_next_nodes.append(x.left)
                if x.right: a_next_nodes.append(x.right)
                if y.left: b_next_nodes.append(y.left)
                if y.right: b_next_nodes.append(y.right)
        if (x and not y) or (not x and y): return False
        if len(a_next_nodes) != len(b_next_nodes): return False
        a_current_nodes, b_current_nodes = a_next_nodes, b_next_nodes
        a_next_nodes, b_next_nodes = [], []
    return True