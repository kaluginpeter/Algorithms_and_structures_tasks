# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.
#
# For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
#
# Each element of nums is in exactly one pair, and
# The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.
#
#
#
# Example 1:
#
# Input: nums = [3,5,2,3]
# Output: 7
# Explanation: The elements can be paired up into pairs (3,3) and (5,2).
# The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
# Example 2:
#
# Input: nums = [3,5,4,2,4,6]
# Output: 8
# Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
# The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
#
#
# Constraints:
#
# n == nums.length
# 2 <= n <= 105
# n is even.
# 1 <= nums[i] <= 105
# Solution 1 - Sort and Two Pointers
class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        x, y, top = 0, len(nums) - 1, 0
        while x < y:
            if nums[x] + nums[y] > top:
                top = nums[x] + nums[y]
            x += 1
            y -= 1
        return top
# Solution 2 - Sort and Two Pointers by One Pointer
class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        x, top = 0, 0
        while x < len(nums) / 2:
            top = max(top, nums[x] + nums[-x - 1])
            x += 1
        return top


# Python O(NlogN) O(1) Greedy
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n: int = len(nums)
        return max((nums[i] + nums[n - i - 1] for i in range(n >> 1)), default=0)

# C++ O(NlogN) O(1) Greedy
class Solution {
public:
    int minPairSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        size_t n = nums.size();
        int output = 0;
        for (size_t i = 0; i < n / 2; ++i) {
            output = std::max(output, nums[i] + nums[n - i - 1]);
        }
        return output;
    }
};