# Given an integer array nums that may contain duplicates, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
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
# Solution
# C++ O(N * 2**N) O(N * 2**N) Backtracking Sorting
class Solution {
public:
    void helper(int index, std::vector<int>& nums, std::vector<int>& init, std::vector<std::vector<int>>& output) {
        if (index >= nums.size()) {
            output.push_back(std::vector<int>(init));
            return;
        }
        init.push_back(nums[index]);
        helper(index + 1, nums, init, output);
        init.pop_back();
        while (index + 1 < nums.size() && nums[index] == nums[index + 1]) {
            ++index;
        }
        helper(index + 1, nums, init, output);
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        std::vector<std::vector<int>> output;
        std::sort(nums.begin(), nums.end());
        std::vector<int> init;
        helper(0, nums, init, output);
        return output;
    }
};

# Python O(N * 2**N) O(N * 2**N) Backtracking Sorting
class Solution:
    def helper(self, idx: int, nums: list[int], init: list[int], output: list[list[int]]) -> None:
        if idx >= len(nums):
            output.append(init.copy())
            return
        init.append(nums[idx])
        self.helper(idx + 1, nums, init, output)
        init.pop()
        while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
            idx += 1
        self.helper(idx + 1, nums, init, output)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output: list[list[int]] = []
        init: list[int] = []
        nums.sort()
        self.helper(0, nums, init, output)
        return output