# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:
#
# Input: nums = [1,2,3]
# Output: 3
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
# Solution
# Python O(N) O(N) DynamicProgramming
class Solution:
    def rob(self, nums: List[int]) -> int:
        n: int = len(nums)
        dp: list[int] = [0] * n
        output: int = max(nums)
        for i in range(n - 1):
            dp[i] = max((dp[i - 1] if i else 0), (dp[i - 2] if i >= 2 else 0) + nums[i])
            output = max(output, dp[i])
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max((dp[i - 1] if i else 0), (dp[i - 2] if i >= 2 else 0) + nums[i])
            output = max(output, dp[i])
        return output

# C++ O(N) O(N) DynamicProgramming
class Solution {
public:
    int rob(vector<int>& nums) {
        size_t n = nums.size();
        std::vector<int> dp(n, 0);
        int output = *std::max_element(nums.begin(), nums.end());
        for (size_t i = 0; i < n - 1; ++i) {
            dp[i] = std::max((i ? dp[i - 1] : 0), (i >= 2 ? dp[i - 2] : 0) + nums[i]);
            output = std::max(output, dp[i]);
        }
        std::fill(dp.begin(), dp.end(), 0);
        for (size_t i = 1; i < n; ++i) {
            dp[i] = std::max((i ? dp[i - 1] : 0), (i >= 2 ? dp[i - 2] : 0) + nums[i]);
            output = std::max(output, dp[i]);
        }
        return output;
    }
};