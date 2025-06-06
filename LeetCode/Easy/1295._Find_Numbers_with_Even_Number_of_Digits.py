# Given an array nums of integers, return how many of them contain an even number of digits.
#
# Example 1:
#
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:
#
# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits.
#
# Constraints:
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 105
# Solution
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for i in nums if len(str(i)) % 2 == 0)


# Python O(NlogM) O(1) Math
class Solution:
    def get_digits(self, n: int) -> int:
        digits: int = 0
        while n:
            digits += 1
            n //= 10
        return digits

    def findNumbers(self, nums: List[int]) -> int:
        output: int = 0
        for num in nums:
            if not (self.get_digits(num) & 1):
                output += 1
        return output

# C++ O(NlogM) O(1) Math
class Solution {
public:
    int getDigits(int n) {
        int digits = 0;
        while (n) {
            ++digits;
            n /= 10;
        }
        return digits;
    }

    int findNumbers(vector<int>& nums) {
        int output = 0;
        for (int num : nums) {
            if ((getDigits(num) & 1) == 0) ++output;
        }
        return output;
    }
};