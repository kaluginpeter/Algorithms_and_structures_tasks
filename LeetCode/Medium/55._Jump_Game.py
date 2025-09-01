# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105
# Solution
# Python O(N) O(1) Greedy DynamicProgramming
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n: int = len(nums)
        cur_end: int = 0
        for i in range(n):
            if i > cur_end: return False
            cur_end = max(cur_end, i + nums[i])
        return cur_end >= n - 1

# C++ O(N) O(1) Greedy DynamicProgramming
class Solution {
public:
    bool canJump(vector<int>& nums) {
        size_t n = nums.size(), curEnd = 0;
        for (size_t i = 0; i < n; ++i) {
            if (i > curEnd) return false;
            curEnd = std::max(curEnd, i + nums[i]);
        }
        return curEnd >= n - 1;
    }
};