# Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.
#
#
# Example 1:
#
# Input: nums1 = [2,5], nums2 = [3,4], k = 2
# Output: 8
# Explanation: The 2 smallest products are:
# - nums1[0] * nums2[0] = 2 * 3 = 6
# - nums1[0] * nums2[1] = 2 * 4 = 8
# The 2nd smallest product is 8.
# Example 2:
#
# Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
# Output: 0
# Explanation: The 6 smallest products are:
# - nums1[0] * nums2[1] = (-4) * 4 = -16
# - nums1[0] * nums2[0] = (-4) * 2 = -8
# - nums1[1] * nums2[1] = (-2) * 4 = -8
# - nums1[1] * nums2[0] = (-2) * 2 = -4
# - nums1[2] * nums2[0] = 0 * 2 = 0
# - nums1[2] * nums2[1] = 0 * 4 = 0
# The 6th smallest product is 0.
# Example 3:
#
# Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
# Output: -6
# Explanation: The 3 smallest products are:
# - nums1[0] * nums2[4] = (-2) * 5 = -10
# - nums1[0] * nums2[3] = (-2) * 4 = -8
# - nums1[4] * nums2[0] = 2 * (-3) = -6
# The 3rd smallest product is -6.
#
#
# Constraints:
#
# 1 <= nums1.length, nums2.length <= 5 * 104
# -105 <= nums1[i], nums2[j] <= 105
# 1 <= k <= nums1.length * nums2.length
# nums1 and nums2 are sorted.
# Solution
# Python O(NlogClogM) O(1) BinarySearch
class Solution:
    # Pytnon way to use binary search manually, will get TLE
    def count(self, nums2: list[int], x1: int, bound: int) -> int:
        match x1:
            case x1 if x1 > 0:
                return bisect_right(nums2, bound // x1)
            case x1 if x1 < 0:
                return len(nums2) - bisect_left(nums2, -(-bound // x1))
            case 0: return [0, len(nums2)][bound >= 0]

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1: int = len(nums1)
        left: int = -10000000001
        right: int = 10000000001
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            pairs: int = 0
            for i in range(n1): pairs += self.count(nums2, nums1[i], middle)
            if pairs < k: left = middle + 1
            else: right = middle - 1
        return left

# C++ O(NlogClogM) O(1) BinarySearch
class Solution {
public:
    int count_(std::vector<int> &nums2, long long x1, long long bound) {
        int n2 = nums2.size(), left = 0, right = n2 - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (x1 >= 0 && nums2[middle] * x1 <= bound || x1 < 0 && nums2[middle] * x1 > bound) left = middle + 1;
            else right = middle - 1;
        }
        return (x1 >= 0 ? left : n2 - left);
    }
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        int n1 = nums1.size();
        long long left = -1e10 - 1, right = 1e10 + 1;
        while (left <= right) {
            long long middle = left + ((right - left) >> 1), pairs = 0;
            for (int i = 0; i < n1; ++i) pairs += count_(nums2, nums1[i], middle);
            if (pairs < k) left = middle + 1;
            else right = middle - 1;
        }
        return left;
    }
};