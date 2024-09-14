# You are given an integer array nums of size n.
#
# Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
#
# In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
# Return the length of the longest such subarray.
#
# The bitwise AND of an array is the bitwise AND of all the numbers in it.
#
# A subarray is a contiguous sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,3,2,2]
# Output: 2
# Explanation:
# The maximum possible bitwise AND of a subarray is 3.
# The longest subarray with that value is [3,3], so we return 2.
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: 1
# Explanation:
# The maximum possible bitwise AND of a subarray is 4.
# The longest subarray with that value is [4], so we return 1.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# Solution Sliding Window
# Python O(N) O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        answer: int = 1 # in constraints minimum length of "nums" is 1
        left: int = 0
        target: int = max(nums)
        for right in range(len(nums)):
            while left <= right and nums[right] != target:
                answer = max(answer, right - left)
                left += 1
            answer = max(answer, right - left + 1)
        return answer
# C++ O(N) O(1)
#include <algorithm>
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int answer = 1; // in constraints minimum length of "nums" is 1
        int target = 0;
        for (int num : nums) {
            target = std::max(target, num);
        }
        int left = 0;
        for (int right = 0; right < nums.size(); ++right){
            while (left <= right && nums[right] != target) {
                answer = std::max(answer, right - left);
                left += 1;
            }
            answer = std::max(answer, right - left + 1);
        }
        return answer;
    }
};