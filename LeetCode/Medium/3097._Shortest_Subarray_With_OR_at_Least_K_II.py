# You are given an array nums of non-negative integers and an integer k.
#
# An array is called special if the bitwise OR of all of its elements is at least k.
#
# Return the length of the shortest special non-empty
# subarray
#  of nums, or return -1 if no special subarray exists.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3], k = 2
#
# Output: 1
#
# Explanation:
#
# The subarray [3] has OR value of 3. Hence, we return 1.
#
# Example 2:
#
# Input: nums = [2,1,8], k = 10
#
# Output: 3
#
# Explanation:
#
# The subarray [2,1,8] has OR value of 11. Hence, we return 3.
#
# Example 3:
#
# Input: nums = [1,2], k = 0
#
# Output: 1
#
# Explanation:
#
# The subarray [1] has OR value of 1. Hence, we return 1.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 105
# 0 <= nums[i] <= 109
# 0 <= k <= 109
# Solution
# Python O(N) O(1) Bit Manipulation
class Solution:
    def fill_bits(self, num: int, bits: list[int]) -> None:
        bit: int = 0
        while num:
            bits[bit] += num & 1
            num >>= 1
            bit += 1

    def erase_bits(self, num: int, bits: list[int]) -> None:
        bit: int = 0
        while num:
            bits[bit] -= num & 1
            num >>= 1
            bit += 1

    def check_on_k(self, bits: list[int], k_bits: list[int]) -> bool:
        is_valid: bool = True
        for bit in range(32 - 1, -1, -1):
            if bits[bit] and not k_bits[bit]: # Current OR greater than K
                break
            if k_bits[bit] and not bits[bit]: # Current OR less than K
                is_valid = False
                break
        return is_valid

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_dist: int = 2 * 10**5
        left: int = 0
        k_bits: list[int] = [0] * 32
        self.fill_bits(k, k_bits)
        bits: list[int] = [0] * 32
        for right in range(len(nums)):
            self.fill_bits(nums[right], bits)
            while left <= right and self.check_on_k(bits, k_bits):
                min_dist = min(min_dist, right - left + 1)
                self.erase_bits(nums[left], bits)
                left += 1
        return min_dist if min_dist != 2 * 10**5 else -1

# C++ O(N) O(1) Bit Manipulation
class Solution {
public:
    void fillBits(int num, std::vector<int>& bits) {
        int bit = 0;
        while (num) {
            bits[bit] += num & 1;
            ++bit;
            num >>= 1;
        }
    }

    void eraseBits(int num, std::vector<int>& bits) {
        int bit = 0;
        while (num) {
            bits[bit] -= num & 1;
            ++bit;
            num >>= 1;
        }
    }

    bool checkOnK(std::vector<int>& bits, std::vector<int>& k_bits) {
        bool isValid = true;
        for (int bit = 32 - 1; bit >= 0; --bit) {
            if (bits[bit] && !k_bits[bit]) { // Current OR greater than K
                break;
            }
            if (k_bits[bit] && !bits[bit]) { // Current OR less than K
                isValid = false;
                break;
            }
        }
        return isValid;
    }
    int minimumSubarrayLength(vector<int>& nums, int k) {
        std::vector<int> k_bits(32, 0);
        fillBits(k, k_bits);
        std::vector<int> bits(32, 0);
        int minDistance = 2 * std::pow(10, 5);
        int left = 0;
        for (int right = 0; right < nums.size(); ++right) {
            fillBits(nums[right], bits);
            while (left <= right && checkOnK(bits, k_bits)) {
                minDistance = std::min(minDistance, right - left + 1);
                eraseBits(nums[left], bits);
                ++left;
            }
        }
        return (minDistance != 2 * std::pow(10, 5)? minDistance : -1);
    }
};