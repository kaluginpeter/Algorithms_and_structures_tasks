# You are given an integer array nums.
#
# From any index i, you can jump to another index j under the following rules:
#
# Jump to index j where j > i is allowed only if nums[j] < nums[i].
# Jump to index j where j < i is allowed only if nums[j] > nums[i].
# For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.
#
# Return an array ans where ans[i] is the maximum value reachable starting from index i.
#
#
#
# Example 1:
#
# Input: nums = [2,1,3]
#
# Output: [2,2,3]
#
# Explanation:
#
# For i = 0: No jump increases the value.
# For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
# For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.
# Thus, ans = [2, 2, 3].
#
# Example 2:
#
# Input: nums = [2,3,1]
#
# Output: [3,3,3]
#
# Explanation:
#
# For i = 0: Jump forward to j = 2 as nums[j] = 1 is less than nums[i] = 2, then from i = 2 jump to j = 1 as nums[j] = 3 is greater than nums[2].
# For i = 1: Since nums[1] = 3 is the maximum value in nums, no jump increases the value.
# For i = 2: Jump to j = 1 as nums[j] = 3 is greater than nums[2] = 1.
# Thus, ans = [3, 3, 3].
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# Solution
# Python O(NlogN) O(N) BinarySearch PrefixSum
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        prefix: list[int] = [0] * n
        mx_bound: int = 0
        for i in range(n):
            if nums[i] > mx_bound: mx_bound = nums[i]
            prefix[i] = mx_bound
        m: int = 1
        seen: list[int] = [n - 1]
        for i in range(n - 1, -1, -1):
            if nums[i] < nums[seen[-1]]:
                seen.append(i)
                m += 1
            left: int = 0
            right: int = m - 1
            while left <= right:
                middle: int = left + ((right - left) >> 1)
                if nums[seen[middle]] < prefix[i]:
                    right = middle - 1
                else: left = middle + 1
            if left < m and nums[seen[left]] < prefix[i]:
                prefix[i] = prefix[seen[left]]
        return prefix

# C++ O(NlogN) O(N) PrefixSum BinarySearch
class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        size_t n = nums.size();
        std::vector<int> prefix(n, 0);
        int mxBound = 0;
        for (size_t i = 0; i < n; ++i) {
            if (nums[i] > mxBound) mxBound = nums[i];
            prefix[i] = mxBound;
        }
        size_t m = 1;
        std::vector<size_t> seen = {n - 1};
        for (size_t i = n; i > 0; --i) {
            if (nums[i - 1] < nums[seen.back()]) {
                seen.push_back(i - 1);
                ++m;
            }
            // bound(i) >= bound(i + 1) >= bound(i + 2) <= ...
            // seen(i) >= seen(i + 1) >= seen(i + 2) >= ...
            // find lefmost seen(i) such that nums[i] < nums[curI] and set nums[curI] to bound(i)
            size_t left = 0, right = m - 1;
            while (left <= right) {
                size_t middle = left + ((right - left) >> 1);
                if (nums[seen[middle]] < prefix[i - 1]) {
                    right = middle;
                    if (!right) break;
                    --right;
                } else left = middle + 1;
            }
            if (left < m && nums[seen[left]] < prefix[i - 1]) {
                prefix[i - 1] = prefix[seen[left]];
            }
        }
        return prefix;
    }
};