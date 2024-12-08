# You are given an array of integers nums and an integer k.
#
# Return the maximum sum of a non-empty subarray of nums, such that the size of the subarray is divisible by k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2], k = 1
#
# Output: 3
#
# Explanation:
#
# The subarray [1, 2] with sum 3 has length equal to 2 which is divisible by 1.
#
# Example 2:
#
# Input: nums = [-1,-2,-3,-4,-5], k = 4
#
# Output: -10
#
# Explanation:
#
# The maximum sum subarray is [-1, -2, -3, -4] which has length equal to 4 which is divisible by 4.
#
# Example 3:
#
# Input: nums = [-5,1,2,-3,4], k = 2
#
# Output: 4
#
# Explanation:
#
# The maximum sum subarray is [1, 2, -3, 4] which has length equal to 4 which is divisible by 2.
#
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 2 * 105
# -109 <= nums[i] <= 109
# Solution
# Python O(N) O(N) Prefix Sum
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        prefix_sum: list[int] = list()
        for idx in range(n):
            if not idx: prefix_sum.append(nums[idx])
            else: prefix_sum.append(nums[idx] + prefix_sum[-1])
        min_prefix_sum: list[int] = [float('inf')] * k
        min_prefix_sum[-1] = 0
        max_sum: int = float('-inf')
        for idx in range(n):
            max_sum = max(max_sum, prefix_sum[idx] - min_prefix_sum[idx % k])
            min_prefix_sum[idx % k] = min(min_prefix_sum[idx % k], prefix_sum[idx])
        return max_sum

# C++ O(N) O(N) PrefixSum
class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        std::vector<long long> prefixSum;
        for (int idx = 0; idx < n; ++idx) {
            if (!idx) {
                prefixSum.push_back(nums[idx]);
            } else {
                prefixSum.push_back(nums[idx] + prefixSum[idx - 1]);
            }
        }
        std::vector<long long> minPrefixSum(k, 1000000000000000);
        minPrefixSum[k - 1] = 0;
        long long maxScore = -1000000000000000;
        for (int idx = 0; idx < n; ++idx) {
            int remainder = idx % k;
            maxScore = std::max(maxScore, prefixSum[idx] - minPrefixSum[remainder]);
            minPrefixSum[remainder] = std::min(minPrefixSum[remainder], prefixSum[idx]);
        }
        return maxScore;
    }
};