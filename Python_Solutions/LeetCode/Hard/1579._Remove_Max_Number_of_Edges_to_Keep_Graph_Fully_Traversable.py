# Alice and Bob have an undirected graph of n nodes and three types of edges:
#
# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can be traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.
#
# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.
#
#
#
# Example 1:
#
#
#
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
# Example 2:
#
#
#
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
# Example 3:
#
#
#
# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
#
#
#
#
# Constraints:
#
# 1 <= n <= 105
# 1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
# edges[i].length == 3
# 1 <= typei <= 3
# 1 <= ui < vi <= n
# All tuples (typei, ui, vi) are distinct.
# Solution Union Find Greedy O(N) O(N)
# Similar problems
# Before start, you should try to complete 684.Leetcode Problem, because it's more similar task than current problem.
#
# General idea
# We should create two disjoints sets for alice and bob respectively.
# Also we should count how many minimum edges we should add to be able traverse after all nodes in graph for alice and bob resepctively.
# By greedy approach initially we should choose edge by "type 3". In each iteration of loop if current edge type is 3, we should add edge into alice and bob union fin(disjoints set) and increment by 1 minimum needed edges.
# After ending first loop, we shoud create a second to move from entire edges and check if edge type is 1, then add edge to alice disjiont set and increment minimum edges if we successfully added edges, otherwise just coninute iterationg. Same operations we should make with edges with type 2 and bob disjoint set.
# After end of second loop we should check, that both of alice and bob disjoints set have only one connections. It means that we can traverse throught all entire graph by alice and bob respectively. If its not, we should return "-1", because we can't moves from all nodes by alice or bob. Otherwise if it is we should return length of edges substract miniumum needed edges to traversing.
# See at code below for better understating
#
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
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
        if parent_x == parent_y: return False # already connected
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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UnionFind(n), UnionFind(n)
        minimum_needed_edges: int = 0
        for type_edge, start_vertex, end_vertex in edges:
            if type_edge == 3:
                minimum_needed_edges += alice.union(start_vertex, end_vertex) | bob.union(start_vertex, end_vertex)
        for type_edge, start_vertex, end_vertex in edges:
            if type_edge == 1:
                minimum_needed_edges += alice.union(start_vertex, end_vertex)
            elif type_edge == 2:
                minimum_needed_edges += bob.union(start_vertex, end_vertex)
        if not alice.is_connected() or not bob.is_connected():
            return -1
        return len(edges) - minimum_needed_edges