# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
#
# Notice that you can not jump outside of the array at any time.
#
#
#
# Example 1:
#
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3
# Example 2:
#
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true
# Explanation:
# One possible way to reach at index 3 with value 0 is:
# index 0 -> index 4 -> index 1 -> index 3
# Example 3:
#
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
#
#
# Constraints:
#
# 1 <= arr.length <= 5 * 104
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length
# Solution
# Python O(N) O(N) Breadth-First-Search Depth-First-Search DynamicProgramming
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n: int = len(arr)
        seen: list[bool] = [False] * n
        seen[start] = True
        cur_nodes: list[int] = [start]
        while cur_nodes:
            cur_pos: int = cur_nodes.pop()
            if not arr[cur_pos]: return True
            # left move
            if cur_pos >= arr[cur_pos] and not seen[cur_pos - arr[cur_pos]]:
                cur_nodes.append(cur_pos - arr[cur_pos])
                seen[cur_pos - arr[cur_pos]] = True
            # right move
            if cur_pos + arr[cur_pos] < n and not seen[cur_pos + arr[cur_pos]]:
                cur_nodes.append(cur_pos + arr[cur_pos])
                seen[cur_pos + arr[cur_pos]] = True
        return False

# C++ O(N) O(N) Breadth-First-Search Depth-First-Search DynamicProgramming
class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        size_t n = arr.size();
        std::vector<bool> seen(n, false);
        seen[start] = true;
        std::vector<size_t> curNodes = {static_cast<size_t>(start)};
        while (!curNodes.empty()) {
            size_t curPos = curNodes.back();
            curNodes.pop_back();
            if (!arr[curPos]) return true;
            // left move
            if (curPos >= arr[curPos] && !seen[curPos - arr[curPos]]) {
                curNodes.push_back(curPos - arr[curPos]);
                seen[curPos - arr[curPos]] = true;
            }
            // right move
            if (curPos + arr[curPos] < n && !seen[curPos + arr[curPos]]) {
                curNodes.push_back(curPos + arr[curPos]);
                seen[curPos + arr[curPos]] = true;
            }
        }
        return false;
    }
};


# Python O(V) O(V) Graph
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n: int = len(arr)
        seen: list[bool] = [False] * n
        nodes: list[int] = [start]
        while nodes:
            node: int = nodes.pop()
            if seen[node]: continue
            seen[node] = True
            if node - arr[node] >= 0 and not seen[node - arr[node]]:
                nodes.append(node - arr[node])
            if node + arr[node] < n and not seen[node + arr[node]]:
                nodes.append(node + arr[node])
        return any(not arr[vertex] and seen[vertex] for vertex in range(n))

# C++ O(V) O(V) Graph
class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        std::vector<bool> seen(n, false);
        std::vector<int> nodes = {start};
        while (!nodes.empty()) {
            int node = nodes.back();
            nodes.pop_back();
            if (seen[node]) continue;
            seen[node] = true;
            if (node - arr[node] >= 0 && !seen[node - arr[node]]) nodes.push_back(node - arr[node]);
            if (node + arr[node] < n && !seen[node + arr[node]]) nodes.push_back(node + arr[node]);
        }
        for (int i = 0; i < n; ++i) {
            if (!arr[i] && seen[i]) return true;
        }
        return false;
    }
};