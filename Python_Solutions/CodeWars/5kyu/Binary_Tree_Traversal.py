# Given the root node of a binary tree (but not necessarily a binary search tree,) write three functions that will print the tree in pre-order, in-order, and post-order.
#
# A Node has the following properties:
#
# data    # A number or a string
# left    # A Node, which is None if there is no left child.
# right   # A Node, which is None if there is no right child.
# Pre-order means that we
# 1.) Visit the root.
# 2.) Traverse the left subtree (left node.)
# 3.) Traverse the right subtree (right node.)
#
# In-order means that we
# 1.) Traverse the left subtree (left node.)
# 2.) Visit the root.
# 3.) Traverse the right subtree (right node.)
#
# Post-order means that we
# 1.) Traverse the left subtree (left node.)
# 2.) Traverse the right subtree (right node.)
# 3.) Visit the root.
#
# Let's say we have three nodes.
#
# a = Node("A")
# b = Node("B")
# c = Node("C")
#
# a.left = b
# a.right = c
# Then, preOrder(a) should return ["A", "B", C"]
# inOrder(a) should return ["B", "A", "C"]
# postOrder(a) should return ["B", "C", A"]
#
# What would happen if we did this?
#
# d = Node("D")
# c.left = d
# preOrder(a) should return ["A", "B", "C", "D"]
# inOrder(a) should return ["B", "A", "D", "C"]
# postOrder(a) should return ["B", "D", "C", "A"]
#
# BINARY TREESTREESRECURSIONDATA STRUCTURESALGORITHMS