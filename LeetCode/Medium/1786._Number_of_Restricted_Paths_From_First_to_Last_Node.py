# There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.
#
# A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.
#
# The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.
#
# Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
#
# Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
# Output: 3
# Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The three restricted paths are:
# 1) 1 --> 2 --> 5
# 2) 1 --> 2 --> 3 --> 5
# 3) 1 --> 3 --> 5
# Example 2:
#
#
# Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
# Output: 1
# Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The only restricted path is 1 --> 3 --> 7.
#
#
# Constraints:
#
# 1 <= n <= 2 * 104
# n - 1 <= edges.length <= 4 * 104
# edges[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 1 <= weighti <= 105
# There is at most one edge between any two nodes.
# There is at least one path between any two nodes.
# Solution
# Python O((V + E)logV + V) O(V) Dijkstra Graph DynamicProgramming
class Solution:
    def dijkstra(self, source: int, edges: list[list[int]], costs: list[int]) -> None:
        adj_list: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for u, v, c in edges:
            adj_list[u].append((v, c))
            adj_list[v].append((u, c))
        min_heap: list[tuple[int, int]] = [(0, source)]
        while min_heap:
            cost, vertex = heapq.heappop(min_heap)
            for neighbor, price in adj_list[vertex]:
                next_cost: int = cost + price
                if next_cost >= costs[neighbor]: continue
                costs[neighbor] = next_cost
                heapq.heappush(min_heap, (next_cost, neighbor))

    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        costs: list[int] = [float('inf')] * (n + 1)
        costs[n] = 0
        self.dijkstra(n, edges, costs)
        in_degree: list[int] = [0] * (n + 1)
        adj_list: dict[int, list[int]] = defaultdict(list)
        for u, v, c in edges:
            if costs[u] > costs[v]:
                in_degree[v] += 1
                adj_list[u].append(v)
            elif costs[v] > costs[u]:
                in_degree[u] += 1
                adj_list[v].append(u)
        nodes: list[int] = deque()
        for vertex in range(1, n + 1):
            if in_degree[vertex]: continue
            nodes.append(vertex)
        topological_order: list[int] = []
        while nodes:
            node: int = nodes.popleft()
            topological_order.append(node)
            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                if not in_degree[neighbor]: nodes.append(neighbor)
        dp: list[int] = [0] * (n + 1)
        dp[1] = 1
        mod: int = 10**9 + 7
        for vertex in topological_order:
            for neighbor in adj_list[vertex]:
                dp[neighbor] = (dp[neighbor] + dp[vertex]) % mod
        return dp[n]

# C++ O((V + E)logV + V) O(V) Graph DynamicProgramming Dijkstra
class Solution {
public:
    void dijkstra(int source, const std::vector<std::vector<int>> &edges, std::vector<int> &costs) {
        std::unordered_map<int, std::vector<std::pair<int, int>>> adjList;
        for (const std::vector<int> &edge : edges) {
            adjList[edge[0]].push_back({edge[1], edge[2]});
            adjList[edge[1]].push_back({edge[0], edge[2]});
        }
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> minHeap;
        minHeap.push({0, source});
        while (!minHeap.empty()) {
            int cost = minHeap.top().first, vertex = minHeap.top().second;
            minHeap.pop();
            for (const std::pair<int, int> &edge : adjList[vertex]) {
                int nextCost = cost + edge.second;
                if (nextCost >= costs[edge.first]) continue;
                costs[edge.first] = nextCost;
                minHeap.push({nextCost, edge.first});
            }
        }
    }
    int countRestrictedPaths(int n, vector<vector<int>>& edges) {
        std::vector<int> costs(n + 1, INT32_MAX);
        costs[n] = 0;
        dijkstra(n, edges, costs);
        std::unordered_map<int, std::vector<int>> adjList;
        std::vector<int> inDegree(n + 1, 0);
        for (const std::vector<int> &edge : edges) {
            if (costs[edge[0]] > costs[edge[1]]) {
                adjList[edge[0]].push_back(edge[1]);
                ++inDegree[edge[1]];
            } else if (costs[edge[1]] > costs[edge[0]]) {
                adjList[edge[1]].push_back(edge[0]);
                ++inDegree[edge[0]];
            }
        }
        std::queue<int> nodes;
        for (int vertex = 1; vertex <= n; ++vertex) {
            if (inDegree[vertex]) continue;
            nodes.push(vertex);
        }
        std::vector<int> topologicalOrder;
        while (!nodes.empty()) {
            int node = nodes.front();
            nodes.pop();
            topologicalOrder.push_back(node);
            for (const int &neighbor : adjList[node]) {
                --inDegree[neighbor];
                if (!inDegree[neighbor]) nodes.push(neighbor);
            }
        }
        std::vector<int> dp(n + 1, 0);
        dp[1] = 1;
        int mod = 1e9 + 7;
        for (const int &vertex : topologicalOrder) {
            for (const int &neighbor : adjList[vertex]) {
                dp[neighbor] = (dp[neighbor] + dp[vertex]) % mod;
            }
        }
        return dp[n];
    }
};