# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
#
# In one move, you can increment or decrement an element of the array by 1.
#
# Test cases are designed so that the answer will fit in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# Example 2:
#
# Input: nums = [1,10,2,9]
# Output: 16
#
#
# Constraints:
#
# n == nums.length
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# Solution
# Python O(NlogN + N) O(1) Sorting Math
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        output: int = float('inf')
        left: int = 0
        right: int = sum(nums)
        n: int = len(nums)
        for i in range(n):
            prefix: int = i * nums[i] - left
            suffix: int = right - (n - i) * nums[i]
            output = min(output, prefix + suffix)
            left += nums[i]
            right -= nums[i]
        return output

# C++ O(NlogN + N) O(1) Sorting Math
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        size_t n = nums.size();
        long long output = INT64_MAX, left = 0, right = std::accumulate(nums.begin(), nums.end(), 0LL);
        for (size_t i = 0; i < n; ++i) {
            long long prefix = (i * nums[i] - left), suffix = (right - (n - i) * nums[i]);
            output = std::min(output, prefix + suffix);
            right -= nums[i];
            left += nums[i];
        }
        return output;
    }
};