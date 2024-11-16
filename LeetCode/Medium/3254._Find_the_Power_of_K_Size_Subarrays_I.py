# You are given an array of integers nums of length n and a positive integer k.
#
# The power of an array is defined as:
#
# Its maximum element if all of its elements are consecutive and sorted in ascending order.
# -1 otherwise.
# You need to find the power of all
# subarrays
#  of nums of size k.
#
# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,3,2,5], k = 3
#
# Output: [3,4,-1,-1,-1]
#
# Explanation:
#
# There are 5 subarrays of nums of size 3:
#
# [1, 2, 3] with the maximum element 3.
# [2, 3, 4] with the maximum element 4.
# [3, 4, 3] whose elements are not consecutive.
# [4, 3, 2] whose elements are not sorted.
# [3, 2, 5] whose elements are not consecutive.
# Example 2:
#
# Input: nums = [2,2,2,2,2], k = 4
#
# Output: [-1,-1]
#
# Example 3:
#
# Input: nums = [3,2,3,2,3,2], k = 2
#
# Output: [-1,3,-1,3,-1]
#
#
#
# Constraints:
#
# 1 <= n == nums.length <= 500
# 1 <= nums[i] <= 105
# 1 <= k <= n
# Solution Sliding Window O(N) O(N)
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        result: list[int] = []
        left: int = 0
        right: int = 1
        while left <= len(nums) - k and right < len(nums):
            if nums[right] - 1 == nums[right - 1]:
                if right - left + 1 == k:
                    result.append(nums[right])
                    left += 1
            else:
                while left < right and left <= len(nums) - k:
                    result.append(-1)
                    left += 1
            right += 1
        return result

# C++ O(N) O(N) Sliging Window
class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        if (k == 1) {
            return nums;
        }
        std::vector<int> output;
        int left = 0;
        int right = 1;
        int n = nums.size();
        while (left <= n - k && right < n) {
            if (nums[right] - 1 == nums[right - 1]) {
                if (right - left + 1 == k) {
                    output.push_back(nums[right]);
                    ++left;
                }
            } else {
                while (left < right && left <= n - k) {
                    output.push_back(-1);
                    ++left;
                }
            }
            ++right;
        }
        return output;
    }
};

# Python O(N) O(N) Monotonic Stack
from collections import deque
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        output: list[int] = []
        stack: list[int] = deque()
        for idx in range(k - 1):
            while stack and stack[-1] + 1 != nums[idx]:
                stack.popleft()
            stack.append(nums[idx])
        n: int = len(nums)
        for right in range(k - 1, n):
            while stack and stack[-1] + 1 != nums[right]:
                stack.popleft()
            stack.append(nums[right])
            if len(stack) == k:
                output.append(stack[-1])
                stack.popleft()
            else:
                output.append(-1)
        return output

# C++ O(N) O(N) Monotonic Stack
class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        std::vector<int> output;
        std::deque<int> stack;
        for (int index = 0; index < k - 1; ++index) {
            while (stack.size() && stack.back() + 1 != nums[index]) {
                stack.pop_front();
            }
            stack.push_back(nums[index]);
        }
        int n = nums.size();
        for (int right = k - 1; right < n; ++right) {
            while (stack.size() && stack.back() + 1 != nums[right]) {
                stack.pop_front();
            }
            stack.push_back(nums[right]);
            if (stack.size() == k) {
                output.push_back(nums[right]);
                stack.pop_front();
            } else {
                output.push_back(-1);
            }
        }
        return output;
    }
};