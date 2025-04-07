# You are given an m x n integer matrix mat and an integer target.
#
# Choose one integer from each row in the matrix such that the absolute difference between target and the sum of the chosen elements is minimized.
#
# Return the minimum absolute difference.
#
# The absolute difference between two numbers a and b is the absolute value of a - b.
#
#
#
# Example 1:
#
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
# Output: 0
# Explanation: One possible choice is to:
# - Choose 1 from the first row.
# - Choose 5 from the second row.
# - Choose 7 from the third row.
# The sum of the chosen elements is 13, which equals the target, so the absolute difference is 0.
# Example 2:
#
#
# Input: mat = [[1],[2],[3]], target = 100
# Output: 94
# Explanation: The best possible choice is to:
# - Choose 1 from the first row.
# - Choose 2 from the second row.
# - Choose 3 from the third row.
# The sum of the chosen elements is 6, and the absolute difference is 94.
# Example 3:
#
#
# Input: mat = [[1,2,9,8,7]], target = 6
# Output: 1
# Explanation: The best choice is to choose 7 from the first row.
# The absolute difference is 1.
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 70
# 1 <= mat[i][j] <= 70
# 1 <= target <= 800
# Solution
# Python O(NMK) O(K) DynamicProgramming Matrix
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        sums: set[int] = {0}
        for row in mat:
            sums = {prev_sum + num for num in row for prev_sum in sums}
        return min(abs(target - mat_sum) for mat_sum in sums)

# C++ O(NMK) O(K) DynamicProgramming Matrix
class Solution {
public:
    int minimizeTheDifference(vector<vector<int>>& mat, int target) {
        int n = mat.size(), m = mat[0].size(), K = 4901;
        vector<bool> prevDp (K, false);
        vector<bool> curDp (K, false);
        prevDp[0] = true;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                for (int k = K - mat[i][j] - 1; k >= 0; --k) {
                    if (prevDp[k]) {
                        curDp[k + mat[i][j]] = true;;
                    }
                }
            }
            prevDp = curDp;
            curDp = vector<bool> (K, false);
        }
        int minDiff = INT32_MAX;
        for (int k = 0; k < K; ++k) {
            if (prevDp[k]) {
                int diff = abs(target - k);
                minDiff = min(minDiff, diff);
            }
        }
        return minDiff;
    }
};