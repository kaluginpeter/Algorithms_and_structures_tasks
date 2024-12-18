# You are given an integer array nums, an integer k, and an integer multiplier.
#
# You need to perform k operations on nums. In each operation:
#
# Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.
#
#
#
# Example 1:
#
# Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
#
# Output: [8,4,6,5,6]
#
# Explanation:
#
# Operation	Result
# After operation 1	[2, 2, 3, 5, 6]
# After operation 2	[4, 2, 3, 5, 6]
# After operation 3	[4, 4, 3, 5, 6]
# After operation 4	[4, 4, 6, 5, 6]
# After operation 5	[8, 4, 6, 5, 6]
# Example 2:
#
# Input: nums = [1,2], k = 3, multiplier = 4
#
# Output: [16,8]
#
# Explanation:
#
# Operation	Result
# After operation 1	[4, 2]
# After operation 2	[4, 8]
# After operation 3	[16, 8]
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= k <= 10
# 1 <= multiplier <= 5
# Solution Heap Simulation O(NlogN + KlogN) O(N)
import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap: list[int] = []
        for idx in range(len(nums)):
            heapq.heappush(heap, (nums[idx], idx))
        for _ in range(k):
            curr_num, idx = heapq.heappop(heap)
            heapq.heappush(heap, (curr_num * multiplier, idx))
        while heap:
            curr_num, idx = heapq.heappop(heap)
            nums[idx] = curr_num
        return nums

# C++ O(NlogN + KlogN) O(N) Priority Queue
class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> maxHeap;
        for (int idx =  0; idx < nums.size(); ++idx) {
            maxHeap.push({nums[idx], idx});
        }
        for (int i = 0; i < k; ++i) {
            int num = maxHeap.top().first;
            int idx = maxHeap.top().second;
            maxHeap.pop();
            num *= multiplier;
            nums[idx] = num;
            maxHeap.push({num, idx});
        }
        return nums;
    }
};