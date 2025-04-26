# You are given an integer array nums and two integers minK and maxK.
#
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
#
# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.
#
# A subarray is a contiguous part of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
# Example 2:
#
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# 1 <= nums[i], minK, maxK <= 106
# Solution
# Python O(N) O(N) SlidingWindow
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        output: int = 0
        left: int = 0
        hashmap: dict[int, int] = dict()
        already_valid: int = 0
        is_min: bool = False
        is_max: bool = False
        for right in range(len(nums)):
            if nums[right] < minK or nums[right] > maxK:
                already_valid = 0
                left = right + 1
                is_min, is_max = False, False
                hashmap.clear()
            else:
                hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1
                if nums[right] == minK: is_min = True
                if nums[right] == maxK: is_max = True
                while is_min and is_max:
                    hashmap[nums[left]] -= 1
                    already_valid += 1
                    if not hashmap[nums[left]]:
                        if nums[left] == minK: is_min = False
                        if nums[left] == maxK: is_max = False
                        del hashmap[nums[left]]
                    left += 1
                output += already_valid
        return output

# C++ O(N) O(N) SlidingWindow
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long output = 0;
        int left = 0, alreadyValid = 0;
        bool isMin = false, isMax = false;
        unordered_map<int, int> hashmap;
        for (int right = 0; right < nums.size(); ++right) {
            if (nums[right] < minK || nums[right] > maxK) {
                hashmap.clear();
                alreadyValid = 0;
                left = right + 1;
                isMin = false;
                isMax = false;
            } else {
                ++hashmap[nums[right]];
                if (nums[right] == minK) isMin = true;
                if (nums[right] == maxK) isMax = true;
                while (isMin && isMax) {
                    ++alreadyValid;
                    --hashmap[nums[left]];
                    if (!hashmap[nums[left]]) {
                        if (nums[left] == minK) isMin = false;
                        else if (nums[left] == maxK) isMax = false;
                        hashmap.erase(nums[left]);
                    }
                    ++left;
                }
                output += alreadyValid;
            }
        }
        return output;
    }
};