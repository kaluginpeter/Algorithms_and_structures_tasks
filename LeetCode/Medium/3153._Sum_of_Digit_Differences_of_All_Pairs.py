# You are given an array nums consisting of positive integers where all integers have the same number of digits.
#
# The digit difference between two integers is the count of different digits that are in the same position in the two integers.
#
# Return the sum of the digit differences between all pairs of integers in nums.
#
#
#
# Example 1:
#
# Input: nums = [13,23,12]
#
# Output: 4
#
# Explanation:
# We have the following:
# - The digit difference between 13 and 23 is 1.
# - The digit difference between 13 and 12 is 1.
# - The digit difference between 23 and 12 is 2.
# So the total sum of digit differences between all pairs of integers is 1 + 1 + 2 = 4.
#
# Example 2:
#
# Input: nums = [10,10,10,10]
#
# Output: 0
#
# Explanation:
# All the integers in the array are the same. So the total sum of digit differences between all pairs of integers will be 0.
#
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# 1 <= nums[i] < 109
# All integers in nums have the same number of digits.
# Solution
# Python O(Nlog(max(N)) + log(max(N))) O(log(max(N)) * 10) HashMap BitManipulation
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        hashmap: list[list[int]] = [[0] * 10 for _ in range(33)]
        count: list[int] = [0] * 33
        for num in nums:
            place: int = 0
            while num:
                hashmap[place][num % 10] += 1
                count[place] += 1
                num //= 10
                place += 1
        output: int = 0
        for bit in range(33):
            for d in range(10):
                if not hashmap[bit][d]: continue
                count[bit] -= hashmap[bit][d]
                output += hashmap[bit][d] * count[bit]
        return output

# C++ O(Nlog(max(N)) + log(max(N))) O(log(max(N))) BitManipulation HashMap
class Solution {
public:
    long long sumDigitDifferences(vector<int>& nums) {
        std::array<std::array<int, 10>, 33> hashmap{};
        std::array<int, 33> count{};
        for (int num : nums) {
            int place = 0;
            while (num) {
                ++hashmap[place][num % 10];
                ++count[place];
                num /= 10;
                ++place;
            }
        }
        long long output = 0;
        for (int bit = 0; bit < 33; ++bit) {
            for (int d = 0; d < 10; ++d) {
                if (!hashmap[bit][d]) continue;
                count[bit] -= hashmap[bit][d];
                output += static_cast<long long>(hashmap[bit][d]) * count[bit];
            }
        }
        return output;
    }
};