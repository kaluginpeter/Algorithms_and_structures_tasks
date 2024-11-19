# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
#
# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
# Example 2:
#
# Input: nums = [4,4,4], k = 3
# Output: 0
# Explanation: The subarrays of nums with length 3 are:
# - [4,4,4] which does not meet the requirements because the element 4 is repeated.
# We return 0 because no subarrays meet the conditions.
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 105
# 1 <= nums[i] <= 105
# Solution
# Python O(N) O(N) Sliding Window HashMap
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hashmap: dict[int, int] = dict()
        max_sum: int = 0
        cur_sum: int = 0
        n: int = len(nums)
        size: int = 0
        left: int = 0
        for right in range(n):
            hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1
            cur_sum += nums[right]
            size += 1
            while left < right and (size > k or hashmap[nums[right]] > 1):
                size -= 1
                hashmap[nums[left]] -= 1
                cur_sum -= nums[left]
                left += 1
            if size == k:
                max_sum = max(max_sum, cur_sum)
        return max_sum

# C++ O(N) O(N) Sliding Window HashMap
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        std::unordered_map<int, int> hashmap;
        long long maxSum = 0;
        long long curSum = 0;
        int size = 0;
        int n =  nums.size();
        int left = 0;
        for (int right = 0; right < n; ++right) {
            ++hashmap[nums[right]];
            ++size;
            curSum += nums[right];
            while (left < right && (size > k || hashmap[nums[right]] > 1)) {
                --hashmap[nums[left]];
                curSum -= nums[left];
                --size;
                ++left;
            }
            if (size == k) {
                maxSum = std::max(maxSum, curSum);
            }
        }
        return maxSum;
    }
};