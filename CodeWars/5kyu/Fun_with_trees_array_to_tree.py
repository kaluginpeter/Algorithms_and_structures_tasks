# You are given an array of integers. Implement a function which creates a complete binary tree from the array (complete meaning that every level of the tree, except possibly the last, is completely filled).
#
# The elements of the array are to be taken left-to-right, and put into the tree top-to-bottom, left-to-right.
#
# For example, given the array [17, 0, -4, 3, 15] you should create the following tree:
#
#     17
#    /  \
#   0   -4
#  / \
# 3   15
# A tree node type is preloaded for you:
#
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
# This kata is part of fun with trees series:
#
# Fun with trees: max sum
# Fun with trees: array to tree
# Fun with trees: is perfect
# TREESARRAYSBINARY TREESDATA STRUCTURESALGORITHMS
# Solution
from preloaded import Node


def array_to_tree(arr):
    if not arr: return None
    head = Node(arr[0])
    current_nodes: list = [head]
    next_nodes: list = []
    idx: int = 1
    while idx < len(arr):
        for node in current_nodes:
            if idx < len(arr):
                node.left = Node(arr[idx])
                next_nodes.append(node.left)
                idx += 1
            if idx < len(arr):
                node.right = Node(arr[idx])
                next_nodes.append(node.right)
                idx += 1
        current_nodes = next_nodes
        next_nodes = []
    return head