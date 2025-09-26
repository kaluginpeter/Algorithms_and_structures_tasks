# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
#
#
#
# Example 1:
#
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Example 2:
#
# Input: nums = [4,2,3,4]
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# Solution
# Python O(N^2logN) O(1) BinarySearch Sorting
class Solution:
    def get_k(self, nums: list[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if nums[middle] >= target: right = middle - 1
            else: left = middle + 1
        return right

    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        output: int = 0
        n: int = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                target: int = nums[i] + nums[j]
                k: int = self.get_k(nums, target)
                if k > j: output += k - j
        return output

# C++ O(N^2logN) O(1) Sorting BinarySearch
class Solution {
public:
    int getK(std::vector<int>& nums, int& target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (nums[middle] >= target) right = middle - 1;
            else left = middle + 1;
        }
        return right;
    }
    int triangleNumber(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        size_t n = nums.size();
        int output = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int target = nums[i] + nums[j];
                int k = getK(nums, target);
                if (k > j) output += k - j;
            }
        }
        return output;
    }
};