# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
# Constraints:
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# Solution
# Python O(NK) O(N) DynamicProgramming NumberTheory
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        score: int = sum(nums)
        if score & 1: return False
        score //= 2
        n: int = len(nums)
        prev_dp: list[bool] = [False] * (score + 1)
        cur_dp: list[bool] = [False] * (score + 1)
        prev_dp[0] = True
        for num in nums:
            for cost in range(score, -1, -1):
                cur_dp[cost] = prev_dp[cost]
                if cost >= num:
                    cur_dp[cost] = cur_dp[cost] or prev_dp[cost - num]
            prev_dp = cur_dp
            cur_dp = [False] * (score + 1)
        return prev_dp[score]

# C++ O(NK) O(N) DynamicProgramming NumberTheory
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int totalSum = 0;
        for (int &num : nums) totalSum += num;
        if (totalSum % 2 != 0) return false;
        totalSum /= 2;
        int n = nums.size();
        vector<bool>prevDp (totalSum + 1, false);
        prevDp[0] = true;
        vector<bool> curDp (totalSum + 1, false);
        for (int i = 1; i <= n; ++i) {
            for (int cost = totalSum; cost >= 0; --cost) {
                curDp[cost] = prevDp[cost];
                if (cost >= nums[i - 1]) curDp[cost] = curDp[cost] || prevDp[cost - nums[i - 1]];
            }
            prevDp = curDp;
            curDp = vector<bool>(totalSum + 1, false);
        }
        return prevDp[totalSum];
    }
};