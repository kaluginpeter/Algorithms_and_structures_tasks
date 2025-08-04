# The frequency of an element is the number of times it occurs in an array.
#
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
#
# Return the maximum possible frequency of an element after performing at most k operations.
#
#
#
# Example 1:
#
# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.
# Example 2:
#
# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
# Example 3:
#
# Input: nums = [3,9,6], k = 2
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= k <= 105
# Solution
# Python O(NlogN) O(1) SlidingWindow
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        output: int = 1
        left: int = 0
        wasted: int = 0
        for right in range(1, len(nums)):
            wasted += (right - left) * (nums[right] - nums[right - 1])
            while wasted > k:
                wasted -= nums[right] - nums[left]
                left += 1
            output = max(output, right - left + 1)
        return output

# C++ O(NlogN) O(1) SlidingWindow
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        int output = 1, left = 0;
        long long wasted = 0;
        std::sort(nums.begin(), nums.end());
        for (int right = 1; right < nums.size(); ++right) {
            wasted += static_cast<long long>(nums[right] - nums[right - 1]) * (right - left);
            while (wasted > k) {
                wasted -= nums[right] - nums[left];
                ++left;
            }
            output = std::max(output, right - left + 1);
        }
        return output;
    }
};