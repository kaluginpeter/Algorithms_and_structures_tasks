# You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:
#
# For each index i (where 0 <= i < nums.length), perform the following independent actions:
# If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] == 0: Set result[i] to nums[i].
# Return the new array result.
#
# Note: Since nums is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.
#
#
#
# Example 1:
#
# Input: nums = [3,-2,1,1]
#
# Output: [1,1,1,3]
#
# Explanation:
#
# For nums[0] that is equal to 3, If we move 3 steps to right, we reach nums[3]. So result[0] should be 1.
# For nums[1] that is equal to -2, If we move 2 steps to left, we reach nums[3]. So result[1] should be 1.
# For nums[2] that is equal to 1, If we move 1 step to right, we reach nums[3]. So result[2] should be 1.
# For nums[3] that is equal to 1, If we move 1 step to right, we reach nums[0]. So result[3] should be 3.
# Example 2:
#
# Input: nums = [-1,4,-1]
#
# Output: [-1,-1,4]
#
# Explanation:
#
# For nums[0] that is equal to -1, If we move 1 step to left, we reach nums[2]. So result[0] should be -1.
# For nums[1] that is equal to 4, If we move 4 steps to right, we reach nums[2]. So result[1] should be -1.
# For nums[2] that is equal to -1, If we move 1 step to left, we reach nums[1]. So result[2] should be 4.
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100
# Solution
# Python O(N) O(N) Math
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        output: list[int] = [0] * n
        for i in range(n):
            if nums[i] == 0:
                output[i] = nums[i]
            elif nums[i] > 0:
                output[i] = nums[(nums[i] + i) % n]
            else:
                output[i] = nums[(i - abs(nums[i]) + n) % n]
        return output

# C++ O(N) O(N) Math
class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> output(n, 0);
        for (int idx = 0; idx < n; ++idx) {
            if (!nums[idx]) {
                output[idx] = nums[idx];
            } else if (nums[idx] > 0) {
                output[idx] = nums[(idx + nums[idx]) % n];
            } else {
                output[idx] = nums[(idx - std::abs(nums[idx]) % n + n) % n];
            }
        }
        return output;
    }
};