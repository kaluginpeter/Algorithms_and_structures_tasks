# Given two arrays nums1 and nums2.
#
# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
#
# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).
#
#
#
# Example 1:
#
# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18
# Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
# Their dot product is (2*3 + (-2)*(-6)) = 18.
# Example 2:
#
# Input: nums1 = [3,-2], nums2 = [2,-6,7]
# Output: 21
# Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
# Their dot product is (3*7) = 21.
# Example 3:
#
# Input: nums1 = [-1,-1], nums2 = [1,1]
# Output: -1
# Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
# Their dot product is -1.
#
#
# Constraints:
#
# 1 <= nums1.length, nums2.length <= 500
# -1000 <= nums1[i], nums2[i] <= 1000
# Solution
# Python O(NM) O(max(N, M) + N + M) DynamicProgramming Memoization
bound: int = float('-inf')
class Solution:
    x: list[int]
    y: list[int]
    @cache
    def dp(self, i: int, j: int, n: int, m: int) -> int:
        if i == n or j == m: return bound
        take: int = self.x[i] * self.y[j]
        output: int = max(
            take + self.dp(i + 1, j + 1, n, m),
            take,
            self.dp(i + 1, j, n, m),
            self.dp(i, j + 1, n, m)
        )
        return output

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        self.x = nums1
        self.y = nums2
        return self.dp(0, 0, (n := len(nums1)), (m := len(nums2)))


# C++ O(NM) O(max(N, M) + N + M) Memoization DynamicProgramming
constexpr int bound = INT32_MIN / 2;
class Solution {
public:
    int dp(int i, int j, const int& n, const int& m, const std::vector<int>& x, const std::vector<int>& y, std::vector<std::vector<int>>& memo) {
        if (i == n || j == m) return bound;
        if (memo[i][j] != bound) return memo[i][j];
        int take = x[i] * y[j];
        int output = max({
            take + dp(i + 1, j + 1, n, m, x, y, memo),
            take,
            dp(i + 1, j, n, m, x, y, memo),
            dp(i, j + 1, n, m, x, y, memo)
        });
        return memo[i][j] = output;
    }
    int maxDotProduct(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        std::vector<std::vector<int>> memo(n, std::vector<int>(m, bound));
        return dp(0, 0, n, m, nums1, nums2, memo);
    }
};