# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
#
#
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
#
# Constraints:
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# Solution BackTracking O(2**N) O(2**N)
class Solution:
    global_combs: list[list[int, ...], ...] = None

    def find_comb(
        self, candidates: list[int], target: int, cur_sum: int, cur_comb: list[int, ...], idx: int
    ) -> None:
        prev: int = -1

        for pointer in range(idx, len(candidates)):
            if cur_sum + candidates[pointer] > target: break
            if prev == candidates[pointer]: continue
            cur_comb.append(candidates[pointer])
            self.find_comb(candidates, target, cur_sum + candidates[pointer], cur_comb, pointer + 1)
            cur_comb.pop()
            prev = candidates[pointer]
        if cur_sum == target:
            self.global_combs.append(cur_comb.copy())


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.global_combs = []
        candidates.sort()
        self.find_comb(candidates, target, 0, [], 0)
        return self.global_combs