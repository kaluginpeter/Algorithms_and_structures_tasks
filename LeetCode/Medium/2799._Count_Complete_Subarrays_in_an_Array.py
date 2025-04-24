# You are given an array nums consisting of positive integers.
#
# We call a subarray of an array complete if the following condition is satisfied:
#
# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.
#
# A subarray is a contiguous non-empty part of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,3,1,2,2]
# Output: 4
# Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
# Example 2:
#
# Input: nums = [5,5,5,5]
# Output: 10
# Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2000
# Solution
# Python O(N) O(D) SlidingWindow HashMap
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        bound: int = len(set(nums))
        window: dict[int, int] = dict()
        left: int = 0
        output: int = 0
        already_valid: int = 0
        for right in range(len(nums)):
            window[nums[right]] = window.get(nums[right], 0) + 1
            while len(window) == bound:
                already_valid += 1
                window[nums[left]] -= 1
                if not window[nums[left]]: del window[nums[left]]
                left += 1
            output += already_valid
        return output

# C++ O(N) O(D) SlidingWindow HashMap
class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        int bound = unordered_set<int>(nums.begin(), nums.end()).size();
        unordered_map<int, int> window;
        int left = 0, alreadyValid = 0, output = 0;
        for (int right = 0; right < nums.size(); ++right) {
            ++window[nums[right]];
            while (window.size() == bound) {
                ++alreadyValid;
                --window[nums[left]];
                if (!window[nums[left]]) window.erase(nums[left]);
                ++left;
            }
            output += alreadyValid;
        }
        return output;
    }
};