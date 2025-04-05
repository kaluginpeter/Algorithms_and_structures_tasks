# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
#
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums.
#
# Note: Subsets with the same elements should be counted multiple times.
#
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
#
#
#
# Example 1:
#
# Input: nums = [1,3]
# Output: 6
# Explanation: The 4 subsets of [1,3] are:
# - The empty subset has an XOR total of 0.
# - [1] has an XOR total of 1.
# - [3] has an XOR total of 3.
# - [1,3] has an XOR total of 1 XOR 3 = 2.
# 0 + 1 + 3 + 2 = 6
# Example 2:
#
# Input: nums = [5,1,6]
# Output: 28
# Explanation: The 8 subsets of [5,1,6] are:
# - The empty subset has an XOR total of 0.
# - [5] has an XOR total of 5.
# - [1] has an XOR total of 1.
# - [6] has an XOR total of 6.
# - [5,1] has an XOR total of 5 XOR 1 = 4.
# - [5,6] has an XOR total of 5 XOR 6 = 3.
# - [1,6] has an XOR total of 1 XOR 6 = 7.
# - [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
# 0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
# Example 3:
#
# Input: nums = [3,4,5,6,7,8]
# Output: 480
# Explanation: The sum of all XOR totals for every subset is 480.
#
#
# Constraints:
#
# 1 <= nums.length <= 12
# 1 <= nums[i] <= 20
# Solution Combinatoric O(2^N) O(N)
class Solution:
    from itertools import combinations
    def subsetXORSum(self, nums: List[int]) -> int:
        total: int = 0
        for i in range(len(nums) + 1):
            for subset in combinations(nums, i):
                xor: int = 0
                for num in subset:
                    xor ^= num
                total += xor
        return total


# Python O(2^N) O(N) Backtracking Combinations Bit Manipulations
class Solution:
    score: int = 0
    def backtrack(self, idx: int, nums: list[int], cur_sum: int) -> None:
        if idx == len(nums): return
        for next_idx in range(idx, len(nums)):
            next_sum: int = cur_sum ^ nums[next_idx]
            self.score += next_sum
            self.backtrack(next_idx + 1, nums, next_sum)

    def subsetXORSum(self, nums: List[int]) -> int:
        self.score = 0
        self.backtrack(0, nums, 0)
        return self.score

# C++ O(2^N) O(N) Backtracking Combinations BitManipulations
class Solution {
public:
    void backtrack(int idx, vector<int>& nums, int curSum, int& score) {
        if (idx == nums.size()) return;
        for (int nextIdx = idx; nextIdx < nums.size(); ++nextIdx) {
            int nextSum = curSum ^ nums[nextIdx];
            score += nextSum;
            backtrack(nextIdx + 1, nums, nextSum, score);
        }
    }
    int subsetXORSum(vector<int>& nums) {
        int score = 0;
        backtrack(0, nums, 0, score);
        return score;
    }
};

# Python O(N) O(1) BitMasking Math BitManipulations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        score: int = 0
        for num in nums: score |= num
        return score << (len(nums) - 1)

# C++ O(N) O(1) BitMasking Math BitManipulations
class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int score = 0;
        for (int &num : nums) score |= num;
        return score << (nums.size() - 1);
    }
};