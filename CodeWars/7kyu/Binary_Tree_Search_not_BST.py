# Given a number and a binary tree ( not a Binary Search Tree! ):
#
# return True/true if the given number is in the tree
# return False/false if it isn't
# BINARY TREESFUNDAMENTALS
# Solution BFS O(N) O(1)
from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


def search(n: int, root: Optional[Node]) -> bool:
    """ Determines if a value is in a binary tree (NOT bst) """
    return root.value == n or search(n, root.left) or search(n, root.right) if root else False