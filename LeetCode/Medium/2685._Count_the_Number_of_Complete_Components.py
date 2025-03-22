# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.
#
# Return the number of complete connected components of the graph.
#
# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
#
# A connected component is said to be complete if there exists an edge between every pair of its vertices.
#
#
#
# Example 1:
#
#
#
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# Output: 3
# Explanation: From the picture above, one can see that all of the components of this graph are complete.
# Example 2:
#
#
#
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# Output: 1
# Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.
#
#
# Constraints:
#
# 1 <= n <= 50
# 0 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated edges.
# Solution
# Python O(|V| + |E|) O(|V| + |E|) Graph Coloring
class Solution:
    def dfs(self, start: int, adj_list: list[list[int]], components: list[int], component: int) -> int:
        components[start] = component
        edges: int = 1
        q: list[int] = [start]
        while q:
            vertex: int = q.pop()
            for neighbor in adj_list[vertex]:
                if components[neighbor] == -1:
                    edges += 1
                    components[neighbor] = component
                    q.append(neighbor)
        return edges

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        components: list[int] = [-1] * n
        components_edges: list[int] = []
        component: int = 0
        for vertex in range(n):
            if components[vertex] == -1:
                amount_edges: int = self.dfs(vertex, adj_list, components, component)
                component += 1
                components_edges.append(amount_edges)
        complete_components: int = component
        for vertex in range(n):
            if components_edges[components[vertex]] != len(adj_list[vertex]) + 1:
                if components_edges[components[vertex]] != -1:
                    complete_components -= 1
                    components_edges[components[vertex]] = -1
        return complete_components

# C++ O(|V| + |E|) O(|V| + |E|) Graph Coloring
class Solution {
public:
    int dfs(int& start, vector<vector<int>>& adjList, vector<int>& components, int& component) {
        int edges = 1;
        components[start] = component;
        queue<int> q;
        q.push(start);
        while (!q.empty()) {
            int& vertex = q.front();
            q.pop();
            for (int& neighbor : adjList[vertex]) {
                if (components[neighbor] == -1) {
                    components[neighbor] = component;
                    q.push(neighbor);
                    ++edges;
                }
            }
        }
        return edges;
    }
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adjList (n, vector<int>());
        for (vector<int>& edge : edges) {
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }
        vector<int> components (n, -1);
        vector<int> componentsEdges;
        int component = 0;
        for (int vertex = 0; vertex < n; ++vertex) {
            if (components[vertex] == -1) {
                int amountEdges = dfs(vertex, adjList, components, component);
                ++component;
                componentsEdges.push_back(amountEdges);
            }
        }
        int completeComponents = component;
        for (int vertex = 0; vertex < n; ++vertex) {
            if (componentsEdges[components[vertex]] != adjList[vertex].size() + 1) {
                if (componentsEdges[components[vertex]] != -1) {
                    --completeComponents;
                    componentsEdges[components[vertex]] = -1;
                }
            }
        }
        return completeComponents;
    }
};