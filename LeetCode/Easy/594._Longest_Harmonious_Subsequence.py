# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
#
# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
#
#
#
# Example 1:
#
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: 2
# Example 3:
#
# Input: nums = [1,1,1,1]
# Output: 0
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109
# Solution HashTable O(N) O(N)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ht: dict = {}
        for i in nums:
            ht[i] = ht.get(i, 0) + 1
        top: int = 0
        for i in ht:
            if i-1 in ht:
                top = max(top, ht[i] + ht[i-1])
        return top


# Python O(NlogN) O(1) Sorting SlidingWindow
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        output: int = 0
        left: int = 0
        nums.sort()
        for right in range(len(nums)):
            while left < right and nums[right] - nums[left] > 1: left += 1
            if nums[right] - nums[left] == 1: output = max(output, right - left + 1)
        return output

# C++ O(NlogN) O(1) Sorting SlidingWindow
class Solution {
public:
    int findLHS(vector<int>& nums) {
        int output = 0;
        int left = 0;
        std::sort(nums.begin(), nums.end());
        for (int right = 0; right < nums.size(); ++right) {
            while (left < right && nums[right] - nums[left] > 1) ++left;
            if (nums[right] - nums[left] == 1) output = std::max(output, right - left + 1);
        }
        return output;
    }
};

# Python O(N) O(N) HashMap
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        output: int = 0
        hashmap: dict[int, int] = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for num in nums:
            if num - 1 in hashmap: output = max(output, hashmap[num] + hashmap[num - 1])
        return output

# C++ O(N) O(N) HashMap
class Solution {
public:
    int findLHS(vector<int>& nums) {
        int output = 0;
        std::unordered_map<int, int> hashmap;
        for (int &num : nums) ++hashmap[num];
        for (int &num : nums) {
            if (hashmap.count(num - 1)) output = std::max(output, hashmap[num] + hashmap[num - 1]);
        }
        return output;
    }
};