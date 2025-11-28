# There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
#
# You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node, and an integer k.
#
# A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by k, where the value of a connected component is the sum of the values of its nodes.
#
# Return the maximum number of components in any valid split.
#
#
#
# Example 1:
#
#
# Input: n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
# Output: 2
# Explanation: We remove the edge connecting node 1 with 2. The resulting split is valid because:
# - The value of the component containing nodes 1 and 3 is values[1] + values[3] = 12.
# - The value of the component containing nodes 0, 2, and 4 is values[0] + values[2] + values[4] = 6.
# It can be shown that no other valid split has more than 2 connected components.
# Example 2:
#
#
# Input: n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3
# Output: 3
# Explanation: We remove the edge connecting node 0 with 2, and the edge connecting node 0 with 1. The resulting split is valid because:
# - The value of the component containing node 0 is values[0] = 3.
# - The value of the component containing nodes 2, 5, and 6 is values[2] + values[5] + values[6] = 9.
# - The value of the component containing nodes 1, 3, and 4 is values[1] + values[3] + values[4] = 6.
# It can be shown that no other valid split has more than 3 connected components.
#
#
# Constraints:
#
# 1 <= n <= 3 * 104
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# values.length == n
# 0 <= values[i] <= 109
# 1 <= k <= 109
# Sum of values is divisible by k.
# The input is generated such that edges represents a valid tree.
# Solution
# Python O(E + N) O(E) Depth First Search
class Solution:
    components: int = 0
    total_sum: int = 0

    def build_adj_list(self, edges: list[list[int]]) -> dict[int, list[int]]:
        adj_list: dict[int, list[int]] = dict()
        for edge in edges:
            x, y = edge
            if x not in adj_list:
                adj_list[x] = list()
            if y not in adj_list:
                adj_list[y] = list()
            adj_list[x].append(y)
            adj_list[y].append(x)
        return adj_list

    def dfs(self, source: int, adj_list: dict[int, list[int]], values: list[int], k: int, seen: set[int]) -> int:
        cur_sub_tree_sum: int = values[source]
        for vertex in adj_list.get(source, []):
            if vertex in seen: continue
            seen.add(vertex)
            child_sum: int = self.dfs(vertex, adj_list, values, k, seen)
            if child_sum % k == 0 and (self.total_sum - child_sum) % k == 0:
                self.components += 1
                self.total_sum -= child_sum
            else:
                cur_sub_tree_sum += child_sum
        return cur_sub_tree_sum

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        self.components = 1
        self.total_sum = sum(values)
        seen: set[int] = set()
        seen.add(0)
        adj_list: dict[int, list[int]] = self.build_adj_list(edges)
        self.dfs(0, adj_list, values, k, seen)
        return self.components

# C++ O(E + N) O(E) Depth First Search
class Solution {
public:
    int components = 0;
    long long totalSum = 0;
    std::unordered_map<int, std::vector<int>> buildAdjList(std::vector<std::vector<int>>& edges) {
        std::unordered_map<int, std::vector<int>> adjList;
        for (std::vector<int>& edge : edges) {
            int x = std::min(edge[0], edge[1]);
            int y = std::max(edge[0], edge[1]);
            adjList[x].push_back(y);
            adjList[y].push_back(x);
        }
        return adjList;
    }
    long long dfs(int source, std::unordered_map<int, std::vector<int>>& adjList, int& k, std::vector<int>& values, std::unordered_set<int>& seen) {
        long long curSubTreeSum = values[source];
        for (int edge : adjList[source]) {
            if (seen.count(edge)) {
                continue;
            } else {
                seen.insert(edge);
            }
            long long childSum = dfs(edge, adjList, k, values, seen);
            if (childSum % k == 0 && (totalSum - childSum) % k == 0) {
                ++components;
                totalSum -= childSum;
            } else {
                curSubTreeSum += childSum;
            }
        }
        return curSubTreeSum;

    }
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        components = 1;
        totalSum = 0;
        for (int val : values) {
            totalSum += val;
        }
        std::unordered_set<int> seen;
        std::unordered_map<int, std::vector<int>> adjList = buildAdjList(edges);
        seen.insert(0);
        dfs(0, adjList, k, values, seen);
        return components;
    }
};

# C++ O(V + E) O(E) Depth-First-Search
class Solution {
public:
    int components = 0;
    long long totalSum = 0;
    std::unordered_map<int, std::vector<int>> buildAdjList(std::vector<std::vector<int>>& edges) {
        std::unordered_map<int, std::vector<int>> adjList;
        for (std::vector<int>& edge : edges) {
            int x = std::min(edge[0], edge[1]);
            int y = std::max(edge[0], edge[1]);
            adjList[x].push_back(y);
            adjList[y].push_back(x);
        }
        return adjList;
    }
    long long dfs(int source, std::unordered_map<int, std::vector<int>>& adjList, int& k, std::vector<int>& values, std::unordered_set<int>& seen) {
        long long curSubTreeSum = values[source];
        for (int edge : adjList[source]) {
            if (seen.count(edge)) continue;
            else seen.insert(edge);
            long long childSum = dfs(edge, adjList, k, values, seen);
            if (childSum % k == 0 && (totalSum - childSum) % k == 0) {
                ++components;
                totalSum -= childSum;
            } else curSubTreeSum += childSum;
        }
        return curSubTreeSum;

    }
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        components = 1;
        totalSum = 0;
        for (int val : values) totalSum += val;
        std::unordered_set<int> seen;
        std::unordered_map<int, std::vector<int>> adjList = buildAdjList(edges);
        seen.insert(0);
        dfs(0, adjList, k, values, seen);
        return components;
    }
};