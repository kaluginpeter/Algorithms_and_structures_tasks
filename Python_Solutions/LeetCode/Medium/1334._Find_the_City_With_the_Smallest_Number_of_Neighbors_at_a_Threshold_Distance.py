# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
#
# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
#
# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
#
#
#
# Example 1:
#
#
# Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
# Output: 3
# Explanation: The figure above describes the graph.
# The neighboring cities at a distanceThreshold = 4 for each city are:
# City 0 -> [City 1, City 2]
# City 1 -> [City 0, City 2, City 3]
# City 2 -> [City 0, City 1, City 3]
# City 3 -> [City 1, City 2]
# Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
# Example 2:
#
#
# Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
# Output: 0
# Explanation: The figure above describes the graph.
# The neighboring cities at a distanceThreshold = 2 for each city are:
# City 0 -> [City 1]
# City 1 -> [City 0, City 4]
# City 2 -> [City 3, City 4]
# City 3 -> [City 2, City 4]
# City 4 -> [City 1, City 2, City 3]
# The city 0 has 1 neighboring city at a distanceThreshold = 2.
#
#
# Constraints:
#
# 2 <= n <= 100
# 1 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti, distanceThreshold <= 10^4
# All pairs (fromi, toi) are distinct.
# Solution Heap, Dijkstra, Greedy, HashMap, Graph
# Complexity
# Time complexity: O(N * ElogV)
# Space complexity: O(V + E)
# Code
import heapq
class Solution:
    def dijkstra(self, source: int, paths: list[list[int, int]], boundary: int) -> int:
        destinations: dict[int, int] = dict()
        score: int = 0
        min_heap: list[tuple[int, int]] = [(0, source)]
        while min_heap:
            cur_weight, cur_vertex = heapq.heappop(min_heap)
            if cur_vertex in destinations: continue
            destinations[cur_vertex] = cur_weight
            if cur_weight <= boundary: score += 1
            for neighbor in paths[cur_vertex]:
                if neighbor[0] in destinations: continue
                heapq.heappush(min_heap, (cur_weight + neighbor[1], neighbor[0]))
        return score - 1

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Represent adjacency list: vertex = [i1, i2, ..., in]
        # Where i = [neighbor, weight]
        vertexes: dict[int, list[list[int, int]]] = dict()
        for vertex in range(n):
            if vertex not in vertexes:
                vertexes[vertex] = []
        # Fill the adjacency list
        for path in edges:
            source, destination, weight = path
            if weight > distanceThreshold: continue
            vertexes[source].append([destination, weight])
            vertexes[destination].append([source, weight])
        # Calculate maximum vertex with minimum possible neighbors
        min_edge = min_neighbors = float('inf')
        for vertex in range(n):
            cost: int = self.dijkstra(vertex, vertexes, distanceThreshold)
            if cost <= min_neighbors:
                min_edge, min_neighbors = vertex, cost

        return min_edge