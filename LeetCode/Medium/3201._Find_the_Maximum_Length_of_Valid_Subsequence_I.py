# 3201. Find the Maximum Length of Valid Subsequence I
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums.
# A subsequence sub of nums with length x is called valid if it satisfies:
#
# (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
# Return the length of the longest valid subsequence of nums.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
#
# Output: 4
#
# Explanation:
#
# The longest valid subsequence is [1, 2, 3, 4].
#
# Example 2:
#
# Input: nums = [1,2,1,1,2,1,2]
#
# Output: 6
#
# Explanation:
#
# The longest valid subsequence is [1, 2, 1, 2, 1, 2].
#
# Example 3:
#
# Input: nums = [1,3]
#
# Output: 2
#
# Explanation:
#
# The longest valid subsequence is [1, 3].
#
#
#
# Constraints:
#
# 2 <= nums.length <= 2 * 105
# 1 <= nums[i] <= 107
# Solution
# Python O(N) O(1) Greedy
class Solution:
    def simulate(self, nums: list[int], has_even: bool, is_diff: bool) -> int:
        output: int = 0
        for num in nums:
            if has_even and not (num & 1):
                if is_diff: has_even = not has_even
                output += 1
            elif not has_even and num & 1:
                if is_diff: has_even = not has_even
                output += 1
        return output

    def maximumLength(self, nums: List[int]) -> int:
        first: int = max(self.simulate(nums, False, True), self.simulate(nums, True, True))
        second: int = max(self.simulate(nums, False, False), self.simulate(nums, True, False))
        return max(first, second)

# C++ O(N) O(1) Greedy
class Solution {
public:
    int simulate(std::vector<int> &nums, bool needEven, bool isDiff) {
        int output = 0;
        for (int &num : nums) {
            if (needEven && !(num & 1)) {
                if (isDiff) needEven = !needEven;
                ++output;
            } else if (!needEven && (num & 1)) {
                if (isDiff) needEven = !needEven;
                ++output;
            }
        }
        return output;
    }

    int maximumLength(vector<int>& nums) {
        // 1st case, start with odd
        // even + odd, odd + even
        int first = std::max(simulate(nums, false, true), simulate(nums, true, true));
        // 2nd case, start with even
        // even + even, odd + odd
        int second = std::max(simulate(nums, false, false), simulate(nums, true, false));
        return std::max(first, second);
    }
};