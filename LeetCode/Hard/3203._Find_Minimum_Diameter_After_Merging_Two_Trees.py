# There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
#
# You must connect one node from the first tree with another node from the second tree with an edge.
#
# Return the minimum possible diameter of the resulting tree.
#
# The diameter of a tree is the length of the longest path between any two nodes in the tree.
#
#
#
# Example 1:
#
# Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]
#
# Output: 3
#
# Explanation:
#
# We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.
#
# Example 2:
#
#
# Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
#
# Output: 5
#
# Explanation:
#
# We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.
#
#
#
# Constraints:
#
# 1 <= n, m <= 105
# edges1.length == n - 1
# edges2.length == m - 1
# edges1[i].length == edges2[i].length == 2
# edges1[i] = [ai, bi]
# 0 <= ai, bi < n
# edges2[i] = [ui, vi]
# 0 <= ui, vi < m
# The input is generated such that edges1 and edges2 represent valid trees.
# Solution
# Python O(N + M) O(N + M) DFS
class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> int:
        n: int = len(edges1) + 1
        m: int = len(edges2) + 1
        adj_list1: list[list[int]] = self.build_adj_list(n, edges1)
        adj_list2: list[list[int]] = self.build_adj_list(m, edges2)
        diameter1, _ = self.find_diameter(adj_list1, 0, -1)
        diameter2, _ = self.find_diameter(adj_list2, 0, -1)
        combined_diameter: int = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1
        return max(diameter1, diameter2, combined_diameter)

    def build_adj_list(
        self, size: int, edges: list[list[int]]
    ) -> list[list[int]]:
        adj_list: list[list[int]] = [[] for _ in range(size)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

    def find_diameter(
        self, adj_list: list[list[int]], node: int, parent: int
    ) -> tuple[int, int]:
        max_depth1 = max_depth2 = 0
        diameter: int = 0
        for neighbor in adj_list[node]:
            if neighbor == parent:
                continue
            child_diameter, depth = self.find_diameter(adj_list, neighbor, node)
            depth += 1
            diameter = max(diameter, child_diameter)
            if depth > max_depth1:
                max_depth2 = max_depth1
                max_depth1 = depth
            elif depth > max_depth2:
                max_depth2 = depth
        diameter = max(diameter, max_depth1 + max_depth2)
        return diameter, max_depth1

# C++ O(N + M) O(N + M)
class Solution {
public:
    std::vector<std::vector<int>> buildAdjList(int& size, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> adjList(size, std::vector<int>());
        for (std::vector<int>& edge : edges) {
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }
        return adjList;
    }
    std::vector<int> findDiameter(std::vector<std::vector<int>>& adjList, int& node, int& parent) {
        int maxDepth1 = 0, maxDepth2 = 0;
        int diameter = 0;
        for (int& neighbor : adjList[node]) {
            if (neighbor == parent) {
                continue;
            }
            std::vector<int> res = findDiameter(adjList, neighbor, node);
            int childDiameter = res[0];
            int depth = res[1] + 1;
            diameter = std::max(diameter, childDiameter);
            if (depth > maxDepth1) {
                maxDepth2 = maxDepth1;
                maxDepth1 = depth;
            } else if (depth > maxDepth2) {
                maxDepth2 = depth;
            }
        }
        diameter = std::max(diameter, maxDepth1 + maxDepth2);
        return {diameter, maxDepth1};
    }

    int minimumDiameterAfterMerge(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = edges1.size() + 1;
        int m = edges2.size() + 1;
        std::vector<std::vector<int>> adjList1 = buildAdjList(n, edges1);
        std::vector<std::vector<int>> adjList2 = buildAdjList(m, edges2);
        int node = 0, parent = -1;
        int diameter1 = findDiameter(adjList1, node, parent)[0];
        int diameter2 = findDiameter(adjList2, node, parent)[0];
        int combinedDiameter = (diameter1 + 1) / 2 + (diameter2 + 1) / 2 + 1;
        return std::max(diameter1, std::max(diameter2, combinedDiameter));
    }
};