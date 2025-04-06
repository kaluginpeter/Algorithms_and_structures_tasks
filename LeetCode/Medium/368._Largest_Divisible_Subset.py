# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
#
# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
# Example 2:
#
# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 109
# All the integers in nums are unique.
# Solution
# Python O(NlogN + N^2) O(N) DynamicProgramming Math Sorting
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n: int = len(nums)
        dp: list[int] = [1] * n
        prev: list[int] = [-1] * n
        for right in range(n):
            for left in range(right):
                if nums[right] % nums[left] == 0:
                    if dp[left] + 1 > dp[right]:
                        dp[right] = dp[left] + 1
                        prev[right] = left
        idx: int = 0
        for i in range(1, n):
            if dp[idx] < dp[i]: idx = i
        path: list[int] = [nums[idx]]
        while prev[idx] != -1:
            path.append(nums[prev[idx]])
            idx = prev[idx]
        return path

# C++ O(NlogN + N^2) O(N) DynamicProgramming Sorting Math
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<int> dp (n, 1);
        vector<int> prev(n, -1);
        for (int right = 0; right < nums.size(); ++right) {
            for (int left = 0; left < right; ++left) {
                if (nums[right] % nums[left] == 0) {
                    if (dp[left] + 1 > dp[right]) {
                        dp[right] = dp[left] + 1;
                        prev[right] = left;
                    }
                }
            }
        }
        int idx = 0;
        for (int i = 1; i < n; ++i) {
            if (dp[i] > dp[idx]) idx = i;
        }
        vector<int> path = {nums[idx]};
        while (prev[idx] != -1) {
            path.push_back(nums[prev[idx]]);
            idx = prev[idx];
        }
        return path;
    }

};