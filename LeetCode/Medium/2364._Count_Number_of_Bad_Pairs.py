# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
#
# Return the total number of bad pairs in nums.
#
#
#
# Example 1:
#
# Input: nums = [4,1,3,3]
# Output: 5
# Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
# The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
# The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
# The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
# The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
# There are a total of 5 bad pairs, so we return 5.
# Example 2:
#
# Input: nums = [1,2,3,4,5]
# Output: 0
# Explanation: There are no bad pairs.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# Solution
# Python O(N) O(N) HashMap Counting
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n: int = len(nums)
        hashmap: dict[int, int] = dict()
        valid: int = 0
        for idx in range(n):
            diff: int = nums[idx] - idx
            hashmap[diff] = hashmap.get(diff, 0) + 1
            valid += hashmap[diff]
        return n * (n + 1) // 2 - valid

# C++ O(N) O(N) HashMap Counting
class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        int n = nums.size();
        std::unordered_map<int, int> hashmap;
        long long valid = 0;
        for (int i = 0; i < n; ++i) {
            int diff = nums[i] - i;
            ++hashmap[diff];
            valid += hashmap[diff];
        }
        return (long long)n * (n + 1) / 2 - valid;
    }
};