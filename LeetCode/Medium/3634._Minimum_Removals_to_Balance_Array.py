# You are given an integer array nums and an integer k.
#
# An array is considered balanced if the value of its maximum element is at most k times the minimum element.
#
# You may remove any number of elements from nums​​​​​​​ without making it empty.
#
# Return the minimum number of elements to remove so that the remaining array is balanced.
#
# Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.
#
#
#
# Example 1:
#
# Input: nums = [2,1,5], k = 2
#
# Output: 1
#
# Explanation:
#
# Remove nums[2] = 5 to get nums = [2, 1].
# Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.
# Example 2:
#
# Input: nums = [1,6,2,9], k = 3
#
# Output: 2
#
# Explanation:
#
# Remove nums[0] = 1 and nums[3] = 9 to get nums = [6, 2].
# Now max = 6, min = 2 and max <= min * k as 6 <= 2 * 3. Thus, the answer is 2.
# Example 3:
#
# Input: nums = [4,6], k = 2
#
# Output: 0
#
# Explanation:
#
# Since nums is already balanced as 6 <= 4 * 2, no elements need to be removed.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 105
# Solution
# Python O(NlogN + N ) O(1) SlidingWindow Sorting
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n: int = len(nums)
        output: int = n - 1
        left: int = 0
        for right in range(n):
            while nums[left] * k < nums[right]: left += 1
            output = min(output, n - (right - left + 1))
        return output

# C++ O(NlogN + N) O(1) Sorting SlidingWindow
class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        size_t n = nums.size(), output = n - 1, left = 0;
        for (size_t right = 0; right < n; ++right) {
            while (nums[right] / nums[left] + (nums[right] % nums[left] == 0 ? 0 : 1) > k) ++left;
            output = std::min(output, n - (right - left + 1));
        }
        return output;
    }
};