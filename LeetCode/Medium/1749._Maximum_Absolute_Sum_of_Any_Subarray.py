# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
#
# Return the maximum absolute sum of any (possibly empty) subarray of nums.
#
# Note that abs(x) is defined as follows:
#
# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
#
#
# Example 1:
#
# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
# Example 2:
#
# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# Solution
# Python O(N) O(1) Kadane Dynamic Programming
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum: int = 0
        max_sum: int = 0
        cur_min_sum: int = 0
        cur_max_sum: int = 0
        for num in nums:
            cur_min_sum = min(cur_min_sum + num, 0)
            cur_max_sum = max(cur_max_sum + num, 0)
            min_sum = min(min_sum, cur_min_sum)
            max_sum = max(max_sum, cur_max_sum)
        return max(abs(min_sum), max_sum)

# C++ O(N) O(1) Kadane DynamicProgramming
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        long long maxSum = 0;
        long long minSum = 0;
        long long curMaxSum = 0;
        long long curMinSum = 0;
        for (int& num : nums) {
            curMaxSum = std::max(curMaxSum + num, 0LL);
            maxSum = std::max(maxSum, curMaxSum);
            curMinSum = std::min(curMinSum + num, 0LL);
            minSum = std::min(minSum, curMinSum);
        }
        return std::max(std::abs(minSum), maxSum);
    }
};