# Given an array of integers arr, you are initially positioned at the first index of the array.
#
# In one step you can jump from index i to index:
#
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.
#
# Notice that you can not jump outside of the array at any time.
#
#
#
# Example 1:
#
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
# Example 2:
#
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You do not need to jump.
# Example 3:
#
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
#
#
# Constraints:
#
# 1 <= arr.length <= 5 * 104
# -108 <= arr[i] <= 108
# Solution
# Python O(V + E) O(V + E) Graph Breadth-First-Search
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n: int = len(arr)
        extras: dict[int, set[int]] = defaultdict(set)
        for i in range(n): extras[arr[i]].add(i)
        cur_nodes: list[int] = [0]
        next_nodes: list[int] = []
        seen: list[int] = [float('inf')] * n
        seen[0] = 0
        steps: int = 1
        while cur_nodes:
            for i in cur_nodes:
                if steps - 1 > seen[i]: continue
                if i == n - 1: return steps - 1
                if i and seen[i - 1] > steps:
                    seen[i - 1] = steps
                    next_nodes.append(i - 1)
                if i + 1 < n and seen[i + 1] > steps:
                    seen[i + 1] = steps
                    next_nodes.append(i + 1)
                for j in extras[arr[i]].copy():
                    if steps >= seen[j]:
                        extras[arr[i]].remove(j)
                        continue
                    seen[j] = steps
                    next_nodes.append(j)
            cur_nodes = next_nodes.copy()
            next_nodes.clear()
            steps += 1
        return -1

# C++ O(V + E) O(V + E) Breadth-First-Search Graph
class Solution {
public:
    int minJumps(vector<int>& arr) {
        size_t n = arr.size();
        std::unordered_map<int, std::unordered_set<int>> extras;
        for (size_t i = 0; i < n; ++i) {
            extras[arr[i]].insert(i);
        }
        std::vector<int> curNodes = {0}, nextNodes;
        std::vector<int> seen(n, INT32_MAX);
        seen[0] = 0;
        int steps = 1;
        while (!curNodes.empty()) {
            for (int& i : curNodes) {
                if (i == n - 1) return steps - 1;
                if (steps - 1 > seen[i]) continue;
                if (i && seen[i - 1] > steps) {
                    seen[i - 1] = steps;
                    nextNodes.push_back(i - 1);
                }
                if (i + 1 < n && seen[i + 1] > steps) {
                    seen[i + 1] = steps;
                    nextNodes.push_back(i + 1);
                }
                std::unordered_set<int> toDelete;
                for (const int& j : extras[arr[i]]) {
                    if (seen[j] <= steps) {
                        toDelete.insert(j);
                        continue;
                    }
                    seen[j] = steps;
                    nextNodes.push_back(j);
                }
                for (const int& j : toDelete) extras[arr[i]].erase(j);
            }
            curNodes = nextNodes;
            nextNodes.clear();
            ++steps;
        }
        return -1;
    }
};