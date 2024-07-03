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