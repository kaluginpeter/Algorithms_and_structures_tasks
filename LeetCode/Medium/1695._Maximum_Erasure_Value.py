# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
#
# Return the maximum score you can get by erasing exactly one subarray.
#
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
#
#
#
# Example 1:
#
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
# Example 2:
#
# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# Solution
# Python O(N) O(D) HashMap TwoPointers
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        output: int = 0
        hashmap: list[int] = [-1] * (10**5 + 1)
        left: int = 0
        window_sum: int = 0
        for right in range(len(nums)):
            if hashmap[nums[right]] != -1:
                while left <= hashmap[nums[right]]:
                    window_sum -= nums[left]
                    hashmap[nums[left]] = -1
                    left += 1
            window_sum += nums[right]
            hashmap[nums[right]] = right
            output = max(output, window_sum)
        return output

# C++ O(N) O(D) HashMap TwoPointers
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int output = 0;
        int left = 0, windowSum = 0;
        std::vector<int> hashmap(1e5 + 1, -1);
        for (int right = 0; right < nums.size(); ++right) {
            if (hashmap[nums[right]] != -1) {
                while (left <= hashmap[nums[right]]) {
                    hashmap[nums[left]] = -1;
                    windowSum -= nums[left];
                    ++left;
                }
            }
            windowSum += nums[right];
            hashmap[nums[right]] = right;
            output = std::max(output, windowSum);
        }
        return output;
    }
};