# Given an array nums sorted in non-decreasing order, return the maximum between
# the number of positive integers and the number of negative integers.
# In other words, if the number of positive integers in nums is pos
# and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.
#
# Example 1:
#
# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 2:
#
# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 3:
#
# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
#
# Constraints:
# 1 <= nums.length <= 2000
# -2000 <= nums[i] <= 2000
# nums is sorted in a non-decreasing order.
# Follow up: Can you solve the problem in O(log(n)) time complexity?
# Solution
# Python O(N) O(1) Greedy
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(sum(1 for i in nums if i < 0), sum(1 for i in nums if i > 0))

# Python O(logN) O(1) Binary Search
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n: int = len(nums)
        left: int = 0
        right: int = n - 1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if nums[middle] >= 0: right = middle - 1
            else: left = middle + 1
        negative: int = left
        left = 0
        right = n - 1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if nums[middle] <= 0: left = middle + 1
            else: right = middle - 1
        positive: int = n - right - 1
        return max(negative, positive)

# C++ O(logN) O(1) Binary Search
class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int n = nums.size();
        int left = 0;
        int right = n - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (nums[middle] >= 0) right = middle - 1;
            else left = middle + 1;
        }
        int negative = left;
        left = 0;
        right = n - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (nums[middle] <= 0) left = middle + 1;
            else right = middle - 1;
        }
        int positive = n - right - 1;
        return std::max(negative, positive);
    }
};