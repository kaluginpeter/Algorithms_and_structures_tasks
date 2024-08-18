# Your task is simple enough. You will write a function which takes a tree as its input. Your function should output one string with the values of the nodes in an order corresponding to a breadth first search. This string also should be broken into levels corresponding to the depth of the nodes tree, and there should be a space between each value. For example if the following tree were input to our function :
#
# alt text
#
# the output would be a string and look something like this:
#
# 2
# 7 5
# 2 6 9
# 5 11 4
# All nodes in the tree will have two properties, .value and .children. You may assume the .value property will always be either a string or a number. The .children property will be an array containing all of the node's children. The tree is NOT necessarily a binary tree, each node may have many children nodes
#
# You may implement whatever method you see fit to search the tree. There are both breadth first and depth first approaches.
#
# ALGORITHMS
# Solution
# preloaded TreeNode class:
"""
class TreeNode:
    def __init__(self, value, children = None):
        self.value = value
        self.children = [] if children is None else children
"""
from preloaded import TreeNode

def tree_printer(tree : TreeNode) -> str:
    current_nodes = []
    next_nodes = []
    current_nodes.append(tree)
    output_array: list[str] = []
    while current_nodes:
        local_array: list[str] = []
        for node in current_nodes:
            local_array.append(node.value)
            if node.children is not None:
                next_nodes.extend(node.children)
        local_array = ' '.join(str(el) for el in local_array)
        output_array.append(local_array)
        current_nodes = next_nodes
        next_nodes = []
    return '\n'.join(output_array)