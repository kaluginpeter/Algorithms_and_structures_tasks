# A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.
#
# Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.
#
# The second minimum value is defined as the smallest value strictly larger than the minimum value.
#
# For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
# Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.
#
# Notes:
#
# You can go through any vertex any number of times, including 1 and n.
# You can assume that when the journey starts, all signals have just turned green.
#
#
# Example 1:
#
#        
# Input: n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
# Output: 13
# Explanation:
# The figure on the left shows the given graph.
# The blue path in the figure on the right is the minimum time path.
# The time taken is:
# - Start at 1, time elapsed=0
# - 1 -> 4: 3 minutes, time elapsed=3
# - 4 -> 5: 3 minutes, time elapsed=6
# Hence the minimum time needed is 6 minutes.
#
# The red path shows the path to get the second minimum time.
# - Start at 1, time elapsed=0
# - 1 -> 3: 3 minutes, time elapsed=3
# - 3 -> 4: 3 minutes, time elapsed=6
# - Wait at 4 for 4 minutes, time elapsed=10
# - 4 -> 5: 3 minutes, time elapsed=13
# Hence the second minimum time is 13 minutes.
# Example 2:
#
#
# Input: n = 2, edges = [[1,2]], time = 3, change = 2
# Output: 11
# Explanation:
# The minimum time path is 1 -> 2 with time = 3 minutes.
# The second minimum time path is 1 -> 2 -> 1 -> 2 with time = 11 minutes.
#
#
# Constraints:
#
# 2 <= n <= 104
# n - 1 <= edges.length <= min(2 * 104, n * (n - 1) / 2)
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# There are no duplicate edges.
# Each vertex can be reached directly or indirectly from every other vertex.
# 1 <= time, change <= 103
# Solution BFS Deque Graph Shortests Path O(V + E) O(V + E)
from collections import deque


class Solution:
    def validate_time(self, current_time: int, change: int) -> int:
        whole: int = current_time // change
        # If current whole part is odd, it means
        # that we on red signal
        if whole & 1:
            return change * (whole + 1) - current_time if current_time % change != 0 else change
        return 0

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Create adjacency list
        adj_list: list[list[int]] = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        edges = deque([(1, False)])
        # Initial time to destination all vertex
        first_time_seen: list[int] = [None] * (n + 1)
        # Initial time to destination all vertex
        second_time_seen: list[int] = [None] * (n + 1)
        # Start with vertex1 and set destination time to "0"
        first_time_seen[1] = 0
        while edges:
            cur_edge, seen = edges.popleft()
            current_time = first_time_seen[cur_edge] if not seen else second_time_seen[cur_edge]
            # Make a step to all neighbor edges
            current_time += self.validate_time(current_time, change) + time

            for neighbor in adj_list[cur_edge]:
                # If we not see neighbor edge
                if first_time_seen[neighbor] == None:
                    first_time_seen[neighbor] = current_time
                    edges.append((neighbor, False))
                # If we already seen the neighbor edge
                # and current time of destination is strickly more than previouse time destination
                # For case when: second shortest path can have equal time with first shortest path
                elif second_time_seen[neighbor] == None and first_time_seen[neighbor] != current_time:
                    # If we found last edge(meaning traversing from 1 to n)
                    if neighbor == n: return current_time
                    second_time_seen[neighbor] = current_time
                    edges.append((neighbor, True))
        return 0