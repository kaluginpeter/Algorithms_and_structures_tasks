# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
#
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
#
#
#
# Example 1:
#
#
# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
# Example 2:
#
# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1
#
#
# Constraints:
#
# 3 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# The given edges represent a valid star graph.
# HashSet, works only in valid start graph
# Complexity
# Time complexity: O(N), but in the real definition of start graph it will take O(1), because we only need one iteration to check start graph
# Space complexity: O(N)
# Code
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ways: set[int] = set()
        for path in edges:
            start, end = path
            if start in ways: return start
            if end in ways: return end
            ways.add(start)
            ways.add(end)

# HashMap, works on every star graph(also in invalid star graph)
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ways: dict[int, int] = defaultdict(int)
        n: int = len(edges)
        for path in edges:
            start, end = path
            ways[start] += 1
            ways[end] += 1
        for vertex in ways:
            if ways[vertex] == n:
                return vertex

# Tricky hack, but works only in valid star graph
# Complexity
# Time complexity: O(1)
# Space complexity: O(1)
# Code
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]