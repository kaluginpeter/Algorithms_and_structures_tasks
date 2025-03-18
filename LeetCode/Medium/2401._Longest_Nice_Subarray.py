# You are given an array nums consisting of positive integers.
#
# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
#
# Return the length of the longest nice subarray.
#
# A subarray is a contiguous part of an array.
#
# Note that subarrays of length 1 are always considered nice.
#
#
#
# Example 1:
#
# Input: nums = [1,3,8,48,10]
# Output: 3
# Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
# - 3 AND 8 = 0.
# - 3 AND 48 = 0.
# - 8 AND 48 = 0.
# It can be proven that no longer nice subarray can be obtained, so we return 3.
# Example 2:
#
# Input: nums = [3,1,5,11,13]
# Output: 1
# Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# Solution
# Python O(N) O(1) BitManipulation SlidingWindow
from collections.abc import Iterator
import math


class Solution:
    def get_bound(self, n: int) -> int:
        if n == 0: return 1
        return n.bit_length()

    def get_bits(self, n: int) -> Iterator[int]:
        while n:
            yield n % 2
            n //= 2

    def add(self, hashmap: list[int], n: int) -> None:
        bound: int = self.get_bound(n)
        bits: Iterator[int] = self.get_bits(n)
        for idx in range(bound):
            hashmap[idx] |= next(bits)

    def subtract(self, hashmap: list[int], n: int) -> None:
        bound: int = self.get_bound(n)
        bits: Iterator[int] = self.get_bits(n)
        for idx in range(bound):
            if next(bits): hashmap[idx] = 0

    def can_add(self, hashmap: list[int], n: int) -> bool:
        bound: int = self.get_bound(n)
        bits: Iterator[int] = self.get_bits(n)
        for idx in range(bound):
            if hashmap[idx] & next(bits):  return False
        return True

    def longestNiceSubarray(self, nums: List[int]) -> int:
        hashmap: list[int] = [0] * 32
        max_len: int = 0
        left: int = 0
        for right in range(len(nums)):
            while not self.can_add(hashmap, nums[right]):
                self.subtract(hashmap, nums[left])
                left += 1
            self.add(hashmap, nums[right])
            max_len = max(max_len, right - left + 1)
        return max_len

# C++ O(N) O(1) BitManipulation SlidingWindow
class Solution {
public:
    bool canAdd(bitset<32>& hashmap, int& n) {
        bitset<32> nBits (n);
        for (int idx = 0; idx < 32; ++idx) {
            if (hashmap[idx] & nBits[idx]) return false;
        }
        return true;
    }
    void subtract(bitset<32>& hashmap, int& n) {
        bitset<32> nBits (n);
        for (int idx = 0; idx < 32; ++idx) {
            if (nBits[idx]) hashmap[idx] = 0;
        }
    }
    void add(bitset<32>& hashmap, int& n) {
        bitset<32> nBits (n);
        for (int idx = 0; idx < 32; ++idx) {
            if (nBits[idx]) hashmap[idx] = 1;
        }
    }
    int longestNiceSubarray(vector<int>& nums) {
        int maxLen = 0;
        int left = 0;
        bitset<32> hashmap;
        for (int right = 0; right < nums.size(); ++right) {
            while (!canAdd(hashmap, nums[right])) {
                subtract(hashmap, nums[left]);
                ++left;
            }
            add(hashmap, nums[right]);
            maxLen = max(maxLen, right - left + 1);
        }
        return maxLen;
    }
};