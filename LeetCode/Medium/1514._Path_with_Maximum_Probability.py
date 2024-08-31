# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
#
# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.
#
# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
#
#
#
# Example 1:
#
#
#
# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
# Example 2:
#
#
#
# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
# Output: 0.30000
# Example 3:
#
#
#
# Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# Output: 0.00000
# Explanation: There is no path between 0 and 2.
#
#
# Constraints:
#
# 2 <= n <= 10^4
# 0 <= start, end < n
# start != end
# 0 <= a, b < n
# a != b
# 0 <= succProb.length == edges.length <= 2*10^4
# 0 <= succProb[i] <= 1
# There is at most one edge between every two nodes.
# Solution Dijkstra Heap Graph Shortest Path O(N + E log(N)) O(N)
from collections import defaultdict
import heapq
class Solution:
    def dijkstra(self, start: int, end: int, adj_list: dict[int, list[tuple[int ,int]]], paths: list[int]) -> None:
        seen: set[int] = set()
        heap: list[int] = [(-0, start)]
        while heap:
            cost, cur_edge = heapq.heappop(heap)
            # Transform from negative to positive
            cost = -cost

            if cur_edge in seen:
                continue
            if paths[cur_edge] < cost:
                paths[cur_edge] = cost
            # If we just multiply first edge with start
            # with initial value 0, we always get 0, so transform to 1
            if cost == 0:
                cost = 1
            seen.add(cur_edge)
            for neighbor in adj_list.get(cur_edge, []):
                neighbor_edge, neighbor_weight = neighbor
                neighbor_weight: int = cost * neighbor_weight
                heapq.heappush(heap, (-neighbor_weight, neighbor_edge))


    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for edge_idx in range(len(edges)):
            start, end = edges[edge_idx]
            weight: int = succProb[edge_idx]
            adj_list[start].append((end, weight))
            adj_list[end].append((start, weight))
        # We can use a little bit of optimization here, but it no nesscesarry
        # if adj_list.get(end_node, None) is None:
        #     return 0
        paths: list[int] = [0] * n
        self.dijkstra(start_node, end_node, adj_list, paths)

        return paths[end_node]

# Solution O(N + E logN) O(N)
from collections import defaultdict
import heapq
class Solution:
    def dijkstra(self, start: int, end: int, adj_list: dict[int, list[tuple[int, int]]], costs: list[int]) -> None:
        seen: set[int] = set()
        heap: list[tuple[int, int]] = [(-0, start)]
        while heap:
            cur_cost, cur_vertex = heapq.heappop(heap)
            cur_cost = -cur_cost
            if cur_vertex in seen: continue
            seen.add(cur_vertex)
            costs[cur_vertex] = max(costs[cur_vertex], cur_cost)
            if cur_vertex == end: return
            if cur_cost == 0:
                cur_cost = 1
            for neighbor in adj_list.get(cur_vertex, []):
                neighbor_cost, neighbor_vertex = neighbor
                heapq.heappush(heap, (-cur_cost * neighbor_cost, neighbor_vertex))

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for idx in range(len(edges)):
            source, destination = edges[idx]
            probability: int = succProb[idx]
            adj_list[source].append((probability, destination))
            adj_list[destination].append((probability, source))
        costs: list[int] = [0] * n
        self.dijkstra(start_node, end_node, adj_list, costs)
        return costs[end_node]