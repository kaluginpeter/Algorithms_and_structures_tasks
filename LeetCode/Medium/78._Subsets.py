# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# Solution
# Python O(N * 2**N) O(N * 2**N) Backtracking
class Solution:
    def helper(self, idx: int, nums: list[list[int]], init: list[int], output: list[list[int]]) -> None:
        if idx == len(nums):
            output.append(init.copy())
            return
        init.append(nums[idx])
        self.helper(idx + 1, nums, init, output)
        init.pop()
        self.helper(idx + 1, nums, init, output)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        output: list[list[int]] = []
        init: list[int] = []
        self.helper(0, nums, init, output)
        return output

# C++ O(N * 2**N) O(N * 2**N) Backtracking
class Solution {
public:
    void helper(int index, std::vector<int>& nums, std::vector<int>& init, std::vector<std::vector<int>>& output) {
        if (index == nums.size()) {
            output.push_back(std::vector<int>(init));
            return;
        }
        init.push_back(nums[index]);
        helper(index + 1, nums, init, output);
        init.pop_back();
        helper(index + 1, nums, init, output);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        std::vector<std::vector<int>> output;
        std::vector<int> init;
        helper(0, nums, init, output);
        return output;
    }
};