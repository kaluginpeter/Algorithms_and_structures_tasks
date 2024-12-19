# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
#
# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
#
# Return the largest number of chunks we can make to sort the array.
#
#
#
# Example 1:
#
# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
# Example 2:
#
# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
#
#
# Constraints:
#
# n == arr.length
# 1 <= n <= 10
# 0 <= arr[i] < n
# All the elements of arr are unique.
# Solution
# Python O(N) O(1) Greedy
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks: int = 0
        n: int = len(arr)
        local_idx: int = 0
        for idx in range(n):
            if arr[idx] > idx:
                local_idx = max(local_idx, arr[idx])
            elif local_idx == idx:
                chunks += 1
                if local_idx + 1 < n:
                    local_idx += 1
        return chunks
# C++ O(N) O(1) Greedy
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int chunks = 0;
        int n = arr.size();
        int localIdx = 0;
        for (int idx = 0; idx < n; ++idx) {
            if (arr[idx] > idx) {
                localIdx = std::max(localIdx, arr[idx]);
            } else if (localIdx == idx) {
                ++chunks;
                if (localIdx + 1 < n) {
                    ++localIdx;
                }
            }
        }
        return chunks;
    }
};