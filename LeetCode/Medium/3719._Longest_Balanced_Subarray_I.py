# You are given an integer array nums.
#
# A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.
#
# Return the length of the longest balanced subarray.
#
#
#
# Example 1:
#
# Input: nums = [2,5,4,3]
#
# Output: 4
#
# Explanation:
#
# The longest balanced subarray is [2, 5, 4, 3].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
# Example 2:
#
# Input: nums = [3,2,2,5,4]
#
# Output: 5
#
# Explanation:
#
# The longest balanced subarray is [3, 2, 2, 5, 4].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
# Example 3:
#
# Input: nums = [1,2,3,2]
#
# Output: 3
#
# Explanation:
#
# The longest balanced subarray is [2, 3, 2].
# It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.
#
#
# Constraints:
#
# 1 <= nums.length <= 1500
# 1 <= nums[i] <= 105
#
# Solution
# Python O(N^2) O(N) BruteForce HashSet
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        output: int = 0
        n: int = len(nums)
        for i in range(n):
            odd: set[int] = set()
            even: set[int] = set()
            for j in range(i, n):
                if nums[j] & 1: odd.add(nums[j])
                else: even.add(nums[j])
                if len(odd) == len(even): output = max(output, j - i + 1)
        return output

# C++ O(N^2) O(N) BruteForce HashSet
class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int output = 0, n = nums.size();
        for (int i = 0; i < n; ++i) {
            std::unordered_set<int> odd, even;
            for (int j = i; j < n; ++j) {
                if (nums[j] & 1) odd.insert(nums[j]);
                else even.insert(nums[j]);
                if (odd.size() == even.size()) output = std::max(output, j - i + 1);
            }
        }
        return output;
    }
};