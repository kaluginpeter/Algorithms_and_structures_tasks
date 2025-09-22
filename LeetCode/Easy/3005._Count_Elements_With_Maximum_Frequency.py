# You are given an array nums consisting of positive integers.
#
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
#
# The frequency of an element is the number of occurrences of that element in the array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.
# Example 2:
#
# Input: nums = [1,2,3,4,5]
# Output: 5
# Explanation: All elements of the array have a frequency of 1 which is the maximum.
# So the number of elements in the array with maximum frequency is 5.
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# Solution O(N) O(N) HashTable
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d: dict = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        count, m = 0, max(d.values())
        for i in d:
            if d[i] == m:
                count += d[i]
        return count


# Python O(N) O(D) HashMap
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        output: int = 0
        threshold: int = 0
        hashmap: list[int] = [0] * 101
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > threshold: threshold = output = hashmap[num]
            elif hashmap[num] == threshold: output += hashmap[num]
        return output

# C++ O(N) O(D) HashMap
class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int output = 0, threshold = 0;
        std::array<int, 101> hashmap{};
        for (int& num : nums) {
            ++hashmap[num];
            if (hashmap[num] > threshold) {
                output = hashmap[num];
                threshold = hashmap[num];
            } else if (hashmap[num] == threshold) output += hashmap[num];
        }
        return output;
    }
};