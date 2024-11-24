# You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.
#
# Return the minimum sum of such a subarray. If no such subarray exists, return -1.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [3, -2, 1, 4], l = 2, r = 3
#
# Output: 1
#
# Explanation:
#
# The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:
#
# [3, -2] with a sum of 1
# [1, 4] with a sum of 5
# [3, -2, 1] with a sum of 2
# [-2, 1, 4] with a sum of 3
# Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.
#
# Example 2:
#
# Input: nums = [-2, 2, -3, 1], l = 2, r = 3
#
# Output: -1
#
# Explanation:
#
# There is no subarray of length between l and r that has a sum greater than 0. So, the answer is -1.
#
# Example 3:
#
# Input: nums = [1, 2, 3, 4], l = 2, r = 4
#
# Output: 3
#
# Explanation:
#
# The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So, the answer is 3.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= l <= r <= nums.length
# -1000 <= nums[i] <= 1000
# Solution
# Python O(KN), where K is r - l + 1 O(1) Sliding Window
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        n: int = len(nums)
        for window_size in range(l, r + 1):
            window_sum: int = sum(nums[:window_size])
            if window_sum > 0:
                min_sum = min(min_sum, window_sum)
            for shrink in range(window_size, n):
                window_sum += nums[shrink]
                window_sum -= nums[shrink - window_size]
                if window_sum > 0:
                    min_sum = min(min_sum, window_sum)
        return min_sum if min_sum != float('inf') else -1

# C++ O(KN), where K is r - l + 1 O(1) Sliding Window
class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int minSum = std::pow(10, 6) + 1;
        int n = nums.size();
        for (int windowSize = l; windowSize < r + 1; ++windowSize) {
            int curSum = 0;
            for (int index = 0; index < windowSize; ++index) {
                curSum += nums[index];
            }
            if (curSum > 0) {
                minSum = std::min(minSum, curSum);
            }
            for (int shrink = windowSize; shrink < n; ++shrink) {
                curSum += nums[shrink];
                curSum -= nums[shrink - windowSize];
                if (curSum > 0) {
                    minSum = std::min(minSum, curSum);
                }
            }
        }
        return (minSum != std::pow(10, 6) + 1? minSum : -1);
    }
};