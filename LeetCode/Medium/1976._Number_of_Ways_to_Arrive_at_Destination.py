# You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.
#
# You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.
#
# Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
#
# Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
# Output: 4
# Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
# The four ways to get there in 7 minutes are:
# - 0 ➝ 6
# - 0 ➝ 4 ➝ 6
# - 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
# - 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
# Example 2:
#
# Input: n = 2, roads = [[1,0,10]]
# Output: 1
# Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
#
#
# Constraints:
#
# 1 <= n <= 200
# n - 1 <= roads.length <= n * (n - 1) / 2
# roads[i].length == 3
# 0 <= ui, vi <= n - 1
# 1 <= timei <= 109
# ui != vi
# There is at most one road connecting any two intersections.
# You can reach any intersection from any other intersection.
# Solution
# Python O(|E|log(|V|)) O(|V|) Dijkstra ShortestPath DynamicProgramming Graph
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD: int = 1000000007
        adj_list: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, w in roads:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
        path_count: list[int] = [0] * n
        path_count[0] = 1
        path_cost: list[int] = [float('inf')] * n
        path_cost[0] = 0
        min_heap: list[tuple[int, int]] = [(0, 0)]
        while min_heap:
            cur_cost, vertex = heapq.heappop(min_heap)
            for neighbor, weight in adj_list[vertex]:
                next_cost: int = cur_cost + weight
                if next_cost < path_cost[neighbor]:
                    path_cost[neighbor] = next_cost
                    path_count[neighbor] = path_count[vertex]
                    heapq.heappush(min_heap, (next_cost, neighbor))
                elif next_cost == path_cost[neighbor]:
                    path_count[neighbor] = (path_count[neighbor] + path_count[vertex]) % MOD
        return path_count[n - 1]

# C++ O(|E|log(|V|)) O(|V|) Graph Dijkstra DynamicProgramming
class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        long long MOD = 1000000007;
        vector<vector<pair<int, int>>> adjList (n, vector<pair<int, int>>());
        for (vector<int>& road : roads) {
            int& u = road[0];
            int& v = road[1];
            int& w = road[2];
            adjList[u].push_back({v, w});
            adjList[v].push_back({u, w});
        }
        vector<long long> pathCount (n, 0);
        pathCount[0] = 1;
        vector<long long> costVertex (n, 1e12);
        costVertex[0] = 0;
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> minHeap;
        minHeap.push({0, 0});
        while (!minHeap.empty()) {
            long long curCost = minHeap.top().first;
            int vertex = minHeap.top().second;
            minHeap.pop();
            for (pair<int, int>& edge : adjList[vertex]) {
                long long nextCost = curCost + edge.second;
                if (nextCost < costVertex[edge.first]) {
                    costVertex[edge.first] = nextCost;
                    pathCount[edge.first] = pathCount[vertex];
                    minHeap.push({nextCost, edge.first});
                } else if (nextCost == costVertex[edge.first]) {
                    pathCount[edge.first] = (pathCount[edge.first] + pathCount[vertex]) % MOD;
                }
            }
        }
        return pathCount[n - 1];
    }
};