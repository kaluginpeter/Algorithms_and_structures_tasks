# You are given an integer n and a 2D integer array queries.
#
# There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.
#
# queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.
#
# Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.
#
#
#
# Example 1:
#
# Input: n = 5, queries = [[2,4],[0,2],[0,4]]
#
# Output: [3,2,1]
#
# Explanation:
#
#
#
# After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.
#
#
#
# After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.
#
#
#
# After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.
#
# Example 2:
#
# Input: n = 4, queries = [[0,3],[0,2]]
#
# Output: [1,1]
#
# Explanation:
#
#
#
# After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.
#
#
#
# After the addition of the road from 0 to 2, the length of the shortest path remains 1.
#
#
#
# Constraints:
#
# 3 <= n <= 500
# 1 <= queries.length <= 500
# queries[i].length == 2
# 0 <= queries[i][0] < queries[i][1] < n
# 1 < queries[i][1] - queries[i][0]
# There are no repeated roads among the queries.
# Solution
# Complexity
# Time
# complexity: O(K(V + E)logV) where k is length of queries
# Space
# complexity: O(N)
#
# Code
import heapq


class Solution:
    def dijkstra(self, start: int, target: int, paths: dict[int, list[int]]) -> int:
        min_heap: list[tuple[int]] = [(0, start)]
        seen: set[int] = set()
        while min_heap:
            cur_cost, vertex = heapq.heappop(min_heap)
            if vertex in seen: continue
            seen.add(vertex)
            if vertex == target: return cur_cost
            for neighbor in paths[vertex]:
                if neighbor in seen: continue
                heapq.heappush(min_heap, (cur_cost + 1, neighbor))

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        paths: dict[int, list[int]] = dict()
        for vertex in range(n):
            if vertex not in paths:
                paths[vertex] = []
            if vertex == n - 1: continue
            paths[vertex].append(vertex + 1)
        answer: list[int] = []
        for query in queries:
            source, destination = query
            paths[source].append(destination)
            answer.append(self.dijkstra(0, n - 1, paths))
        return answer