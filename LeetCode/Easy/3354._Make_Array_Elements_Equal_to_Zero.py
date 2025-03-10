# You are given an integer array nums.
#
# Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.
#
# After that, you repeat the following process:
#
# If curr is out of the range [0, n - 1], this process ends.
# If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
# Else if nums[curr] > 0:
# Decrement nums[curr] by 1.
# Reverse your movement direction (left becomes right and vice versa).
# Take a step in your new direction.
# A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.
#
# Return the number of possible valid selections.
#
#
#
# Example 1:
#
# Input: nums = [1,0,2,0,3]
#
# Output: 2
#
# Explanation:
#
# The only possible valid selections are the following:
#
# Choose curr = 3, and a movement direction to the left.
# [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,0].
# Choose curr = 3, and a movement direction to the right.
# [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0].
# Example 2:
#
# Input: nums = [2,3,4,0,4,1,0]
#
# Output: 0
#
# Explanation:
#
# There are no possible valid selections.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# There is at least one element i where nums[i] == 0.
# Solution
# Python O(N) O(N) Prefix Suffix
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefix: list[int] = []
        for idx in range(len(nums)):
            if not idx:
                prefix.append(nums[idx])
            else:
                prefix.append(nums[idx] + prefix[-1])
        positions: int = 0
        for idx in range(len(nums)):
            if not nums[idx]:
                prefix_sum: int = prefix[idx]
                suffix_sum: int = prefix[-1] - prefix[idx]
                if prefix_sum == suffix_sum:
                    positions += 2
                elif abs(prefix_sum - suffix_sum) == 1:
                    positions += 1
        return positions

# C++ O(N) O(N) Prefix Suffix
class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        std::vector<int> prefix;
        int n = nums.size();
        for (int index = 0; index < n; ++index) {
            if (!index) {
                prefix.push_back(nums[index]);
            } else {
                prefix.push_back(nums[index] + prefix[prefix.size() - 1]);
            }
        }
        int positions = 0;
        for (int index = 0; index < n; ++index) {
            if (!nums[index]) {
                int prefixSum = prefix[index];
                int suffixSum = prefix[n - 1] - prefix[index];
                if (prefixSum == suffixSum) {
                    positions += 2;
                } else if (std::abs(prefixSum - suffixSum) == 1) {
                    ++positions;
                }
            }
        }
        return positions;
    }
};