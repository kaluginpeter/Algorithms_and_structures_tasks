# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
#
# The test cases are generated so that the answer can fit in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:
#
# Input: nums = [9], target = 3
# Output: 0
#
#
# Constraints:
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
#
#
# Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
# Solution
# Python O(NT) O(T) DynamicProgramming
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp: list[int] = [0] * (target + 1)
        dp[0] = 1
        mod: int = 1 << 32 - 1
        for subset in range(1, target + 1):
            for num in nums:
                if subset - num < 0 or not dp[subset - num]: continue
                dp[subset] = (dp[subset] + dp[subset - num]) % mod
        return dp[target]

# C++ O(NT) O(T) DynamicProgramming
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        std::vector<unsigned int> dp(target + 1, 0); // use unsigned to avoid overflow error
        dp[0] = 1;
        for (int subset = 0; subset <= target; ++subset) {
            for (const int &num : nums) {
                if (subset - num < 0 || !dp[subset - num]) continue;
                dp[subset] += dp[subset - num];
            }
        }
        return dp[target];
    }
};