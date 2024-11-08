# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
#  of at least one of the chosen numbers is different.
#
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
#
#
#
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:
#
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:
#
# Input: candidates = [2], target = 1
# Output: []
#
#
# Constraints:
#
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
# Solution
# Python O(N * C(N, N)) O(N * C(N, N)) Backtracking
class Solution:
    def helper(self, idx: int, cur_sum: int, candidates: list[int], target: int, init: list[int], output: list[list[int]]) -> None:
        if cur_sum == target:
            output.append(init.copy())
            return
        if idx == len(candidates) or cur_sum > target:
            return
        for next_idx in range(idx, len(candidates)):
            init.append(candidates[next_idx])
            self.helper(next_idx, cur_sum + candidates[next_idx], candidates, target, init, output)
            init.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output: list[list[int]] = []
        init: list[int] = []
        self.helper(0, 0, candidates, target, init, output)
        return output

# C++ O(N * C(N, N)) O(N * C(N, N)) Backtracking
class Solution {
public:
    void helper(
        int index, int curSum,
        std::vector<int>& candidates,
        int target,
        std::vector<int>& init,
        std::vector<std::vector<int>>& output
    ) {
        if (curSum == target) {
            output.push_back(init);
            return;
        }
        if (curSum > target || index >= candidates.size()) {
            return;
        }
        for (int nextIndex = index; nextIndex < candidates.size(); ++nextIndex) {
            init.push_back(candidates[nextIndex]);
            helper(nextIndex, curSum + candidates[nextIndex], candidates, target, init, output);
            init.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        std::vector<std::vector<int>> output;
        std::vector<int> init;
        helper(0, 0, candidates, target, init, output);
        return output;
    }
};