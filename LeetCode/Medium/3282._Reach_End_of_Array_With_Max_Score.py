# You are given an integer array nums of length n.
#
# Your goal is to start at index 0 and reach index n - 1. You can only jump to indices greater than your current index.
#
# The score for a jump from index i to index j is calculated as (j - i) * nums[i].
#
# Return the maximum possible total score by the time you reach the last index.
#
#
#
# Example 1:
#
# Input: nums = [1,3,1,5]
#
# Output: 7
#
# Explanation:
#
# First, jump to index 1 and then jump to the last index. The final score is 1 * 1 + 2 * 3 = 7.
#
# Example 2:
#
# Input: nums = [4,3,1,3,2]
#
# Output: 16
#
# Explanation:
#
# Jump directly to the last index. The final score is 4 * 4 = 16.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# Solution
# Python O(N) O(1) Dynamic Programming
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n: int = len(nums)
        j: int = n - 1
        cur_max_number: int = 0
        steps_after_max_number: int = 0
        previous_best: int = 0
        max_score: int = 0
        for i in range(len(nums)):
            steps_after_max_number += 1
            if nums[i] <= cur_max_number: continue
            currrent_score: int = nums[i] * (j - i)
            previous_best += cur_max_number * steps_after_max_number
            max_score = max(max_score, currrent_score + previous_best)
            cur_max_number, steps_after_max_number = nums[i], 0
        return max_score

# C++ O(N) O(1) Dynamic Programming
class Solution {
public:
    long long findMaximumScore(vector<int>& nums) {
        long long n, j, cur_max_number, previous_best, steps_after_max_number;
        n = nums.size();
        j = n - 1;
        cur_max_number = 0;
        previous_best = 0;
        steps_after_max_number = 0;
        long long max_score = 0;
        for (int i = 0; i < n; i++) {
            steps_after_max_number += 1;
            if (nums[i] <= cur_max_number) {
                continue;
            }
            long long current_cost = (j - i) * nums[i];
            previous_best += cur_max_number * steps_after_max_number;
            max_score = std::max(max_score, current_cost + previous_best);
            cur_max_number = nums[i];
            steps_after_max_number = 0;
        }
        return max_score;
    }
};