# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:
#
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:
#
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#
#
# Constraints:
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
# Solution
# Python O(V + E) O(V + E) Depth-First-Search Graph TopologicalSorting
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output: list[int] = []
        in_degree: list[int] = [0] * numCourses
        adj_list: list[list[int]] = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            in_degree[u] += 1
            adj_list[v].append(u)
        graph: list[int] = []
        for vertex in range(numCourses):
            if in_degree[vertex]: continue
            graph.append(vertex)
        colors: list[int] = [0] * numCourses
        while graph:
            vertex: int = graph.pop()
            if not colors[vertex]:
                colors[vertex] = 1
                graph.append(vertex)
                for neighbor in adj_list[vertex]:
                    if colors[neighbor] == 1: return []
                    elif colors[neighbor]: continue
                    graph.append(neighbor)
            else:
                if colors[vertex] == 2: continue
                output.append(vertex)
                colors[vertex] = 2
        if len(output) != numCourses: return []
        output.reverse()
        return output

# C++ O(V + E) O(V + E) Graph TopologicalSorting Depth-First-Search
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        std::vector<int> output;
        std::vector<int> inDegree(numCourses, 0);
        std::vector<std::vector<int>> adjList(numCourses, std::vector<int>());
        for (const std::vector<int> &p : prerequisites) {
            ++inDegree[p[0]];
            adjList[p[1]].push_back(p[0]);
        }
        std::vector<int> graph, colors(numCourses, 0);
        for (int vertex = 0; vertex < numCourses; ++vertex) {
            if (inDegree[vertex]) continue;
            graph.push_back(vertex);
        }
        while (!graph.empty()) {
            int vertex = graph.back();
            graph.pop_back();
            if (!colors[vertex]) {
                graph.push_back(vertex);
                colors[vertex] = 1;
                for (int &neighbor : adjList[vertex]) {
                    if (colors[neighbor] == 1) return std::vector<int>();
                    else if (colors[neighbor]) continue;
                    graph.push_back(neighbor);
                }
            } else {
                if (colors[vertex] == 2) continue;
                colors[vertex] = 2;
                output.push_back(vertex);
            }
        }
        if (output.size() != numCourses) return std::vector<int>();
        std::reverse(output.begin(), output.end());
        return output;
    }
};