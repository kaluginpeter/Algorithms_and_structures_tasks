# Some graph theory definitions:
# A graph consists of nodes, also known as vertices (singular: vertex).
# The number of vertices in a graph is called the order of this graph.
# In the kata nodes will be numbered from A0 to A(n-1) for a graph with n nodes.
# Nodes may or may not be connected with one another.
# In our definition below the node "A0" is connected with the node "A3", but "A0" is not connected with "A1".
# The connecting line between two nodes is called an edge.
# If the edges between the nodes are undirected, the graph is called an undirected graph.
# A weighted graph is a graph in which a number (the weight) is assigned to each edge.
# 3 possible graph representations
# Dictionaries
# A graph can be represented as a dictionary:
#
# graph = {
#   'A0': [('A3', 1), ('A5', 4)],
#   'A1': [('A2', 2)],
#   'A2': [('A1', 1), ('A2', 2), ('A3', 1), ('A4', 1)],
#   'A3': [('A0', 1), ('A2', 1)],
#   'A4': [('A2', 1), ('A4', 1)],
#   'A5': [('A3', 3)]
# }
# Here the nodes are A0...A5; following each nodes is the edges list of linked nodes with their weight. A0 is linked to A3 with a weight of 1 and to A5 with weight 4. A dictionary is not ordered but the list of linked nodes is sorted. So:
#
# 'A0': [('A3', 1), ('A5', 4)]is correct but 'A0': [('A5', 4), ('A3', 1)]is not.
#
# Adjacency Matrices
# The edges E of a graph G induce a binary relation that is called the adjacency relation of G. One can associate an adjacency matrix:
#
# M =  [
#   [0, 0, 0, 1, 0, 4],
#   [0, 0, 2, 0, 0, 0],
#   [0, 1, 2, 1, 1, 0],
#   [1, 0, 1, 0, 0, 0],
#   [0, 0, 1, 0, 1, 0],
#   [0, 0, 0, 3, 0, 0]
# ]
# Let us imagine that lines are numbered from A0 to A5 and the same for columns. The first line correspond to A0 and we can see that A0 is connected to A3 with weight 1, A0 is also connected to A5 with weight 4.
#
# Adjacency Lists
# Another way is to use an adjacency list: An adjacency list representation for a graph associates each vertex in the graph with the collection of its neighboring edges:
#
# L = [
#   ['A0', [('A3', 1), ('A5', 4)]],
#   ['A1', [('A2', 2)]],
#   ['A2', [('A1', 1), ('A2', 2), ('A3', 1), ('A4', 1)]],
#   ['A3', [('A0', 1), ('A2', 1)]],
#   ['A4', [('A2', 1), ('A4', 1)]],
#   ['A5', [('A3', 3)]]
# ]
# L is sorted in order A0 to A5 and each sublist is sorted as in a graph dictionary.
#
# Task
# You are provided with the skeleton of the class Graph. The constructor takes a single integer argument: the order of the graph.
#
# You have to write 6 conversion methods to convert between each of the 3 graph representations defined above.
#
# You also have to write a pathfinding method find_all_paths(dictionary, src, dst) that returns a list of all paths between src and dst. A path is a hyphen-separated string of nodes from src to dst, both inclusive. The list of paths should be ordered by the number of steps in the path in ascending order. If two paths have the same number of steps, sort them lexicographically.
#
# dct = {
#   'A3': [('A0', 1), ('A2', 1)],
#   'A0': [('A3', 1), ('A2', 1)],
#   'A4': [('A2', 1)],
#   'A1': [('A2', 1)],
#   'A2': [('A1', 1), ('A2', 1), ('A3', 1), ('A4', 1)]
# }
# g = Graph(5)
# g.find_all_paths(dct, "A0", "A4")
# # should return:
# ['A0-A2-A4', 'A0-A3-A2-A4']
# FundamentalsListsMatrixGraph Theory