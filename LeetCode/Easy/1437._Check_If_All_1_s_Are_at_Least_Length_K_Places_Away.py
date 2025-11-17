# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.
#
#
#
# Example 1:
#
#
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.
# Example 2:
#
#
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 0 <= k <= nums.length
# nums[i] is 0 or 1
# Solution
# Python O(N) O(1) TwoPointers
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        left: int = 0
        right: int = 0
        n: int = len(nums)
        while right < n:
            while left < n and not nums[left]: left += 1
            right = left + 1
            while right < n and not nums[right]: right += 1
            if right < n and right - left - 1 < k: return False
            left = right
        return True

# C++ O(N) O(1) TwoPointers
class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        size_t left = 0, right = 0, n = nums.size();
        while (right < n) {
            while (left < n && !nums[left]) ++left;
            right = left + 1;
            while (right < n && !nums[right]) ++right;
            if (right < n && (right - left - 1) < k) return false;
            left = right;
        }
        return true;
    }
};