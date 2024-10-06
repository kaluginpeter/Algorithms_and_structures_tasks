# You are maintaining a project that has n methods numbered from 0 to n - 1.
#
# You are given two integers n and k, and a 2D integer array invocations, where invocations[i] = [ai, bi] indicates that method ai invokes method bi.
#
# There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are considered suspicious and we aim to remove them.
#
# A group of methods can only be removed if no method outside the group invokes any methods within it.
#
# Return an array containing all the remaining methods after removing all the suspicious methods. You may return the answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.
#
#
#
# Example 1:
#
# Input: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]
#
# Output: [0,1,2,3]
#
# Explanation:
#
#
#
# Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.
#
# Example 2:
#
# Input: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]
#
# Output: [3,4]
#
# Explanation:
#
#
#
# Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove them.
#
# Example 3:
#
# Input: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]
#
# Output: []
#
# Explanation:
#
#
#
# All methods are suspicious. We can remove them.
#
#
#
# Constraints:
#
# 1 <= n <= 105
# 0 <= k <= n - 1
# 0 <= invocations.length <= 2 * 105
# invocations[i] == [ai, bi]
# 0 <= ai, bi <= n - 1
# ai != bi
# invocations[i] != invocations[j]
# Solution
# Python O(V(V + E)) O(V + E) Depth-First-Search
class Solution:
    def traverse(self, start: int, maps: dict[int, set[int]], visited: set[int]) -> None:
        nodes: list[int] = [start]
        while nodes:
            cur_node: int = nodes.pop()
            if cur_node in visited:
                continue
            visited.add(cur_node)
            for child in maps.get(cur_node, []):
                if child not in visited:
                    nodes.append(child)

    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        adj_list: dict[int, set[int]] = {}
        for a, b in invocations:
            if a not in adj_list:
                adj_list[a] = set()
            adj_list[a].add(b)
        invalid: set[int] = set()
        valid: set[int] = set()
        self.traverse(k, adj_list, invalid)
        for node in range(n):
            if node not in invalid:
                self.traverse(node, adj_list, valid)
        if any(node in valid for node in invalid):
            return list(range(n))
        return list(valid)

# C++ O(V(V + E) O(V + E) Depth-First-Search
class Solution {
public:
    void traverse(int start, std::unordered_map<int, std::unordered_set<int>>& adj_list, std::unordered_set<int>& visited) {
        std::vector<int> nodes = {start};
        while (nodes.size()) {
            int cur_node = nodes[nodes.size() - 1];
            nodes.pop_back();
            if (visited.count(cur_node)) {
                continue;
            }
            visited.insert(cur_node);
            for (int child : adj_list[cur_node]) {
                if (!visited.count(child)) {
                    nodes.push_back(child);
                }
            }
        }
    }
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        std::unordered_map<int, std::unordered_set<int>> adj_list;
        for (vector<int> pair : invocations) {
            int source = pair[0], destination = pair[1];
            adj_list[source].insert(destination);
        }
        std::unordered_set<int> invalid, valid;
        traverse(k, adj_list, invalid);
        for (int node = 0; node < n; ++node) {
            if (invalid.count(node)) {
                continue;
            }
            traverse(node, adj_list, valid);
        }
        for (int node : invalid) {
            if (valid.count(node)) {
                std::vector<int> output;
                for (int i = 0; i < n; ++i) {
                    output.push_back(i);
                }
                return output;
            }
        }
        std::vector<int> output;
        for (int node : valid) {
            output.push_back(node);
        }
        return output;
    }
};