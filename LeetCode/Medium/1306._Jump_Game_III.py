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