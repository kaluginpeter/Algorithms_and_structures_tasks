# You are given an integer array nums and an integer k.
#
# You are allowed to perform the following operation on each element of the array at most once:
#
# Add an integer in the range [-k, k] to the element.
# Return the maximum possible number of distinct elements in nums after performing the operations.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,3,3,4], k = 2
#
# Output: 6
#
# Explanation:
#
# nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.
#
# Example 2:
#
# Input: nums = [4,4,4,4], k = 1
#
# Output: 3
#
# Explanation:
#
# By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= k <= 109
# Solution
# Python O(NlogN) O(1) Sorting Greedy
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        lower: int = nums[0] - k
        count: int = 1
        for num in nums[1:]:
            if lower < num - k: # We need to update lower bound
                lower = num - k
                count += 1
            elif num + k > lower: # Number can be placed at lower + 1
                lower += 1
                count += 1
        return count

# C++ O(NlogN) O(1) Sorting Greedy
class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int lower = nums[0] - k;
        int count = 1;
        for (int idx = 1; idx < nums.size(); ++idx) { // We need to update lower bound
            if (lower < nums[idx] - k) {
                lower = nums[idx] - k;
                ++count;
            } else if (lower < nums[idx] + k) { // Number can be placed at lower + 1
                ++lower;
                ++count;
            }
        }
        return count;
    }
};
