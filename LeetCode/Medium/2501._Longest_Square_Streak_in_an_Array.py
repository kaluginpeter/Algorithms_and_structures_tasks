# You are given an integer array nums. A subsequence of nums is called a square streak if:
#
# The length of the subsequence is at least 2, and
# after sorting the subsequence, each element (except the first element) is the square of the previous number.
# Return the length of the longest square streak in nums, or return -1 if there is no square streak.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#
#
#
# Example 1:
#
# Input: nums = [4,3,6,16,8,2]
# Output: 3
# Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
# - 4 = 2 * 2.
# - 16 = 4 * 4.
# Therefore, [4,16,2] is a square streak.
# It can be shown that every subsequence of length 4 is not a square streak.
# Example 2:
#
# Input: nums = [2,3,5,6,7]
# Output: -1
# Explanation: There is no square streak in nums so return -1.
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# 2 <= nums[i] <= 105
# Solution
# Python O(N) O(1) HashSet
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        bound: int = 100_001
        mx_seq: int = -1
        hashset: set[int] = set(nums)
        for num in range(1, 318):
            if num in hashset:
                cur_count: int = 1
                while num*num in hashset:
                    cur_count += 1
                    num *= num
                if cur_count > 1:
                    mx_seq = max(mx_seq, cur_count)
        return mx_seq

# C++ O(N) O(1) Bitset
class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        std::vector<int> bitset(100001);
        for (int num : nums) {
            ++bitset[num];
        }
        int mxSeq = -1;
        for (int num = 1; num < 317; ++num) {
            if (bitset[num]) {
                int curCount = 0;
                long long square = num;
                while (square < 100001 && bitset[square]) {
                    ++curCount;
                    square = square * square;
                }
                if (curCount > 1) {
                    mxSeq = std::max(mxSeq, curCount);
                }
            }
        }
        return mxSeq;
    }
};