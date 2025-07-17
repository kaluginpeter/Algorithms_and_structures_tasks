# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
#
# Note that:
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
#
#
# Example 1:
#
# Input: nums = [3,6,9,12]
# Output: 4
# Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
# Example 2:
#
# Input: nums = [9,4,7,2,10]
# Output: 3
# Explanation:  The longest arithmetic subsequence is [4,7,10].
# Example 3:
#
# Input: nums = [20,1,15,3,10,5,8]
# Output: 4
# Explanation:  The longest arithmetic subsequence is [20,15,10,5].
#
#
# Constraints:
#
# 2 <= nums.length <= 1000
# 0 <= nums[i] <= 500
# Solution
# Python O(N^2 + NK) O(NK) DynamicProgramming
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n: int = len(nums)
        m: int = 500
        dp: list[dict[int, int]] = [dict() for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i - 1, 0, -1):
                step: int = nums[i - 1] - nums[j - 1]
                dp[i][step] = max(dp[i].get(step, 0), dp[j].get(step, 1) + 1)
        return max(max(chunk.values()) if chunk else 0 for chunk in dp)

# C++ O(N^2 + NK) O(NK) DynamicProgramming
class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        int n = nums.size(), m = 500;
        std::vector<std::unordered_map<int, int>> dp(n + 1);
        for (int i = 1; i <= n; ++i) {
            for (int j = i - 1; j > 0; --j) {
                int step = nums[i - 1] - nums[j - 1];
                dp[i][step] = std::max(dp[i][step], std::max(dp[j][step], 1) + 1);
            }
        }
        int output = 0;
        for (std::unordered_map<int, int> &chunk : dp) {
            for (auto p : chunk) output = std::max(output, p.second);
        }
        return output;
    }
};