# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
#
# A subarray is a contiguous part of an array.
#
#
#
# Example 1:
#
# Input: nums = [1], k = 1
# Output: 1
# Example 2:
#
# Input: nums = [1,2], k = 4
# Output: -1
# Example 3:
#
# Input: nums = [2,-1,2], k = 3
# Output: 3
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
# 1 <= k <= 109
# Solution
# Python O(NlogN) O(N) Priority Queue
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        min_heap: list[tuple[int, int]] = []
        cur_prefix_sum: int = 0
        min_subarray: int = float('inf')
        for right in range(len(nums)):
            cur_prefix_sum += nums[right]
            if cur_prefix_sum >= k:
                min_subarray = min(min_subarray, right + 1)
            while min_heap and cur_prefix_sum - min_heap[0][0] >= k:
                prev_prefix_sum, prev_prefix_idx = heapq.heappop(min_heap)
                min_subarray = min(min_subarray, right - prev_prefix_idx)
            heapq.heappush(min_heap, (cur_prefix_sum, right))
        return min_subarray if min_subarray != float('inf') else -1

# C++ O(NlogN) O(N) Priority Queue
#include <cmath>
#include <queue>
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int minSubarray = std::pow(10, 5) + 1;
        std::priority_queue<std::pair<long long, int>,
                        std::vector<std::pair<long long, int>>,
                        std::greater<std::pair<long long, int>>> minHeap;
        long long curPrefixSum = 0;
        int n = nums.size();
        for (int right = 0; right < n; ++right) {
            curPrefixSum += nums[right];
            if (curPrefixSum >= k) {
                minSubarray = std::min(minSubarray, right + 1);
            }
            while (minHeap.size() && curPrefixSum - minHeap.top().first >= k) {
                minSubarray = std::min(minSubarray, right - minHeap.top().second);
                minHeap.pop();
            }
            minHeap.push({curPrefixSum, right});
        }
        return (minSubarray != std::pow(10, 5) + 1? minSubarray : -1);
    }
};

# Python O(N) O(N) Monotonic Increasing Queue
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        stack: list[tuple[int, int]] = deque()
        cur_prefix_sum: int = 0
        min_subarray: int = float('inf')
        for right in range(len(nums)):
            cur_prefix_sum += nums[right]
            if cur_prefix_sum >= k:
                min_subarray = min(min_subarray, right + 1)
            while stack and cur_prefix_sum - stack[0][0] >= k:
                min_subarray = min(min_subarray, right - stack.popleft()[1])
            while stack and stack[-1][0] >= cur_prefix_sum:
                stack.pop()
            stack.append((cur_prefix_sum, right))
        return min_subarray if min_subarray != float('inf') else -1

# C++ O(N) O(N) Monotonic Increasing Queue
#include <deque>
#include <cmath>
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        std::deque<std::pair<long long, int>> dq;
        long long cur_prefix_sum = 0;
        int minSubarray = std::pow(10, 5) + 1;
        int n = nums.size();
        for (int right = 0; right < n; ++right) {
            cur_prefix_sum += nums[right];
            if (cur_prefix_sum >= k) {
                minSubarray = std::min(minSubarray, right + 1);
            }
            while (dq.size() && cur_prefix_sum - dq.front().first >= k) {
                minSubarray = std::min(minSubarray, right - dq.front().second);
                dq.pop_front();
            }
            while (dq.size() && dq.back().first >= cur_prefix_sum) {
                dq.pop_back();
            }
            dq.push_back({cur_prefix_sum, right});
        }
        return (minSubarray != std::pow(10, 5) + 1? minSubarray : -1);
    }
};