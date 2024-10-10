# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
#
# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.
#
#
#
# Example 1:
#
# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
# Example 2:
#
# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
#
#
# Constraints:
#
# 2 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 5 * 104
# Solution
# Python O(N) O(N) Monotonic Stack
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack: list[int] = []
        for idx in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[idx]:
                stack.append(idx)
        max_length: int = 0
        for right in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[right]:
                max_length = max(max_length, right - stack.pop())
        return max_length
# C++ O(N) O(N) Monotonic Stack
class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        std::vector<int> stack;
        for (int index = 0; index < nums.size(); ++index) {
            if (!stack.size() || nums[stack[stack.size() - 1]] > nums[index]) {
                stack.push_back(index);
            }
        }
        int max_length = 0;
        for (int right = nums.size() - 1; right >= 0; --right) {
            while (stack.size() && nums[stack[stack.size() - 1]] <= nums[right]) {
                max_length = std::max(max_length, right - stack[stack.size() - 1]);
                stack.pop_back();
            }
        }
        return max_length;
    }
};
# Python O(N) O(N) Two Pointers
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        right_idxs: list[int] = [0] * len(nums)
        right_idxs[len(nums) - 1] = nums[len(nums) - 1]
        for idx in range(len(nums) - 2, -1, -1):
            right_idxs[idx] = max(nums[idx], right_idxs[idx + 1])
        left: int = 0
        right: int = 0
        max_length: int = 0
        while right < len(right_idxs):
            while left < right and nums[left] > right_idxs[right]:
                left += 1
            max_length = max(max_length, right - left)
            right += 1
        return max_length
# C++ O(N) O(N) Two Pointers
class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> right_idxs(n, 0);
        right_idxs[n - 1] = nums[n - 1];
        for (int index = n - 2; index >= 0; --index) {
            right_idxs[index] = std::max(right_idxs[index + 1], nums[index]);
        }
        int left = 0, right = 0;
        int max_length = 0;
        while (right < n) {
            while (left < right && nums[left] > right_idxs[right]) {
                ++left;
            }
            max_length = std::max(max_length, right - left);
            ++right;
        }
        return max_length;
    }
};