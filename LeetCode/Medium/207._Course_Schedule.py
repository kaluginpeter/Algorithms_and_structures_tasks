# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
#
# Constraints:
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# Solution
# Python O(V + E) O(V + E) TopologicalSorting Graph Depth-First-Search
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree: list[int] = [0] * numCourses
        adj_list: list[list[int]] = [[] for _ in range(numCourses)]
        edges: int = 0
        for u, v in prerequisites:
            in_degree[u] += 1
            adj_list[v].append(u)
        graph: list[int] = []
        for vertex in range(numCourses):
            if in_degree[vertex]: continue
            edges += 1
            graph.append(vertex)
        if not graph and edges: return False
        colors: list[int] = [0] * numCourses
        while graph:
            vertex: int = graph.pop()
            if not colors[vertex]:
                colors[vertex] = 1
                graph.append(vertex)
                for neighbor in adj_list[vertex]:
                    if colors[neighbor] == 1: return False
                    elif colors[neighbor]: continue
                    graph.append(neighbor)
            else: colors[vertex] = 2
        return all(colors[vertex] for vertex in range(numCourses))

# C++ O(V + E) O(V + E) Graph Depth-First-Search TopologicalSorting
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::vector<int> inDegree(numCourses, 0);
        std::vector<std::vector<int>> adjList(numCourses, std::vector<int>());
        size_t edges = 0;
        for (const std::vector<int> &p : prerequisites) {
            ++inDegree[p[0]];
            ++edges;
            adjList[p[1]].push_back(p[0]);
        }
        std::vector<int> graph;
        for (int vertex = 0; vertex < numCourses; ++vertex) {
            if (inDegree[vertex]) continue;
            graph.push_back(vertex);
        }
        std::vector<int> colors(numCourses, 0);
        while (!graph.empty()) {
            int vertex = graph.back();
            graph.pop_back();
            if (!colors[vertex]) {
                colors[vertex] = 1;
                graph.push_back(vertex);
                for (int &neighbor : adjList[vertex]) {
                    if (colors[neighbor] == 1) return false;
                    else if (colors[neighbor] == 2) continue;
                    graph.push_back(neighbor);
                }
            } else colors[vertex] = 2;
        }
        for (int vertex = 0; vertex < numCourses; ++vertex) {
            if (!colors[vertex]) return false;
        }
        return true;
    }
};