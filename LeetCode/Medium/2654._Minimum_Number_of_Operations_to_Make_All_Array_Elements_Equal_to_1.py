# You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:
#
# Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
# Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.
#
# The gcd of two integers is the greatest common divisor of the two integers.
#
#
#
# Example 1:
#
# Input: nums = [2,6,3,4]
# Output: 4
# Explanation: We can do the following operations:
# - Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
# - Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
# - Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
# - Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
# Example 2:
#
# Input: nums = [2,10,6,14]
# Output: -1
# Explanation: It can be shown that it is impossible to make all the elements equal to 1.
#
#
# Constraints:
#
# 2 <= nums.length <= 50
# 1 <= nums[i] <= 106
#
# Solution
# Python O(N^2logM) O(1) Math Greedy
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if max(nums) == 1: return 0
        n: int = len(nums)
        output: int = n + n
        ones: int = 0
        is_valid: bool = False
        for i in range(n):
            cur: int = nums[i]
            if cur == 1: ones += 1
            for j in range(i, n):
                cur = gcd(cur, nums[j])
                if cur == 1:
                    output = min(output, max(0, j - i - 1))
                    is_valid = True
                    break
        return (n + output - ones) if is_valid else -1

# C++ O(N^2logM) O(1) Greedy Math
class Solution {
public:
    int minOperations(vector<int>& nums) {
        size_t n = nums.size();
        bool isValid = false;
        int output = INT32_MAX, ones = 0;;
        for (size_t i = 0; i < n; ++i) {
            int cur = nums[i];
            if (cur == 1) ++ones;
            for (size_t j = i; j < n; ++j) {
                cur = std::gcd(cur, nums[j]);
                if (cur == 1) {
                    isValid = true;
                    output = std::min(output, std::max(0, static_cast<int>(j - i - 1)));
                    break;
                }
            }
        }
        if (*std::max_element(nums.begin(), nums.end()) == 1) return 0;
        return (isValid ? n + output - ones : -1);
    }
};