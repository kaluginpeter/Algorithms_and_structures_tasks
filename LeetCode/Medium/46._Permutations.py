# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# Solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools
        return list(itertools.permutations(nums))

# C++ O(N**2 * N!) O(N**2 * N!) Iterative Backtracking
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        std::vector<std::vector<int>> permutations = {{}};
        for (int num : nums) {
            std::vector<std::vector<int>> nextPermutations;
            for (std::vector<int>& permutation : permutations) {
                for (int position = 0; position < permutation.size() + 1; ++position) {
                    std::vector<int> newPermutation(permutation);
                    newPermutation.insert(newPermutation.begin() + position, num);
                    nextPermutations.push_back(newPermutation);
                }
            }
            permutations = nextPermutations;
        }
        return permutations;
    }
};

# Python O(N**2 * N!) O(N**2 * N!) Iterative Backtracking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: list[list[int]] = [[]]
        for num in nums:
            next_permutations: list[list[int]] = []
            for permutation in permutations:
                for position in range(len(permutation) + 1):
                    new_permutation: list[int] = permutation.copy()
                    new_permutation.insert(position, num)
                    next_permutations.append(new_permutation)
            permutations = next_permutations
        return permutations

# C++ O(N**2 * N!) O(N**2 * N!) Recursive Backtracking
class Solution {
public:
    std::vector<std::vector<int>> backtrack(int index, std::vector<int>& nums) {
        if (index == nums.size() - 1) {
            return {{nums[index]}};
        }
        std::vector<std::vector<int>> permutations = backtrack(index + 1, nums);
        std::vector<std::vector<int>> outputPermutations;
        for (std::vector<int>& permutation : permutations) {
            for (int position = 0; position < permutation.size() + 1; ++position) {
                std::vector<int> newPermutation(permutation);
                newPermutation.insert(newPermutation.begin() + position, nums[index]);
                outputPermutations.push_back(newPermutation);
            }
        }
        return outputPermutations;
    }
    vector<vector<int>> permute(vector<int>& nums) {
        return backtrack(0, nums);
    }
};

# Python O(N**2 * N!) O(N**2 * N!) Recursive Backtracking
class Solution:
    def backtrack(self, idx: int, nums: list[int]) -> list[list[int]]:
        if idx == len(nums) - 1:
            return [[nums[idx]]]
        permutations: list[list[int]] = self.backtrack(idx + 1, nums)
        output_permutations: list[list[int]] = []
        for permutation in permutations:
            for position in range(len(permutation) + 1):
                new_permutation: list[int] = permutation.copy()
                new_permutation.insert(position, nums[idx])
                output_permutations.append(new_permutation)
        return output_permutations

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(0, nums)