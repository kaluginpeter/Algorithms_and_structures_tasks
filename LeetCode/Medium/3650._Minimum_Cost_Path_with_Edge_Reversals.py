# You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.
#
# Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch, you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.
#
# The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.
#
# Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.
#
#
#
# Example 1:
#
# Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
#
# Output: 5
#
# Explanation:
#
#
#
# Use the path 0 → 1 (cost 3).
# At node 1 reverse the original edge 3 → 1 into 1 → 3 and traverse it at cost 2 * 1 = 2.
# Total cost is 3 + 2 = 5.
# Example 2:
#
# Input: n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]
#
# Output: 3
#
# Explanation:
#
# No reversal is needed. Take the path 0 → 2 (cost 1), then 2 → 1 (cost 1), then 1 → 3 (cost 1).
# Total cost is 1 + 1 + 1 = 3.
#
#
# Constraints:
#
# 2 <= n <= 5 * 104
# 1 <= edges.length <= 105
# edges[i] = [ui, vi, wi]
# 0 <= ui, vi <= n - 1
# 1 <= wi <= 1000
# Solution
# Python O(VlogE) O(VE) PriorityQueue Graph Dijkstra
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj_list: dict[int, list[int]] = defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w * 2))
        min_heap: list[tuple[int, int]] = [(0, 0)]
        costs: list[int] = [float('inf')] * n
        costs[0] = 0
        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node == n - 1: return cost
            for neighbor, weight in adj_list[node]:
                next_cost: int = cost + weight
                if next_cost >= costs[neighbor]: continue
                costs[neighbor] = next_cost
                heapq.heappush(min_heap, (next_cost, neighbor))
        return -1

# C++ O(VlogE) O(VE) Dijkstra Graph PriorityQueue
class Solution {
public:
    int minCost(int n, vector<vector<int>>& edges) {
        // Follow up:
        // 1) We should use priority queue
        // 2) Complexity under O(NlogN) due to 5*10^4 input data size
        // 3) There isn't negative weights in graph
        // 4) Let's try to build adjList with directed node and reversed
        // 5) Early prunning
        std::unordered_map<int, std::vector<std::pair<int, int>>> adjList;
        for (std::vector<int>& edge: edges) {
            adjList[edge[1]].push_back({edge[0], edge[2] * 2});
            adjList[edge[0]].push_back({edge[1], edge[2]});
        }
        std::priority_queue<
            std::pair<int, int>, // <cost, node>
            std::vector<std::pair<int, int>>,
            std::greater<std::pair<int, int>>
        > minHeap;
        minHeap.push({0, 0});
        std::vector<int> costs(n, INT32_MAX);
        costs[0] = 0; // Starting cost is 0
        while (!minHeap.empty()) {
            auto [cost, node] = minHeap.top();
            if (node == n - 1) return cost; // Reached target node
            minHeap.pop();
            for (std::pair<int, int>& neighbor : adjList[node]) { // Move into directed edges
                int nextCost = cost + neighbor.second;
                if (nextCost >= costs[neighbor.first]) continue; // Meaningless to visit
                costs[neighbor.first] = nextCost;
                minHeap.push({nextCost, neighbor.first});
            }
        }
        return -1; // There is no way to visit n - 1 node starting from 0
    }
};