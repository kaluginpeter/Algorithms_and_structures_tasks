# You are given an integer array nums and a positive integer k.
#
# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
#
# A subarray is a contiguous sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
# Example 2:
#
# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= k <= 105
# Solution Two Pointers O(N) O(1)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans: int = 0
        count_sub: int = 0
        left, mx = 0, max(nums)
        for right in range(len(nums)):
            count_sub += nums[right] == mx
            while count_sub >= k:
                count_sub -= nums[left] == mx
                left += 1
            ans += left
        return ans

# Python O(N) O(1) SlidingWindow
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        output: int = 0
        left: int = 0
        count: int = 0
        already_valid: int = 0
        max_element: int = max(nums)
        for right in range(len(nums)):
            if nums[right] == max_element: count += 1
            while count >= k:
                already_valid += 1
                if nums[left] == max_element: count -= 1
                left += 1
            output += already_valid
        return output

# C++ O(N) O(1) SlidingWindow
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        long long output = 0;
        int left = 0, maxElement = *max_element(nums.begin(), nums.end());
        int alreadyValid = 0, count = 0;
        for (int right = 0; right < nums.size(); ++right) {
            if (nums[right] == maxElement) ++count;
            while (count >= k) {
                ++alreadyValid;
                if (nums[left] == maxElement) --count;
                ++left;
            }
            output += alreadyValid;
        }
        return output;
    }
};