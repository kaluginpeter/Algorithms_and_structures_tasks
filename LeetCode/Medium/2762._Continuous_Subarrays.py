# You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:
#
# Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
# Return the total number of continuous subarrays.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [5,4,2,4]
# Output: 8
# Explanation:
# Continuous subarray of size 1: [5], [4], [2], [4].
# Continuous subarray of size 2: [5,4], [4,2], [2,4].
# Continuous subarray of size 3: [4,2,4].
# Thereare no subarrys of size 4.
# Total continuous subarrays = 4 + 3 + 1 = 8.
# It can be shown that there are no more continuous subarrays.
#
#
# Example 2:
#
# Input: nums = [1,2,3]
# Output: 6
# Explanation:
# Continuous subarray of size 1: [1], [2], [3].
# Continuous subarray of size 2: [1,2], [2,3].
# Continuous subarray of size 3: [1,2,3].
# Total continuous subarrays = 3 + 2 + 1 = 6.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# Solution
# Python O(NlogN) O(N) Priority Queue
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        output: int = 0
        left: int = 0
        min_heap: list[tuple[int, int]] = []
        max_heap: list[tuple[int, int]] = []
        for right in range(len(nums)):
            heapq.heappush(min_heap, (nums[right], right))
            heapq.heappush(max_heap, (-nums[right], right))
            while -max_heap[0][0] - min_heap[0][0] > 2:
                if min_heap[0][1] < max_heap[0][1]:
                    left = heapq.heappop(min_heap)[1] + 1
                else:
                    left = heapq.heappop(max_heap)[1] + 1
            output += right - left + 1
        return output

# C++ O(NlogN) O(N) Priority Queue
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        long long output = 0;
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> minHeap;
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>> maxHeap;
        int left = 0;
        for (int right = 0; right < nums.size(); ++right) {
            minHeap.push({nums[right], right});
            maxHeap.push({nums[right], right});
            while (maxHeap.top().first - minHeap.top().first > 2) {
                if (maxHeap.top().second < minHeap.top().second) {
                    left = std::max(left, maxHeap.top().second + 1);
                    maxHeap.pop();
                } else {
                    left = std::max(left, minHeap.top().second + 1);
                    minHeap.pop();
                }
            }
            output += right - left + 1;
        }
        return output;
    }
};