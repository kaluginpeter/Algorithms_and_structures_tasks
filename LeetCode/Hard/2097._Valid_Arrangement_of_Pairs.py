# You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.
#
# Return any valid arrangement of pairs.
#
# Note: The inputs will be generated such that there exists a valid arrangement of pairs.
#
#
#
# Example 1:
#
# Input: pairs = [[5,1],[4,5],[11,9],[9,4]]
# Output: [[11,9],[9,4],[4,5],[5,1]]
# Explanation:
# This is a valid arrangement since endi-1 always equals starti.
# end0 = 9 == 9 = start1
# end1 = 4 == 4 = start2
# end2 = 5 == 5 = start3
# Example 2:
#
# Input: pairs = [[1,3],[3,2],[2,1]]
# Output: [[1,3],[3,2],[2,1]]
# Explanation:
# This is a valid arrangement since endi-1 always equals starti.
# end0 = 3 == 3 = start1
# end1 = 2 == 2 = start2
# The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also valid.
# Example 3:
#
# Input: pairs = [[1,2],[1,3],[2,1]]
# Output: [[1,2],[2,1],[1,3]]
# Explanation:
# This is a valid arrangement since endi-1 always equals starti.
# end0 = 2 == 2 = start1
# end1 = 1 == 1 = start2
#
#
# Constraints:
#
# 1 <= pairs.length <= 105
# pairs[i].length == 2
# 0 <= starti, endi <= 109
# starti != endi
# No two pairs are exactly the same.
# There exists a valid arrangement of pairs.
# Solution
# Python O(V+ E) Eulerian Circuit
from collections import defaultdict, deque
class Solution:
    def validArrangement(self, pairs):
        adj_list: dict[int, list[int]] = defaultdict(deque)
        in_degree, out_degree = defaultdict(int), defaultdict(int)
        for pair in pairs:
            start, end = pair
            adj_list[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        path: list[int] = []
        def visit(node: int) -> None:
            while adj_list[node]:
                next_node: int = adj_list[node].popleft()
                visit(next_node)
            path.append(node)

        start_node: int = pairs[0][0]
        for node in out_degree:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break
        visit(start_node)
        path.reverse()
        output: list[list[int]] = [
            [path[i - 1], path[i]] for i in range(1, len(path))
        ]
        return output

# C++ O(V + E) O(V + E) Eulerian Circuit
class Solution {
public:
    void visit(int& node, std::unordered_map<int, std::deque<int>>& adjList, std::vector<int>& path) {
        while (!adjList[node].empty()) {
            int nextNode = adjList[node].front();
            adjList[node].pop_front();
            visit(nextNode, adjList, path);
        }
        path.push_back(node);
    }
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        std::unordered_map<int, std::deque<int>> adjList;
        std::unordered_map<int, int> inDegree, outDegree;
        for (std::vector<int>& pair : pairs) {
            int start = pair[0], end = pair[1];
            adjList[start].push_back(end);
            ++inDegree[end];
            ++outDegree[start];
        }
        std::vector<int> path;
        int startNode = pairs[0][0];
        for (auto& node : outDegree) {
            if (node.second - inDegree[node.first] == 1) {
                startNode = node.first;
                break;
            }
        }
        visit(startNode, adjList, path);
        std::vector<std::vector<int>> output;
        int n = path.size();
        for (int idx = n - 2; idx >= 0; --idx) {
            output.push_back({path[idx + 1], path[idx]});
        }
        return output;
    }
};