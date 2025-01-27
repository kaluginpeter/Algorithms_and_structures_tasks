# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.
#
# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.
#
# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.
#
# Return a boolean array answer, where answer[j] is the answer to the jth query.
#
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
# Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
# Course 0 is not a prerequisite of course 1, but the opposite is true.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
# Output: [false,false]
# Explanation: There are no prerequisites, and each course is independent.
# Example 3:
#
#
# Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# Output: [true,true]
#
#
# Constraints:
#
# 2 <= numCourses <= 100
# 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
# prerequisites[i].length == 2
# 0 <= ai, bi <= numCourses - 1
# ai != bi
# All the pairs [ai, bi] are unique.
# The prerequisites graph has no cycles.
# 1 <= queries.length <= 104
# 0 <= ui, vi <= numCourses - 1
# ui != vi
# Solution
# Python O(Q(V + E)) O(V + E) Graph Depth-First-Search
class Solution:
    def dfs(self, adj_list: dict[int, list[int]], source: int, destination: int, n: int) -> bool:
        colors: list[str] = ['white'] * n
        call_stack: list[int] = [source]
        while call_stack:
            vertex: int = call_stack.pop()
            if vertex == destination: return True
            if colors[vertex] == 'white':
                colors[vertex] = 'grey'
                call_stack.append(vertex)
                for neighbor in adj_list.get(vertex, []):
                    if colors[neighbor] == 'white': call_stack.append(neighbor)
            elif colors[vertex] == 'grey':
                colors[vertex] = 'black'
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        adj_list: dict[int, list[int]] = dict()
        for prereq in prerequisites:
            before, after = prereq
            if before not in adj_list: adj_list[before] = []
            adj_list[before].append(after)
        output: list[bool] = []
        for query in queries:
            seen: list[bool] = [False] * numCourses
            x, y = query
            output.append(self.dfs(adj_list, x, y, numCourses))

        return output

# C++ O(Q(V + E)) O(V + E) Graph Depth-First-Search
class Solution {
public:
    bool dfs(std::unordered_map<int, std::vector<int>>& adjList, int& source, int& destination, int& n) {
        std::vector<std::string> colors (n, "white");
        std::vector<int> callStack = {source};
        while (!callStack.empty()) {
            int& vertex = callStack[callStack.size() - 1];
            callStack.pop_back();
            if (vertex == destination) return true;
            if (colors[vertex] == "white") {
                colors[vertex] = "grey";
                callStack.push_back(vertex);
                for (int& neighbor : adjList[vertex]) {
                    if (colors[neighbor] == "white") callStack.push_back(neighbor);
                }
            } else if (colors[vertex] == "grey") colors[vertex] = "black";
        }
        return false;
    }
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        std::unordered_map<int, std::vector<int>> adjList;
        for (std::vector<int>& prereq : prerequisites) {
            int source = prereq[0];
            int destination = prereq[1];
            adjList[source].push_back(destination);
        }
        std::vector<bool> output;
        for (std::vector<int>& query : queries) {
            int& x = query[0];
            int& y = query[1];
            output.push_back(dfs(adjList, x, y, numCourses));
        }
        return output;
    }
};