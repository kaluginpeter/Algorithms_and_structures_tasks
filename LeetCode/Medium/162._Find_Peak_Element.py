# A peak element is an element that is strictly greater than its neighbors.
#
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
#
# You must write an algorithm that runs in O(log n) time.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.
# Solution
# Python O(logN) O(1) BinarySearch
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            l: int = nums[middle - 1] if middle else nums[middle] - 1
            r: int = nums[middle + 1] if middle + 1 < len(nums) else nums[middle] - 1
            if nums[middle] > l: left = middle + 1
            else: right = middle - 1
        return right

# C++ O(logN) O(1) BinarySearch
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            long long l = (middle ? nums[middle - 1] : nums[middle] - 1LL);
            long long r = (middle + 1 < nums.size() ? nums[middle + 1] : nums[middle] - 1LL);
            if (nums[middle] > l) left = middle + 1;
            else right = middle - 1;
        }
        return right;
    }
};