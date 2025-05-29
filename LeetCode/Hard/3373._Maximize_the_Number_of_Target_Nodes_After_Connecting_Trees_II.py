# There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.
#
# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
#
# Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.
#
# Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.
#
# Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.
#
#
#
# Example 1:
#
# Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
#
# Output: [8,7,7,8,8]
#
# Explanation:
#
# For i = 0, connect node 0 from the first tree to node 0 from the second tree.
# For i = 1, connect node 1 from the first tree to node 4 from the second tree.
# For i = 2, connect node 2 from the first tree to node 7 from the second tree.
# For i = 3, connect node 3 from the first tree to node 0 from the second tree.
# For i = 4, connect node 4 from the first tree to node 4 from the second tree.
#
# Example 2:
#
# Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]
#
# Output: [3,6,6,6,6]
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
# 2 <= n, m <= 105
# edges1.length == n - 1
# edges2.length == m - 1
# edges1[i].length == edges2[i].length == 2
# edges1[i] = [ai, bi]
# 0 <= ai, bi < n
# edges2[i] = [ui, vi]
# 0 <= ui, vi < m
# The input is generated such that edges1 and edges2 represent valid trees.
# Solution
# Python O(N + M) O(N) Breadth-First-Search Greedy Tree
class Solution:
    def count_even_neighbors(self, source: int, adj_list: list[list[int]]) -> int:
        cur_nodes: list[int] = [source]
        next_nodes: list[int] = []
        seen: set[int] = set()
        seen.add(source)
        output: int = 0
        step: int = 0
        while cur_nodes:
            for node in cur_nodes:
                if (step & 1) == 0: output += 1
                for neighbor in adj_list[node]:
                    if neighbor in seen: continue
                    seen.add(neighbor)
                    next_nodes.append(neighbor)
            cur_nodes = next_nodes
            next_nodes = []
            step += 1
        return output

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
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
        even_neighbors_from_second_tree: int = self.count_even_neighbors(0, adj_list_edges2)
        extra: int = max(even_neighbors_from_second_tree, m - even_neighbors_from_second_tree)
        even_neighbors_from_first_tree: int = self.count_even_neighbors(0, adj_list_edges1)
        odd_neighbors_from_first_tree: int = n - even_neighbors_from_first_tree
        cur_nodes: list[int] = [0]
        next_nodes: list[int] = []
        output: list[int] = [0] * n
        step: int = 0
        while cur_nodes:
            for node in cur_nodes:
                output[node] = [even_neighbors_from_first_tree, odd_neighbors_from_first_tree][step & 1] + extra
                for neighbor in adj_list_edges1[node]:
                    if output[neighbor]: continue
                    next_nodes.append(neighbor)
            cur_nodes = next_nodes
            next_nodes = []
            step += 1
        return output

# C++ O(N + M) O(N) Breadth-First-Search Tree Greedy
class Solution {
public:
    int countEvenNeighbors(int source, vector<vector<int>> &adjList) {
        vector<int> curNodes = {source}, nextNodes;
        unordered_set<int> seen;
        seen.insert(source);
        int output = 0, step = 0;
        while (!curNodes.empty()) {
            for (int &node : curNodes) {
                if ((step & 1) == 0) ++output;
                for (int &neighbor : adjList[node]) {
                    if (seen.count(neighbor)) continue;
                    seen.insert(neighbor);
                    nextNodes.push_back(neighbor);
                }
            }
            curNodes = nextNodes;
            nextNodes.clear();
            ++step;
        }
        return output;
    }
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = edges1.size() + 1, m = edges2.size() + 1;
        vector<vector<int>> adjListEdges1(n, vector<int>()), adjListEdges2(m, vector<int>());
        for (vector<int> &edge : edges1) {
            adjListEdges1[edge[0]].push_back(edge[1]);
            adjListEdges1[edge[1]].push_back(edge[0]);
        }
        for (vector<int> &edge : edges2) {
            adjListEdges2[edge[0]].push_back(edge[1]);
            adjListEdges2[edge[1]].push_back(edge[0]);
        }
        int evenNeighborsFromSecondTree = countEvenNeighbors(0, adjListEdges2);
        int extra = max(evenNeighborsFromSecondTree, m - evenNeighborsFromSecondTree);
        int evenNeighborsFromFirstTree = countEvenNeighbors(0, adjListEdges1);
        int oddNeighborsFromFirstTree = n - evenNeighborsFromFirstTree;
        vector<int> output(n, 0);
        vector<int> curNodes = {0}, nextNodes;
        int step = 0;
        while (!curNodes.empty()) {
            for (int &node : curNodes) {
                output[node] = (step & 1? oddNeighborsFromFirstTree : evenNeighborsFromFirstTree) + extra;
                for (int &neighbor : adjListEdges1[node]) {
                    if (output[neighbor]) continue;
                    nextNodes.push_back(neighbor);
                }
            }
            curNodes = nextNodes;
            nextNodes.clear();
            ++step;
        }
        return output;
    }
};