# You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, and an integer array edges where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.
#
# Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).
#
# Your task is to modify all edges with a weight of -1 by assigning them positive integer values in the range [1, 2 * 109] so that the shortest distance between the nodes source and destination becomes equal to an integer target. If there are multiple modifications that make the shortest distance between source and destination equal to target, any of them will be considered correct.
#
# Return an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance from source to destination equal to target, or an empty array if it's impossible.
#
# Note: You are not allowed to modify the weights of edges with initial positive weights.
#
#
#
# Example 1:
#
#
#
# Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
# Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
# Explanation: The graph above shows a possible modification to the edges, making the distance from 0 to 1 equal to 5.
# Example 2:
#
#
#
# Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
# Output: []
# Explanation: The graph above contains the initial edges. It is not possible to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. So, an empty array is returned.
# Example 3:
#
#
#
# Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
# Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
# Explanation: The graph above shows a modified graph having the shortest distance from 0 to 2 as 6.
#
#
# Constraints:
#
# 1 <= n <= 100
# 1 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 3
# 0 <= ai, bi < n
# wi = -1 or 1 <= wi <= 107
# ai != bi
# 0 <= source, destination < n
# source != destination
# 1 <= target <= 109
# The graph is connected, and there are no self-loops or repeated edges
# Solution Dijkstra Graph Shortest Path O(N**3logN) O(N**2logN)
import heapq
from collections import defaultdict


class Solution:

    def dijkstra(
            self, start: int, end: int,
            adj_list: dict[int, list[tuple[int, int]]], paths: list[set[int]],
            costs: list[int], boundary: int
    ) -> None:
        seen: set[int] = set()
        heap: list[tuple[int, int]] = [(0, start)]
        costs[start] = 0

        while heap:
            cur_weight, cur_vertex = heapq.heappop(heap)
            if cur_vertex in seen: continue
            seen.add(cur_vertex)
            if cur_weight > boundary: return
            if cur_vertex == end: return
            for neighbor in adj_list.get(cur_vertex, []):
                neighbor_weight, neighbor_vertex = neighbor
                if cur_weight + neighbor_weight < costs[neighbor_vertex]:
                    costs[neighbor_vertex] = cur_weight + neighbor_weight
                    paths[neighbor_vertex].clear()
                    paths[neighbor_vertex].update(paths[cur_vertex])
                    paths[neighbor_vertex].add((cur_vertex, neighbor_vertex))

                heapq.heappush(heap, (cur_weight + neighbor_weight, neighbor_vertex))

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[
        List[int]]:
        should_be_changed: set[int] = set()
        adj_list: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for idx in range(len(edges)):
            edge: list[int, int, int] = edges[idx]
            start, end, weight = edge
            if weight == -1:
                should_be_changed.add((start, end))
                edge[2] = 1
                weight = edge[2]
            adj_list[start].append((weight, end))
            adj_list[end].append((weight, start))

        for _ in range(n):
            paths: list[set[int]] = [set() for _ in range(n)]
            costs: list[int] = [float('inf')] * n
            self.dijkstra(source, destination, adj_list, paths, costs, target)
            if costs[destination] >= target: break

            for idx in range(len(edges)):
                edge: list[int, int, int] = edges[idx]
                if (
                        (edge[0], edge[1]) in should_be_changed and
                        (
                                (edge[0], edge[1]) in paths[destination] or
                                (edge[1], edge[0]) in paths[destination]
                        )
                ):
                    edge[2] += target - costs[destination]
                    for ceil_idx in range(len(adj_list[edge[0]])):
                        if adj_list[edge[0]][ceil_idx][1] == edge[1]:
                            adj_list[edge[0]][ceil_idx] = (edge[2], edge[1])
                            break
                    for ceil_idx in range(len(adj_list[edge[1]])):
                        if adj_list[edge[1]][ceil_idx][1] == edge[0]:
                            adj_list[edge[1]][ceil_idx] = (edge[2], edge[0])
                            break

                    break

        return edges if costs[destination] == target else []