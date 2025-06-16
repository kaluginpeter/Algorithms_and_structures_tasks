# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
#
# Return the maximum difference. If no such i and j exists, return -1.
#
#
#
# Example 1:
#
# Input: nums = [7,1,5,4]
# Output: 4
# Explanation:
# The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
# Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
# Example 2:
#
# Input: nums = [9,4,3,2]
# Output: -1
# Explanation:
# There is no i and j such that i < j and nums[i] < nums[j].
# Example 3:
#
# Input: nums = [1,5,2,10]
# Output: 9
# Explanation:
# The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
#
#
# Constraints:
#
# n == nums.length
# 2 <= n <= 1000
# 1 <= nums[i] <= 109
# Solution
# Python O(N) O(1) Greedy Array
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value: int = nums[0]
        max_value: int = nums[0]
        output: int = 0
        for i in range(len(nums)):
            if nums[i] < min_value:
                min_value = max_value = nums[i]
            elif nums[i] > max_value: max_value = nums[i]
            output = max(output, max_value - min_value)
        return output if output else -1

# C++ O(N) O(1) Greedy Array
class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int minValue = nums[0], maxValue = nums[0], output = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] < minValue) {
                minValue = nums[i];
                maxValue = nums[i];
            } else if (nums[i] > maxValue) maxValue = nums[i];
            output = std::max(output, maxValue - minValue);
        }
        return (output ? output : -1);
    }
};