# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
# Constraints:
#
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
# Solution
# Python O(N**2) O(N) Two Pointers Sorting
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output: list[list[int]] = []
        nums.sort()
        for left in range(len(nums)):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            target: int = -nums[left]
            middle: int = left + 1
            right: int = len(nums) - 1
            while middle < right:
                if right != len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue
                if middle - 1 != left and nums[middle] == nums[middle - 1]:
                    middle += 1
                    continue
                current_sum: int = nums[middle] + nums[right]
                if current_sum == target:
                    output.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                elif current_sum < target:
                    middle += 1
                else:
                    right -= 1
        return output

# C++ O(N**2) O(N) Two Pointers Sorting
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::vector<std::vector<int>> output;
        std::sort(nums.begin(), nums.end());
        for (int left = 0; left < nums.size(); ++left) {
            if (left > 0 && nums[left] == nums[left - 1]) {
                continue;
            }
            int target = -nums[left];
            int middle = left + 1;
            int right = nums.size() - 1;
            while (middle < right) {
                if (right != nums.size() - 1 && nums[right] == nums[right + 1]) {
                    --right;
                    continue;
                }
                if (middle - 1 != left && nums[middle] == nums[middle - 1]) {
                    ++middle;
                    continue;
                }
                int current_sum = nums[middle] + nums[right];
                if (current_sum == target) {
                    output.push_back({nums[left], nums[middle], nums[right]});
                    ++middle;
                } else if (current_sum < target) {
                    ++middle;
                } else {
                    --right;
                }
            }
        }
        return output;
    }
};