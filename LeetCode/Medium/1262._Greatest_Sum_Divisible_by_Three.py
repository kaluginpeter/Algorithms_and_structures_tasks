# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.
#
#
#
# Example 1:
#
# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
# Example 2:
#
# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
# Example 3:
#
# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
#
#
# Constraints:
#
# 1 <= nums.length <= 4 * 104
# 1 <= nums[i] <= 104
# Solution
# Python O(ND) O(D) DynamicProgramming
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp: list[int] = [0, float('-inf'), float('-inf')]
        for num in nums:
            next_dp: list[int] = dp.copy()
            for i in range(3):
                next_dp[(i + num % 3) % 3] = max(next_dp[(i + num % 3) % 3], dp[i] + num)
            dp = next_dp
        return dp[0]

# C++ O(ND) O(D) DynamicProgramming
class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        std::vector<int> dp = {0, INT_MIN, INT_MIN};
        for (int& num : nums) {
            std::vector<int> nextDp = dp;
            for (int i = 0; i < 3; ++i) {
                nextDp[(i + num % 3) % 3] = std::max(
                    nextDp[(i + num % 3) % 3],
                    dp[i] + num
                );
            }
            dp = std::move(nextDp);
        }
        return dp[0];
    }
};