# You are given an integer array nums.
#
# You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:
#
# All elements in the subarray are unique.
# The sum of the elements in the subarray is maximized.
# Return the maximum sum of such a subarray.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5]
#
# Output: 15
#
# Explanation:
#
# Select the entire array without deleting any element to obtain the maximum sum.
#
# Example 2:
#
# Input: nums = [1,1,0,1,1]
#
# Output: 1
#
# Explanation:
#
# Delete the element nums[0] == 1, nums[1] == 1, nums[2] == 0, and nums[3] == 1. Select the entire array [1] to obtain the maximum sum.
#
# Example 3:
#
# Input: nums = [1,2,-1,-2,1,0,-1]
#
# Output: 3
#
# Explanation:
#
# Delete the elements nums[2] == -1 and nums[3] == -2, and select the subarray [2, 1] from [1, 2, 1, 0, -1] to obtain the maximum sum.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100
# Solution
# Python O(N) O(N) Sets Greedy
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        x: list[int] = [num for num in nums if num >= 0]
        if not x: return max(nums)
        return sum(set(x))

# C++ O(N) O(N) Sets Greedy
class Solution {
public:
    int maxSum(vector<int>& nums) {
        int n = nums.size();
        int negative = 0;
        for (int& num : nums) {
            if (num < 0) ++negative;
        }
        if (negative == n) return *max_element(nums.begin(), nums.end());
        unordered_set<int> seen;
        int output = 0;
        for (int& num : nums) {
            if (num > 0 && !seen.count(num)) {
                seen.insert(num);
                output += num;
            }
        }
        return output;
    }
};