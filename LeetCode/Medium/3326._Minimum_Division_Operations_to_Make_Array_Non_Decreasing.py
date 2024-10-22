# You are given an integer array nums.
#
# Any positive divisor of a natural number x that is strictly less than x is called a proper divisor of x. For example, 2 is a proper divisor of 4, while 6 is not a proper divisor of 6.
#
# You are allowed to perform an operation any number of times on nums, where in each operation you select any one element from nums and divide it by its greatest proper divisor.
#
# Return the minimum number of operations required to make the array non-decreasing.
#
# If it is not possible to make the array non-decreasing using any number of operations, return -1.
#
#
#
# Example 1:
#
# Input: nums = [25,7]
#
# Output: 1
#
# Explanation:
#
# Using a single operation, 25 gets divided by 5 and nums becomes [5, 7].
#
# Example 2:
#
# Input: nums = [7,7,6]
#
# Output: -1
#
# Example 3:
#
# Input: nums = [1,1,1,1]
#
# Output: 0
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# Solution
# Python O(Nsqrt(M)) O(1) Math Greedy Number Theory
class Solution:
    def max_proper_divisor(self, x: int) -> int:
        if x <= 2:
            return -1
        largest_proper_divisor: int = -1
        for d in range(2, int(x**0.5) + 1):
            if x % d == 0:
                if d < x:
                    largest_proper_divisor = max(largest_proper_divisor, d)
                if x // d < x:
                    largest_proper_divisor = max(largest_proper_divisor, x // d)
        return largest_proper_divisor

    def minOperations(self, nums: List[int]) -> int:
        count: int = 0
        for idx in range(len(nums) - 1, 0, -1):
            while nums[idx - 1] > nums[idx]:
                divisor: int = self.max_proper_divisor(nums[idx - 1])
                if divisor == -1:
                    return -1
                nums[idx - 1] = nums[idx - 1] // divisor
                count += 1
        return count

# C++ O(Nsqrt(M)) O(1) Math Number Theory Greedy
class Solution {
public:
    int maxProperDivisor(int x) {
        if (x <= 2) {
            return -1;
        }
        int largestProperDivisor = -1;
        for (int divisor = 2; divisor < std::sqrt(x) + 1; ++divisor) {
            if (x % divisor == 0) {
                if (divisor < x) {
                    largestProperDivisor = std::max(largestProperDivisor, divisor);
                }
                if (x / divisor < x) {
                    largestProperDivisor = std::max(largestProperDivisor, x / divisor);
                }
            }
        }
        return largestProperDivisor;
    }

    int minOperations(vector<int>& nums) {
        int operations = 0;
        for (int index = nums.size() - 1; index > 0; --index) {
            while (nums[index - 1] > nums[index]) {
                int divisor = maxProperDivisor(nums[index - 1]);
                if (divisor == -1) {
                    return -1;
                }
                nums[index - 1] = nums[index - 1] / divisor;
                ++operations;
            }
        }
        return operations;
    }
};