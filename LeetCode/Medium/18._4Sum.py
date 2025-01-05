# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#
#
# Constraints:
#
# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Solution
# Python O(N**3) O(N**4) Two Pointers Sorting
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output: list[list[int]] = []
        nums.sort()
        n: int = len(nums)
        for i in range(n):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                first_pair: int = nums[i] + nums[j]
                left: int = j + 1
                right: int = n - 1
                while left < right:
                    second_pair: int = nums[left] + nums[right]
                    cur_sum: int = first_pair + second_pair
                    if cur_sum == target:
                        output.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif cur_sum < target:
                        left += 1
                    else:
                        right -= 1
        return output

# C++ O(N**3) O(N**4) Two Pointers Sorting
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> output;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (i && nums[i - 1] == nums[i]) {
                continue;
            }
            for (int j = i + 1; j < n; ++j) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }
                long long firstPair = nums[i] + nums[j];
                int left = j + 1;
                int right = n - 1;
                while (left < right) {
                    long long secondPair = nums[left] + nums[right];
                    long long curSum = firstPair + secondPair;
                    if (curSum == target) {
                        output.push_back({nums[i], nums[j], nums[left], nums[right]});
                        ++left;
                        --right;
                        while (left < right && nums[left] == nums[left - 1]) {
                            ++left;
                        }
                        while (left < right && nums[right] == nums[right + 1]) {
                            --right;
                        }
                    } else if (curSum < target) {
                        ++left;
                    } else {
                        --right;
                    }
                }
            }
        }
        return output;
    }
};