# You are given an integer array nums and a positive integer k.
# A subsequence sub of nums with length x is called valid if it satisfies:
#
# (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
# Return the length of the longest valid subsequence of nums.
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5], k = 2
#
# Output: 5
#
# Explanation:
#
# The longest valid subsequence is [1, 2, 3, 4, 5].
#
# Example 2:
#
# Input: nums = [1,4,2,3,1,4], k = 3
#
# Output: 4
#
# Explanation:
#
# The longest valid subsequence is [1, 4, 1, 4].
#
#
#
# Constraints:
#
# 2 <= nums.length <= 103
# 1 <= nums[i] <= 107
# 1 <= k <= 103
# Solution
# Python O(NK) O(NK) DynamicProgramming
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        dp: list[list[int]] = [[0] * k for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i - 1, 0, -1):
                remainder: int = (nums[i - 1] + nums[j - 1]) % k
                dp[i][remainder] = max(dp[i][remainder], max(dp[j][remainder], 1) + 1)
        return max(max(chunk) for chunk in dp)

# C++ O(NK) O(NK) DynamicProgramming
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        int n = nums.size();
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(k, 0));
        for (int i = 1; i <= n; ++i) {
            for (int j = i - 1; j > 0; --j) {
                int remainder = (nums[i - 1] + nums[j - 1]) % k;
                dp[i][remainder] = std::max(dp[i][remainder], std::max(1, dp[j][remainder]) + 1);
            }
        }
        int output = 0;
        for (std::vector<int> &state : dp) output = std::max(output, *std::max_element(state.begin(), state.end()));
        return output;
    }
};