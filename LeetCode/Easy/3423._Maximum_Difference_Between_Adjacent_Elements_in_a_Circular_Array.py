# Given a circular array nums, find the maximum absolute difference between adjacent elements.
#
# Note: In a circular array, the first and last elements are adjacent.
#
#
#
# Example 1:
#
# Input: nums = [1,2,4]
#
# Output: 3
#
# Explanation:
#
# Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.
#
# Example 2:
#
# Input: nums = [-5,-10,-5]
#
# Output: 5
#
# Explanation:
#
# The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.
#
#
#
# Constraints:
#
# 2 <= nums.length <= 100
# -100 <= nums[i] <= 100
# Solution
# Python O(N) O(1) String Greedy
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n: int = len(nums)
        output: int = abs(nums[0] - nums[-1])
        for i in range(n - 1):
            output = max(output, abs(nums[i] - nums[i + 1]))
        return output

# C++ O(N) O(1) String Greedy
class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int n = nums.size(), output = abs(nums[0] - nums[n - 1]);
        for (int i = 0; i < n - 1; ++i) {
            output = max(output, abs(nums[i] - nums[i + 1]));
        }
        return output;
    }
};