# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.
#
#
#
# Example 1:
#
# Input: nums = [4,14,2]
# Output: 6
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case).
# The answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
# Example 2:
#
# Input: nums = [4,14,4]
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 109
# The answer for the given input will fit in a 32-bit integer.
# Solution
# Python O(Nlog(max(N)) + log(max(N))) O(log(max(N))) BitManipulation HashMap Math
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        hashmap: list[list[int, int]] = [[0, 0] for _ in range(33)]
        for num in nums:
            bit: int = 32
            while num:
                hashmap[bit][num & 1] += 1
                bit -= 1
                num >>= 1
            while bit >= 0:
                hashmap[bit][0] += 1
                bit -= 1
        output: int = 0
        for zeros, ones in hashmap:
            if not zeros or not ones: continue
            output += zeros * ones
        return output

# C++ O(Nlog(max(N)) + log(max(N))) O(log(max(N))) BitManipulation HashMap Math
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        std::array<std::array<int, 2>, 33> hashmap{};
        for (int& num : nums) {
            int bit = 32;
            while (num) {
                ++hashmap[bit][num % 2];
                --bit;
                num >>= 1;
            }
            while (bit >= 0) {
                ++hashmap[bit][0];
                --bit;
            }
        }
        int output = 0;
        for (int bit = 0; bit < 33; ++bit) {
            if (!hashmap[bit][1] || !hashmap[bit][0]) continue;
            output += hashmap[bit][0] * hashmap[bit][1];
        }
        return output;
    }
};