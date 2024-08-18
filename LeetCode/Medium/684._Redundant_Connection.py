# In this problem, a tree is an undirected graph that is connected and has no cycles.
#
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
#
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
#
#
#
# Example 1:
#
#
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:
#
#
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
#
#
# Constraints:
#
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
# Solution Union Find O(N) O(N)
class UnionFind:
    def __init__(self, count_nodes: int) -> None:
        self.parents: list[int] = list(range(count_nodes + 1))
        self.ranks: list[int] = [1] * (count_nodes + 1)
        self.connections: int = count_nodes

    def find(self, node: int) -> int:
        while node != self.parents[node]:
            node = self.parents[node]
            self.parents[node] = self.parents[self.parents[node]]
        return self.parents[node]

    def union(self, node_x: int, node_y: int) -> bool:
        parent_x, parent_y = self.find(node_x), self.find(node_y)
        if parent_x == parent_y:
            return False
        elif self.ranks[parent_x] > self.ranks[parent_y]:
            self.ranks[parent_x] += self.ranks[parent_y]
            self.parents[parent_y] = parent_x
        else:
            self.ranks[parent_y] += self.ranks[parent_x]
            self.parents[parent_x] = parent_y
        self.connections -= 1
        return True

    def is_connected(self) -> bool:
        return self.connections <= 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjoints_set = UnionFind(len(edges))
        for start_vertex, end_vertex in edges:
            if not disjoints_set.union(start_vertex, end_vertex):
                return [start_vertex, end_vertex]