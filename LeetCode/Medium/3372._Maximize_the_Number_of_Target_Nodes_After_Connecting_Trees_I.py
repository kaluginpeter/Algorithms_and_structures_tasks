# There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.
#
# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.
#
# Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.
#
# Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.
#
# Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.
#
#
#
# Example 1:
#
# Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2
#
# Output: [9,7,9,8,8]
#
# Explanation:
#
# For i = 0, connect node 0 from the first tree to node 0 from the second tree.
# For i = 1, connect node 1 from the first tree to node 0 from the second tree.
# For i = 2, connect node 2 from the first tree to node 4 from the second tree.
# For i = 3, connect node 3 from the first tree to node 4 from the second tree.
# For i = 4, connect node 4 from the first tree to node 4 from the second tree.
#
# Example 2:
#
# Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1
#
# Output: [6,3,3,3,3]
#
# Explanation:
#
# For every i, connect node i of the first tree with any node of the second tree.
#
#
#
#
# Constraints:
#
# 2 <= n, m <= 1000
# edges1.length == n - 1
# edges2.length == m - 1
# edges1[i].length == edges2[i].length == 2
# edges1[i] = [ai, bi]
# 0 <= ai, bi < n
# edges2[i] = [ui, vi]
# 0 <= ui, vi < m
# The input is generated such that edges1 and edges2 represent valid trees.
# 0 <= k <= 1000
# Solution
# Python O(N^2 + M^2) O(N + M) Tree Breadth-First-Search
class Solution:
    def count_neighbors(self, source: int, adj_list: list[list[int]], k: int) -> int:
        seen: set[int] = set()
        cur_nodes: list[int] = [source]
        seen.add(source)
        next_nodes: list[int] = []
        length: int = 0
        neighbors: int = 0
        while cur_nodes and length <= k:
            for node in cur_nodes:
                neighbors += 1
                for neighbor in adj_list[node]:
                    if neighbor in seen: continue
                    seen.add(neighbor)
                    next_nodes.append(neighbor)
            cur_nodes = next_nodes
            next_nodes = []
            length += 1
        return neighbors

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n: int = len(edges1) + 1
        m: int = len(edges2) + 1
        adj_list_edges1: list[list[int]] = [[] for _ in range(n)]
        adj_list_edges2: list[list[int]] = [[] for _ in range(m)]
        for u, v in edges1:
            adj_list_edges1[u].append(v)
            adj_list_edges1[v].append(u)
        for u, v in edges2:
            adj_list_edges2[u].append(v)
            adj_list_edges2[v].append(u)
        extra: int = 0
        for vertex in range(m):
            extra = max(extra, self.count_neighbors(vertex, adj_list_edges2, k - 1))
        output: list[int] = [0] * n
        for vertex in range(n):
            output[vertex] = self.count_neighbors(vertex, adj_list_edges1, k) + extra
        return output

# C++ O(N^2 + M^2) O(N + M) Tree Breadth-First-Search
class Solution {
public:
    int countNeighbors(int &source, vector<vector<int>> &adjList, int k) {
        unordered_set<int> seen;
        int neighbors = 0, length = 0;
        seen.insert(source);
        vector<int> curNodes = {source}, nextNodes;
        while (!curNodes.empty() && length <= k) {
            for (int &node : curNodes) {
                ++neighbors;
                for (int &neighbor : adjList[node]) {
                    if (seen.count(neighbor)) continue;
                    seen.insert(neighbor);
                    nextNodes.push_back(neighbor);
                }
            }
            ++length;
            curNodes = nextNodes;
            nextNodes.clear();
        }
        return neighbors;
    }

    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2, int k) {
        int n = edges1.size() + 1, m = edges2.size() + 1;
        vector<vector<int>> adjListEdges1(n, vector<int>()), adjListEdges2(m, vector<int>());
        for (vector<int> &edge : edges1) {
            adjListEdges1[edge[0]].push_back(edge[1]);
            adjListEdges1[edge[1]].push_back(edge[0]);
        }
        int extra = 0;
        for (vector<int> &edge : edges2) {
            adjListEdges2[edge[0]].push_back(edge[1]);
            adjListEdges2[edge[1]].push_back(edge[0]);
        }
        for (int vertex = 0; vertex < m; ++vertex) {
            extra = max(extra, countNeighbors(vertex, adjListEdges2, k - 1));
        }
        vector<int> output(n, 0);
        for (int vertex = 0; vertex < n; ++vertex) {
            output[vertex] = countNeighbors(vertex, adjListEdges1, k) + extra;
        }
        return output;
    }
};