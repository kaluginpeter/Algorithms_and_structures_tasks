# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
#
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
#
#
# Example 1:
#
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
# Example 2:
#
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1
#
#
# Constraints:
#
# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
# Solution
# Python O(N**2) O(N**2) HashMap
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        first_pairs: dict[int, int] = dict()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pair_sum: int = nums1[i] + nums2[j]
                first_pairs[pair_sum] = first_pairs.get(pair_sum, 0) + 1
        output: int = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                pair_sum: int = nums3[i] + nums4[j]
                output += first_pairs.get(-pair_sum, 0)
        return output

# C++ O(N**2) O(N**2) HashMap
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        std::unordered_map<long long, int> firstPairs;
        for (int i = 0; i < nums1.size(); ++i) {
            for (int j = 0; j < nums2.size(); ++j) {
                ++firstPairs[{nums1[i] + nums2[j]}];
            }
        }
        int output = 0;
        for (int i = 0; i < nums3.size(); ++i) {
            for (int j = 0; j < nums4.size(); ++j) {
                long long pairSum = nums3[i] + nums4[j];
                output += firstPairs[-pairSum];
            }
        }
        return output;
    }
};