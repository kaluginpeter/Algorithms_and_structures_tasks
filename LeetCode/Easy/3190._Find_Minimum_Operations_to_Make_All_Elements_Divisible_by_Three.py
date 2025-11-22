# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
#
# Return the minimum number of operations to make all elements of nums divisible by 3.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
#
# Output: 3
#
# Explanation:
#
# All array elements can be made divisible by 3 using 3 operations:
#
# Subtract 1 from 1.
# Add 1 to 2.
# Subtract 1 from 4.
# Example 2:
#
# Input: nums = [3,6,9]
#
# Output: 0
#
#
#
# Constraints:
#
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50
# Solution One Liner O(N) O(1)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(i % 3 != 0 for i in nums)


# Python O(N) O(1) Greedy
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(max(0, min(3 - num % 3, num % 3)) for num in nums)

# C++ O(N) O(1) Greedy
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int output = 0;
        for (int& num : nums) output += std::max(0, std::min(3 - num % 3, num % 3));
        return output;
    }
};