# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
# Constraints:
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
# Solution
# Python O(N**2 * N!) O(N**2 * N!) Hashing Backtracking
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations: list[list[int]] = [[]]
        hashset: set[tuple[int]] = set()
        for num in nums:
            next_permutations: list[list[int]] = []
            for permutation in permutations:
                for position in range(len(permutation) + 1):
                    new_permutation: list[int] = permutation.copy()
                    new_permutation.insert(position, num)
                    if tuple(new_permutation) not in hashset:
                        hashset.add(tuple(new_permutation))
                        next_permutations.append(new_permutation)
            permutations = next_permutations
            hashset.clear()
        return permutations

# C++ O(N**2 * N!) O(N**2 * N!) Hashing Backtracking
struct VectorHash {
    std::size_t operator()(const std::vector<int>& vec) const {
        std::size_t seed = vec.size();
        for (const auto& i : vec) {
            seed ^= i + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        }
        return seed;
    }
};

struct VectorEqual {
    bool operator()(const std::vector<int>& lhs, const std::vector<int>& rhs) const {
        return lhs == rhs;
    }
};

class Solution {
public:
    std::vector<std::vector<int>> uniquePermutations(std::vector<std::vector<int>>& permutations) {
        std::vector<std::vector<int>> outputPermutations;
        std::unordered_set<std::vector<int>, VectorHash, VectorEqual> hashset;
        for (std::vector<int>& permutation : permutations) {
            if (!hashset.count(permutation)) {
                hashset.insert(permutation);
                outputPermutations.push_back(permutation);
            }
        }
        return outputPermutations;
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
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
        return uniquePermutations(permutations);
    }
};

# Python O(N**2 * N!) O(N**2 * N!) Tricky Backtracking
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations: list[list[int]] = [[]]
        for num in nums:
            next_permutations: list[list[int]] = []
            for permutation in permutations:
                for position in range(len(permutation) + 1):
                    new_permutation: list[int] = permutation.copy()
                    new_permutation.insert(position, num)
                    next_permutations.append(new_permutation)
                    if position < len(permutation) and permutation[position] == num:
                        break
            permutations = next_permutations
        return permutations

# C++ O(N**2 * N!) O(N**2 * N!) Tricky Backtracking
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        std::vector<std::vector<int>> permutations = {{}};
        for (int num : nums) {
            std::vector<std::vector<int>> nextPermutations;
            for (std::vector<int>& permutation : permutations) {
                for (int position = 0; position < permutation.size() + 1; ++position) {
                    std::vector<int> newPermutation(permutation);
                    newPermutation.insert(newPermutation.begin() + position, num);
                    nextPermutations.push_back(newPermutation);
                    if (position < permutation.size() && permutation[position] == num) {
                        break;
                    }
                }
            }
            permutations = nextPermutations;
        }
        return permutations;
    }
};