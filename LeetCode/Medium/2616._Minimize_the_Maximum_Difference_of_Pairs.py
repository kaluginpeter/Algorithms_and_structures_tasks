# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.
#
# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
#
# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.
#
#
#
# Example 1:
#
# Input: nums = [10,1,2,7,1,3], p = 2
# Output: 1
# Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5.
# The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
# Example 2:
#
# Input: nums = [4,2,1,2], p = 1
# Output: 0
# Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= p <= (nums.length)/2
# Solution
# Python O(NlogN + NlogD) O(1) BinarySearch Sorting Greedy
class Solution:
    def check(self, target: int, nums: list[int], p: int) -> bool:
        i: int = 0
        count: int = 0
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] <= target:
                i += 1
                count += 1
            i += 1
        return count >= p

    def minimizeMax(self, nums: List[int], p: int) -> int:
        if not p: return 0
        nums.sort()
        n: int = len(nums)
        left: int = 0
        right: int = nums[-1] - nums[0]
        output: int = 0
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if self.check(middle, nums, p):
                output = middle
                right = middle - 1
            else:
                left = middle + 1
        return output

# C++ O(NlogN + NlogD) O(1) Sorting BinarySearch Greedy
class Solution {
public:
    bool check(int &target, std::vector<int> &nums, int &p) {
        int i = 0, count = 0;
        while (i < nums.size() - 1) {
            if (nums[i + 1] - nums[i] <= target) {
                ++i;
                ++count;
            }
            ++i;
        }
        return count >= p;
    }

    int minimizeMax(vector<int>& nums, int p) {
        if (!p) return 0;
        int n = nums.size();
        std::sort(nums.begin(), nums.end());
        int output = 0;
        int left = 0, right = nums[n - 1] - nums[0];
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (check(middle, nums, p)) {
                output = middle;
                right = middle - 1;
            } else left = middle + 1;
        }
        return output;
    }
};