# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
#
# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
#
# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
#
#
#
# Example 1:
#
# Illustration of graph
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
# Example 2:
#
# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# Output: [4]
# Explanation:
# Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
#
#
# Constraints:
#
# n == graph.length
# 1 <= n <= 104
# 0 <= graph[i].length <= n
# 0 <= graph[i][j] <= n - 1
# graph[i] is sorted in a strictly increasing order.
# The graph may contain self-loops.
# The number of edges in the graph will be in the range [1, 4 * 104].
# Solution
# Python O(V + E) O(V + E) Topological Sorting Graph
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n: int = len(graph)
        adj_list: list[list[int]] = [[] for _ in range(n)]
        indegree: list[int] = [0] * n
        for source in range(n):
            for destination in graph[source]:
                adj_list[destination].append(source)
                indegree[source] += 1
        cur_nodes: list[int] = []
        next_nodes: list[int] = []
        for vertex in range(n):
            if not indegree[vertex]: cur_nodes.append(vertex)
        safe: list[bool] = [False] * n
        while cur_nodes:
            for vertex in cur_nodes:
                safe[vertex] = True
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    if not indegree[neighbor]:
                        next_nodes.append(neighbor)
            cur_nodes = next_nodes
            next_nodes = []
        output: list[int] = []
        for vertex in range(n):
            if safe[vertex]: output.append(vertex)
        return output

# C++ O(V + E) O(V + E) Topological Sorting Graph
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        std::vector<std::vector<int>> adjList (n, std::vector<int>());
        std::vector<int> indegree (n, 0);
        for (int source = 0; source < n; ++source) {
            for (int& destination : graph[source]) {
                adjList[destination].push_back(source);
                ++indegree[source];
            }
        }
        std::vector<int> curNodes;
        std::vector<int> nextNodes;
        for (int vertex = 0; vertex < n; ++vertex) {
            if (!indegree[vertex]) curNodes.push_back(vertex);
        }
        std::vector<bool> safe (n, false);
        while (curNodes.size() > 0) {
            for (int& vertex : curNodes) {
                safe[vertex] = true;
                for (int& neighbor : adjList[vertex]) {
                    --indegree[neighbor];
                    if (!indegree[neighbor]) nextNodes.push_back(neighbor);
                }
            }
            curNodes = nextNodes;
            nextNodes = {};
        }
        std::vector<int> output;
        for (int vertex = 0; vertex < n; ++vertex) {
            if (safe[vertex]) output.push_back(vertex);
        }
        return output;
    }
};