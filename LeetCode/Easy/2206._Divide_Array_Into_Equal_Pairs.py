# You are given an integer array nums consisting of 2 * n integers.
# You need to divide nums into n pairs such that:
# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.
#
# Example 1:
#
# Input: nums = [3,2,3,2,2,2]
# Output: true
# Explanation:
# There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
#
# Constraints:
# nums.length == 2 * n
# 1 <= n <= 500
# 1 <= nums[i] <= 500
# Solution
# Python O(N**2) O(N)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(nums.count(i) % 2 == 0 for i in set(nums))


# Python O(N) O(N) HashMap Counting
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap: dict[int, int] = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        return all(not (freq & 1) for freq in hashmap.values())

# C++ O(N) O(N) HashMap Counting
class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_map<int, int> hashmap;
        for (int& num : nums) {
            ++hashmap[num];
        }
        for (auto& p : hashmap) {
            if (p.second % 2 != 0) return false;
        }
        return true;
    }
};