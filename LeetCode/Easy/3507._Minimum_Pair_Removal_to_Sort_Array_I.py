# Given an array nums, you can perform the following operation any number of times:
#
# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.
#
# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).
#
#
#
# Example 1:
#
# Input: nums = [5,2,3,1]
#
# Output: 2
#
# Explanation:
#
# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.
#
# Example 2:
#
# Input: nums = [1,2,2]
#
# Output: 0
#
# Explanation:
#
# The array nums is already sorted.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 50
# -1000 <= nums[i] <= 1000
# Solution
# Python O(N^2) O(1) BruteForce
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations: int = 0
        n: int = len(nums)
        while not all(nums[i] <= nums[i + 1] for i in range(n - 1)):
            start: int = 0
            for i in range(1, n - 1):
                if nums[start] + nums[start + 1] > nums[i] + nums[i + 1]:
                    start = i
            nums[start] += nums.pop(start + 1)
            operations += 1
            n -= 1
        return operations

# C++ O(N^2) O(1) BruteForce
class Solution {
public:
    bool valid(vector<int>& nums) {
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] > nums[i + 1]) return false;
        }
        return true;
    };

    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size(), operations = 0;
        while (!valid(nums)) {
            int start = 0;
            for (int i = 1; i < n - 1; ++i) {
                if (nums[start] + nums[start + 1] > nums[i] + nums[i + 1]) start = i;
            }
            nums[start] += nums[start + 1];
            nums.erase(nums.begin() + start + 1);
            --n;
            ++operations;
        }
        return operations;
    }
};