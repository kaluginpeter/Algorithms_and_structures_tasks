# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].
# Solution
# Python O(N**2) O(N) DynamicProgramming
class Solution:
    def jump(self, nums: List[int]) -> int:
        n: int = len(nums)
        dp: list[int] = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j >= n: break
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[n - 1]

# C++ O(N**2) O(N) DynamicProgramming
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp (n, INT32_MAX - 10000000);
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 1; j <= nums[i]; ++j) {
                if (i + j >= n) break;
                dp[i + j] = min(dp[i + j], dp[i] + 1);
            }
        }
        return dp[n - 1];
    }
};

# Python O(N) O(1) Greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        n: int = len(nums)
        jumps: int = 0
        cur_end: int = 0
        cur_right: int = 0
        for i in range(n - 1):
            cur_right = max(cur_right, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = cur_right
        return jumps

# C++ O(N) O(1) Greedy
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int jumps = 0;
        int curEnd = 0;
        int curRight = 0;
        for (int i = 0; i < n - 1; ++i) {
            curRight = max(curRight, nums[i] + i);
            if (i == curEnd) {
                ++jumps;
                curEnd = curRight;
            }
        }
        return jumps;
    }
};