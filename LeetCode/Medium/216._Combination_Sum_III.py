# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
#
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
#
#
#
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# Example 3:
#
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
#
#
# Constraints:
#
# 2 <= k <= 9
# 1 <= n <= 60
# Solution
# Python O(2^N * k) O(k) Backtracking
class Solution:
    def backtrack(self, number: int, subset: list[int], subset_sum: int, bound: int, target: int, output: list[list[int]]) -> None:
        if len(subset) == bound:
            if subset_sum == target: output.append(subset.copy())
            return
        if number > 9: return # can't take interger '> 9'
        # take
        subset_sum += number
        subset.append(number)
        if subset_sum <= target: self.backtrack(number + 1, subset, subset_sum, bound, target, output)
        subset_sum -= number
        subset.pop()
        # not take
        self.backtrack(number + 1, subset, subset_sum, bound, target, output)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output: list[list[int]] = []
        subset: list[int] = []
        subset_sum: int = 0
        self.backtrack(1, subset, subset_sum, k, n, output)
        return output

# C++ O(2^N * k) O(k) Backtracking
class Solution {
public:
    void backtrack(int number, std::vector<int> &subset, int subsetSum, int k, int n, std::vector<std::vector<int>> &output) {
        if (subset.size() == k) {
            if (subsetSum == n) output.push_back(subset);
            return;
        }
        if (number > 9) return;
        subset.push_back(number);
        subsetSum += number;
        if (subsetSum <= n) backtrack(number + 1, subset, subsetSum, k, n, output);
        subset.pop_back();
        subsetSum -= number;
        backtrack(number + 1, subset, subsetSum, k, n, output);
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        std::vector<std::vector<int>> output;
        std::vector<int> subset;
        backtrack(1, subset, 0, k, n, output);
        return output;
    }
};