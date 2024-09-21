# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
#
#
#
# Example 1:
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
#
# Constraints:
#
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
#
#
# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
# Solution
# Python Sliding Window Greedy O(N) O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length: int = float('inf')
        left: int = 0
        current_sum: int = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0

# C++ Sliding Window Greedy O(N) O(1)
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int min_length = 100001;
        int current_sum = 0;
        int left = 0;
        for (int right = 0; right < nums.size(); ++right) {
            current_sum += nums[right];
            while (current_sum >= target) {
                min_length = std::min(min_length, right - left + 1);
                current_sum -= nums[left];
                left += 1;
            }
        }
        return min_length != 100001? min_length : 0;
    }
};