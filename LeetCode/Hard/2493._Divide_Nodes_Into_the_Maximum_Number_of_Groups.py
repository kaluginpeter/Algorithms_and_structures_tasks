# You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.
#
# You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.
#
# Divide the nodes of the graph into m groups (1-indexed) such that:
#
# Each node in the graph belongs to exactly one group.
# For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
# Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.
#
#
#
# Example 1:
#
#
# Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
# Output: 4
# Explanation: As shown in the image we:
# - Add node 5 to the first group.
# - Add node 1 to the second group.
# - Add nodes 2 and 4 to the third group.
# - Add nodes 3 and 6 to the fourth group.
# We can see that every edge is satisfied.
# It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.
# Example 2:
#
# Input: n = 3, edges = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied.
# It can be shown that no grouping is possible.
#
#
# Constraints:
#
# 1 <= n <= 500
# 1 <= edges.length <= 104
# edges[i].length == 2
# 1 <= ai, bi <= n
# ai != bi
# There is at most one edge between any pair of vertices.
# Solution
# Python O(N(N + M)) O(N) Depth-First-Search Graph
class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        adj_list: list[list[int]] = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)
        colors: list[int] = [-1] * n
        for vertex in range(n):
            if colors[vertex] != -1: continue
            colors[vertex] = 0
            if not self.is_bipartite(adj_list, vertex, colors): return -1
        distances: list[int] = [
            self.get_longest_shortest_path(adj_list, vertex, n)
            for vertex in range(n)
        ]
        max_number_of_groups: int = 0
        visited: list[bool] = [False] * n
        for vertex in range(n):
            if visited[vertex]: continue
            max_number_of_groups += self.get_number_of_groups_for_component(
                adj_list, vertex, distances, visited
            )
        return max_number_of_groups

    def is_bipartite(self, adj_list: list[list[int]], source: int, colors: list[int]) -> bool:
        for neighbor in adj_list[source]:
            if colors[neighbor] == colors[source]: return False
            if colors[neighbor] != -1: continue
            colors[neighbor] = (colors[source] + 1) % 2
            if not self.is_bipartite(adj_list, neighbor, colors): return False
        return True

    def get_longest_shortest_path(self, adj_list: list[list[int]], source: int, n: int) -> int:
        cur_nodes: list[int] = [source]
        next_nodes: list[int] = []
        visited: list[bool] = [False] * n
        visited[source] = True
        distance: int = 0
        while cur_nodes:
            for cur_node in cur_nodes:
                for neighbor in adj_list[cur_node]:
                    if visited[neighbor]: continue
                    visited[neighbor] = True
                    next_nodes.append(neighbor)
            distance += 1
            cur_nodes = next_nodes
            next_nodes = []
        return distance

    def get_number_of_groups_for_component(
        self, adj_list: list[list[int]], vertex: int, distances: list[int], visited: list[bool]
    ) -> int:
        max_number_of_groups: int = distances[vertex]
        visited[vertex] = True
        for neighbor in adj_list[vertex]:
            if visited[neighbor]: continue
            max_number_of_groups = max(
                max_number_of_groups,
                self.get_number_of_groups_for_component(
                    adj_list, neighbor, distances, visited
                ),
            )
        return max_number_of_groups

# C++ O(N(N + M)) O(N) Depth-First-Search Graph
class Solution {
public:
    bool isBipartite(std::vector<std::vector<int>>& adjList, int& vertex, std::vector<int>& colors) {
        for (int& neighbor : adjList[vertex]) {
            if (colors[neighbor] == colors[vertex]) return false;
            if (colors[neighbor] != -1) continue;
            colors[neighbor] = (colors[vertex] + 1) % 2;
            if (!isBipartite(adjList, neighbor, colors)) return false;
        }
        return true;
    }
    int getLongest(std::vector<std::vector<int>>& adjList, int& source, int& n) {
        std::vector<int> curNodes = {source};
        std::vector<int> nextNodes;
        std::vector<bool> seen (n, false);
        seen[source] = true;
        int distance = 0;
        while (!curNodes.empty()) {
            for (int& vertex : curNodes) {
                for (int& neighbor : adjList[vertex]) {
                    if (seen[neighbor]) continue;
                    seen[neighbor] = true;
                    nextNodes.push_back(neighbor);
                }
            }
            curNodes = nextNodes;
            nextNodes = {};
            ++distance;
        }
        return distance;
    }
    int getNumberOfGroups(std::vector<std::vector<int>>& adjList, int& source, std::vector<int>& distances, std::vector<bool>& seen) {
        int maxNumberOfGroups = distances[source];
        seen[source] = true;
        for (int& neighbor : adjList[source]) {
            if (seen[neighbor]) continue;
            maxNumberOfGroups = std::max(maxNumberOfGroups, getNumberOfGroups(adjList, neighbor, distances, seen));
        }
        return maxNumberOfGroups;
    }
    int magnificentSets(int n, vector<vector<int>>& edges) {
        std::vector<std::vector<int>> adjList (n);
        for (std::vector<int>& edge : edges) {
            adjList[edge[0] - 1].push_back(edge[1] - 1);
            adjList[edge[1] - 1].push_back(edge[0] - 1);
        }
        std::vector<int> colors (n, -1);
        for (int vertex = 0; vertex < n; ++vertex) {
            if (colors[vertex] != -1) continue;
            colors[vertex] = 0;
            if (!isBipartite(adjList, vertex, colors)) return -1;
        }
        std::vector<int> distances;
        for (int vertex = 0; vertex < n; ++vertex) {
            distances.push_back(getLongest(adjList, vertex, n));
        }
        int maxNumberOfGroups = 0;
        std::vector<bool> seen (n, false);
        for (int vertex = 0; vertex < n; ++vertex) {
            if (seen[vertex]) continue;
            maxNumberOfGroups += getNumberOfGroups(adjList, vertex, distances, seen);
        }
        return maxNumberOfGroups;
    }
};