# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
#
# A pair (i, j) is fair if:
#
# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper
#
#
# Example 1:
#
# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
# Example 2:
#
# Input: nums = [1,7,9,2,5], lower = 11, upper = 11
# Output: 1
# Explanation: There is a single fair pair: (2,3).
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums.length == n
# -109 <= nums[i] <= 109
# -109 <= lower <= upper <= 109
# Solution
# Python O(NlogN) O(1) BinarySearch
class Solution:
    def binary_search(self, nums: list[int], left: int, right: int, target: int) -> int:
        while left <= right:
            middle: int = left + (right - left) // 2
            if nums[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1
        return right + 1

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        output: int = 0
        for idx in range(len(nums)):
            left: int = self.binary_search(nums, idx + 1, len(nums) - 1, lower - nums[idx])
            right: itn = self.binary_search(nums, idx + 1, len(nums) - 1, upper - nums[idx] + 1)
            output += right - left
        return output

# C++ O(NlogN) O(1) BinarySearch
class Solution {
public:
    int binarySearch(std::vector<int>& nums, int left, int right, int target) {
        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (nums[middle] >= target) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        return right + 1;
    }
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        std::sort(nums.begin(), nums.end());
        long long output = 0;
        for (int index = 0; index < nums.size(); ++index) {
            int left = binarySearch(nums, index + 1, nums.size() - 1, lower - nums[index]);
            int right = binarySearch(nums, index+ 1, nums.size() - 1, upper - nums[index] + 1);
            output += right - left;
        }
        return output;
    }
};