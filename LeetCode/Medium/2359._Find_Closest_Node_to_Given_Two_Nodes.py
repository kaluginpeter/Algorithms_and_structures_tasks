# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
#
# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.
#
# You are also given two integers node1 and node2.
#
# Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.
#
# Note that edges may contain cycles.
#
#
#
# Example 1:
#
#
# Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
# Output: 2
# Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
# The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
# Example 2:
#
#
# Input: edges = [1,2,-1], node1 = 0, node2 = 2
# Output: 2
# Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
# The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
#
#
# Constraints:
#
# n == edges.length
# 2 <= n <= 105
# -1 <= edges[i] < n
# edges[i] != i
# 0 <= node1, node2 < n
# Solution
# Python O(N) O(N) Depth-First-Search Tree
class Solution:
    def destinate_all(self, source: int, adj_list: list[int], seen: list[int]) -> None:
        step: int = 0
        cur_node: int = source
        while cur_node != -1:
            seen[cur_node] = step
            if adj_list[cur_node] != -1 and seen[adj_list[cur_node]] == -1: cur_node = adj_list[cur_node]
            else: cur_node = -1
            step += 1

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n: int = len(edges)
        adj_list: list[int] = [-1] * n
        for vertex in range(n):
            adj_list[vertex] = edges[vertex]
        seen_node1: list[int] = [-1] * n
        seen_node2: list[int] = [-1] * n
        self.destinate_all(node1, adj_list, seen_node1)
        self.destinate_all(node2, adj_list, seen_node2)
        output: int = -1
        distance: int = -1
        for vertex in range(n):
            if seen_node1[vertex] == -1 or seen_node2[vertex] == -1: continue
            new_distance: int = max(seen_node1[vertex], seen_node2[vertex])
            if output == -1 or new_distance < distance:
                output = vertex
                distance = new_distance
        return output

# C++ O(N) O(N) Depth-First-Search Tree
class Solution {
public:
    void destinateAll(int source, vector<int> &adjList, vector<int> &seen) {
        int step = 0;
        int curNode = source;
        while (curNode != -1) {
            seen[curNode] = step;
            if (adjList[curNode] != -1 && seen[adjList[curNode]] == -1) curNode = adjList[curNode];
            else curNode = -1;
            ++step;
        }
    }

    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        int n = edges.size();
        vector<int> adjList(n, -1);
        for (int vertex = 0; vertex < n; ++vertex) {
            if (edges[vertex] == -1) continue;
            adjList[vertex] = edges[vertex];
        }
        vector<int> seenNode1 (n, -1), seenNode2(n, -1);
        destinateAll(node1, adjList, seenNode1);
        destinateAll(node2, adjList, seenNode2);
        int output = -1, distance = -1;
        for (int vertex = 0; vertex < n; ++vertex) {
            if (seenNode1[vertex] == -1 || seenNode2[vertex] == -1) continue;
            int newDistance = max(seenNode1[vertex], seenNode2[vertex]);
            if (output == -1 || newDistance < distance) {
                output = vertex;
                distance = newDistance;
            }
        }
        return output;
    }
};