# Given an array nums, return true if the array was originally sorted in non-decreasing order,
# then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same
# length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
#
# Example 1:
#
# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
# Example 2:
#
# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
# Example 3:
#
# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
#
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# Solution
class Solution:
    def check(self, nums: List[int]) -> bool:
        l = sorted(nums)
        for i in range(len(nums)):
            if l == nums: return True
            l = l[1:] + [l[0]]
        return False

# Python O(N) O(1) Greedy
class Solution:
    def check(self, nums: List[int]) -> bool:
        has_break: bool = False
        breaks: int = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                has_break = True
                breaks += 1
                if breaks > 1: return False
        return not breaks or nums[0] >= nums[-1]

# C++ O(N) O(1) Greedy
class Solution:
class Solution {
public:
    bool check(vector<int>& nums) {
        bool hasBreak = false;
        int breaks = 0;
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] > nums[i + 1]) {
                hasBreak = true;
                ++breaks;
                if (breaks > 1) return false;
            }
        }
        return !hasBreak || nums[0] >= nums[nums.size() - 1];
    }
};
