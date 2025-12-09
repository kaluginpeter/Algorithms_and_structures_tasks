# You are given an integer array nums.
#
# A special triplet is defined as a triplet of indices (i, j, k) such that:
#
# 0 <= i < j < k < n, where n = nums.length
# nums[i] == nums[j] * 2
# nums[k] == nums[j] * 2
# Return the total number of special triplets in the array.
#
# Since the answer may be large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: nums = [6,3,6]
#
# Output: 1
#
# Explanation:
#
# The only special triplet is (i, j, k) = (0, 1, 2), where:
#
# nums[0] = 6, nums[1] = 3, nums[2] = 6
# nums[0] = nums[1] * 2 = 3 * 2 = 6
# nums[2] = nums[1] * 2 = 3 * 2 = 6
# Example 2:
#
# Input: nums = [0,1,0,0]
#
# Output: 1
#
# Explanation:
#
# The only special triplet is (i, j, k) = (0, 2, 3), where:
#
# nums[0] = 0, nums[2] = 0, nums[3] = 0
# nums[0] = nums[2] * 2 = 0 * 2 = 0
# nums[3] = nums[2] * 2 = 0 * 2 = 0
# Example 3:
#
# Input: nums = [8,4,2,8,4]
#
# Output: 2
#
# Explanation:
#
# There are exactly two special triplets:
#
# (i, j, k) = (0, 1, 3)
# nums[0] = 8, nums[1] = 4, nums[3] = 8
# nums[0] = nums[1] * 2 = 4 * 2 = 8
# nums[3] = nums[1] * 2 = 4 * 2 = 8
# (i, j, k) = (1, 2, 4)
# nums[1] = 4, nums[2] = 2, nums[4] = 4
# nums[1] = nums[2] * 2 = 2 * 2 = 4
# nums[4] = nums[2] * 2 = 2 * 2 = 4
#
#
# Constraints:
#
# 3 <= n == nums.length <= 105
# 0 <= nums[i] <= 105
#
# Solution
# Python O(N) O(N) Math
mod: int = 10**9 + 7
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        overall: dict[int, int] = dict()
        prefix: dict[int, int] = dict()
        for num in nums: overall[num] = overall.get(num, 0) + 1
        output: int = 0
        for num in nums:
            target: int = num * 2
            left: int = prefix.get(target, 0)
            prefix[num] = prefix.get(num, 0) + 1
            right: int = overall.get(target, 0) - prefix.get(target, 0)
            output = (output + left * right % mod) % mod
        return output

# C++ O(N) O(N) Math
constexpr int mod = 1000000007;
class Solution {
public:
    int specialTriplets(vector<int>& nums) {
        std::unordered_map<int, int> overall, prefix;
        for (int v : nums) ++overall[v];
        int output = 0;
        for (int v : nums) {
            int target = v * 2;
            int left = prefix[target];
            ++prefix[v];
            int right = overall[target] - prefix[target];
            output = (output + (1LL * left * right % mod)) % mod;
        }

        return output;
    }
};