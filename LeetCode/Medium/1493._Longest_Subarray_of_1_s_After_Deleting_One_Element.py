# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
#
#
#
# Example 1:
#
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:
#
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:
#
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# Solution Sliding Window O(N) O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros: int = 0
        left: int = 0
        right: int = 0
        mx_length: int = 0
        for right in range(len(nums)):
            if nums[right] == 0: zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            mx_length = max(mx_length, right - left)
        return mx_length


# Python O(N) O(1) TwoPointers
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        output: int = 0
        left: int = 0
        skipped: int = 0
        for right in range(len(nums)):
            if not nums[right]: skipped += 1
            while skipped > 1:
                if not nums[left]: skipped -= 1
                left += 1
            if right - left > output: output = right - left
        return output

# C++ O(N) O(1) TwoPointers
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        size_t output = 0, left = 0, deleted = 0;
        for (size_t right = 0; right < nums.size(); ++right) {
            if (!nums[right]) ++deleted;
            while (deleted > 1) {
                if (!nums[left]) --deleted;
                ++left;
            }
            if (right - left > output) output = right - left;
        }
        return output;
    }
};