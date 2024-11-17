# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
#
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
#
#
#
# Example 1:
#
#
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:
#
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:
#
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
#
#
# Constraints:
#
# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
# Solution
# Python O(ElogE) O(ElogE) Shortest Path Dijkstra Priority Queue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list: dict[int, list[tuple[int, int]]] = dict()
        for time in times:
            source, destination, weight = time
            if source not in adj_list:
                adj_list[source] = list()
            adj_list[source].append((weight, destination))
        bound: int = 6000 * 100 + 1
        distances: dict[int, int] = dict()
        for vertex in range(1, n + 1):
            distances[vertex] = bound
        min_heap: list[tuple[int, int]] = [(0, k)]
        while min_heap:
            cur_cost, cur_vertex = heapq.heappop(min_heap)
            if distances[cur_vertex] != bound:
                continue
            distances[cur_vertex] = cur_cost
            for edge in adj_list.get(cur_vertex, []):
                weight, neighbor = edge
                if distances[neighbor] == bound:
                    heapq.heappush(min_heap, (cur_cost + weight, neighbor))
        min_distance: int = -1
        for vertex in distances:
            if distances[vertex] == bound:
                return -1
            min_distance = max(min_distance, distances[vertex])
        return min_distance

# C++ O(ElogE) O(ElogE) Shortest Path Dijkstra Priority Queue
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        std::unordered_map<int, std::vector<std::pair<int, int>>> adjList;
        for (std::vector<int>& time : times) {
            int source = time[0];
            int destination = time[1];
            int weight = time[2];
            adjList[source].push_back({weight, destination});
        }
        std::unordered_map<int, int> distances;
        int bound = 6000 * 100 + 1;
        for (int vertex = 1; vertex < n + 1; ++vertex) {
            distances[vertex] = bound;
        }
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> minHeap;
        minHeap.push({0, k});
        while (minHeap.size()) {
            int curCost = minHeap.top().first;
            int curVertex = minHeap.top().second;
            minHeap.pop();
            if (distances[curVertex] != bound) {
                continue;
            }
            distances[curVertex] = curCost;
            for (std::pair<int, int>& edge : adjList[curVertex]) {
                if (distances[edge.second] == bound) {
                    minHeap.push({curCost + edge.first, edge.second});
                }
            }

        }
        int minDistance = -1;
        for (auto& vertex : distances) {
            if (vertex.second == bound) {
                return -1;
            } else {
                minDistance = std::max(minDistance, vertex.second);
            }
        }
        return minDistance;
    }
};