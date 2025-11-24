# You are given a binary array nums (0-indexed).
#
# We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).
#
# For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
# Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
#
#
#
# Example 1:
#
# Input: nums = [0,1,1]
# Output: [true,false,false]
# Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
# Only the first number is divisible by 5, so answer[0] is true.
# Example 2:
#
# Input: nums = [1,1,1]
# Output: [false,false,false]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# Solution
class Solution(object):
    def prefixesDivBy5(self, nums):
        l, top = [True] * len(nums), 0
        for i in range(len(nums)):
            top = top * 2 + nums[i]
            l[i] = top % 5 == 0
        return l


# Python O(N) O(1) BitManipulation
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        output: list[bool] = []
        mod: int = 5
        cur: int = 0
        for i in range(len(nums)):
            cur = ((cur << 1) + nums[i]) % mod
            output.append(cur % 5 == 0)
        return output

# C++ O(N) O(1) BitManipulation
class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        int mod = 5, cur = 0;
        std::vector<bool> output(nums.size(), false);
        for (int i = 0; i < nums.size(); ++i) {
            cur = ((cur << 1) + nums[i]) % mod;
            output[i] = (cur ? cur % 5 == 0 : true);
        }
        return output;
    }
};