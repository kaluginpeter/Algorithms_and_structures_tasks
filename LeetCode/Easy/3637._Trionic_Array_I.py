# You are given an integer array nums of length n.
#
# An array is trionic if there exist indices 0 < p < q < n − 1 such that:
#
# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.
#
#
#
# Example 1:
#
# Input: nums = [1,3,5,4,2,6]
#
# Output: true
#
# Explanation:
#
# Pick p = 2, q = 4:
#
# nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
# nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
# nums[4...5] = [2, 6] is strictly increasing (2 < 6).
# Example 2:
#
# Input: nums = [2,1,3]
#
# Output: false
#
# Explanation:
#
# There is no way to pick p and q to form the required three segments.
#
#
#
# Constraints:
#
# 3 <= n <= 100
# -1000 <= nums[i] <= 1000
# Solution
# Python O(N) O(1) Simulation Greedy
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        is_incr: bool = True
        is_decr: bool = False
        was_decr: bool = False
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if is_decr:
                    if was_decr: return False
                    was_decr = True
                    is_decr = False
                    is_incr = True
            elif nums[i] < nums[i - 1]:
                if was_decr or i == 1: return False
                is_decr = True
                is_incr = False
            else: return False
        return was_decr

# C++ O(N) O(1) Greedy Simulation
class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        bool isIncr = true, isDecr = false, wasDecr = false;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[i - 1]) {
                if (isDecr) {
                    if (wasDecr) return false;
                    wasDecr = true;
                    isDecr = false;
                    isIncr = true;
                }
            } else if (nums[i] < nums[i - 1]) {
                if (wasDecr || i == 1) return false;
                isDecr = true;
                isIncr = false;
            } else return false;
        }
        return wasDecr;
    }
};