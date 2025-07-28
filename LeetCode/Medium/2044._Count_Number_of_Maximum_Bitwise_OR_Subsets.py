# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
#
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.
#
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
#
#
#
# Example 1:
#
# Input: nums = [3,1]
# Output: 2
# Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
# - [3]
# - [3,1]
# Example 2:
#
# Input: nums = [2,2,2]
# Output: 7
# Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
# Example 3:
#
# Input: nums = [3,2,1,5]
# Output: 6
# Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
# - [3,5]
# - [3,1,5]
# - [3,2,5]
# - [3,2,1,5]
# - [2,5]
# - [2,1,5]
#
#
# Constraints:
#
# 1 <= nums.length <= 16
# 1 <= nums[i] <= 105
# Solution Backtrack Bit Manipulation
# Python O(2**N) O(2**N)
class Solution:
    def backtrack(self, nums: list[int], group_xor: int, result: list[int], target: int, length: int, start: int) -> None:
        if group_xor == target:
            result[0] += 1
        if length == len(nums):
            return
        for idx in range(start, len(nums)):
            self.backtrack(nums, group_xor | nums[idx], result, target, length + 1, idx + 1)
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        bound: int = 0
        for i in range(len(nums)):
            bound |= nums[i]
        answer: list[int] = [0]
        self.backtrack(nums, 0, answer, bound, 0, 0)
        return answer[0]

# C++ O(2**N) O(2**N) Bit Manipulation BackTrack
class Solution {
public:
    void backtrack(std::vector<int>& nums, int current_or, int target, std::vector<int>& answer, int length, int start) {
        if (current_or == target) {
            ++answer[0];
        }
        if (length == nums.size()) {
            return;
        }
        for (int idx = start; idx < nums.size(); ++idx) {
            backtrack(nums, current_or | nums[idx], target, answer, length + 1, idx + 1);
        }
    }
    int countMaxOrSubsets(vector<int>& nums) {
        std::vector<int> answer = {0};
        int target = 0;
        for (int num : nums) {
            target = target | num;
        }
        backtrack(nums, 0, target, answer, 0, 0);
        return answer[0];
    }
};


# Python O((2^N)N) O(1) BitMask
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or: int = 0
        for num in nums: max_or |= num
        output: int = 0
        n: int = len(nums)
        for mask in range(0, 1 << n):
            or_: int = 0
            for j in range(n):
                if mask & (1 << j): or_ |= nums[j]
            if or_ == max_or: output += 1
        return output

# C++ O((2^N)N) O(1) BitMask
class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int maxOr = 0;
        for (int &num : nums) maxOr |= num;
        int n = nums.size(), output = 0;
        for (int mask = 0; mask < (1 << n); ++mask) {
            int or_ = 0;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) or_ |= nums[i];
            }
            if (or_ == maxOr) ++output;
        }
        return output;
    }
};