# There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
#
# You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.
#
# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
#
# Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
#
#
#
# Example 1:
#
#
#
# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
# Example 2:
#
#
#
# Input: colors = "a", edges = [[0,0]]
# Output: -1
# Explanation: There is a cycle from 0 to 0.
#
#
# Constraints:
#
# n == colors.length
# m == edges.length
# 1 <= n <= 105
# 0 <= m <= 105
# colors consists of lowercase English letters.
# 0 <= aj, bj < n
# Solution
# Python O(N) O(N26) DynamicProgramming TopologicalSorting
class Solution:
    output: int = 0

    def has_cycle(self, source: int, adj_list: dict[int, list[int]], colors: str, seen: list[int], parent: list[int],
                  nodes_hashmap: list[list[int]]) -> bool:
        cur_nodes: list[int] = [source]
        while cur_nodes:
            node: int = cur_nodes.pop()
            if not seen[node]:
                seen[node] = 1
                cur_nodes.append(node)
                for neighbor in adj_list.get(node, []):
                    if not seen[neighbor]:
                        parent[neighbor] = node
                        cur_nodes.append(neighbor)
                    elif seen[neighbor] == 1:
                        return True
                    else:
                        self.copy_hashmap(neighbor, node, nodes_hashmap)
            elif seen[node] == 1:
                seen[node] = 2
                nodes_hashmap[node][ord(colors[node]) - 97] += 1
                self.copy_hashmap(node, parent[node], nodes_hashmap)
        return False

    def copy_hashmap(self, from_: int, to: int, nodes_hashmap: list[list[int]]) -> None:
        for i in range(26):
            nodes_hashmap[to][i] = max(nodes_hashmap[to][i], nodes_hashmap[from_][i])
            if nodes_hashmap[to][i] > self.output:
                self.output = nodes_hashmap[to][i]

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        self.output = 0
        adj_list: dict[int, list[int]] = dict()
        for u, v in edges:
            if u not in adj_list: adj_list[u] = []
            adj_list[u].append(v)
        n: int = len(colors)
        seen: list[int] = [0] * n
        parent: list[int] = list(range(n))
        nodes_hashmap: list[list[int]] = [[0] * 26 for _ in range(n)]
        for vertex in range(n):
            if not seen[vertex]:
                if self.has_cycle(vertex, adj_list, colors, seen, parent, nodes_hashmap):
                    return -1
        return self.output

# C++ O(N) O(N26) TopologicalSorting DynamicProgramming
class Solution {
public:
    bool hasCycle(int source, unordered_map<int, vector<int>> &adjList, int &n, vector<int> &seen, vector<vector<int>> &nodesHashmap, string &colors, vector<int> &parent, int &output) {
        vector<int> curNodes = {source};
        int prev = -1;
        while (!curNodes.empty()) {
            int node = curNodes.back();
            curNodes.pop_back();
            if (!seen[node]) {
                curNodes.push_back(node);
                seen[node] = 1;
                for (int neighbor : adjList[node]) {
                    if (seen[neighbor] == 0) {
                        parent[neighbor] = node;
                        curNodes.push_back(neighbor);
                        prev = neighbor;
                    }
                    else if (seen[neighbor] == 1) return -1;
                    else copyHashmap(neighbor, node, nodesHashmap, output);
                }
            } else if (seen[node] == 1) {
                seen[node] = 2;
                ++nodesHashmap[node][colors[node] - 'a'];
                copyHashmap(node, parent[node], nodesHashmap, output);
            }
        }
        return false;
    }

    void copyHashmap(int &from, int &to, vector<vector<int>> &nodesHashmap, int &output) {
        for (int i = 0; i < 26; ++i) {
            nodesHashmap[to][i] = max(nodesHashmap[to][i], nodesHashmap[from][i]);
            if (nodesHashmap[to][i] > output) output = nodesHashmap[to][i];
        }
    }

    int largestPathValue(string colors, vector<vector<int>>& edges) {
        unordered_map<int, vector<int>> adjList;
        for (vector<int> &edge: edges) adjList[edge[0]].push_back(edge[1]);
        int n = colors.size();
        vector<vector<int>> nodesHashmap(n, vector<int>(26, 0));
        vector<int> seen(n, 0), parent(n, 0);
        int output = 0;
        for (int vertex = 0; vertex < n; ++vertex) {
            parent[vertex] = vertex;
            if (!seen[vertex]) {
                if (hasCycle(vertex, adjList, n, seen, nodesHashmap, colors, parent, output)) return -1;
            }
        }
        return output;
    }
};