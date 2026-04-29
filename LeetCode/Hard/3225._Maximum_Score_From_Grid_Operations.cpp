/*
You are given a 2D matrix grid of size n x n. Initially, all cells of the grid are colored white. In one operation, you can select any cell of indices (i, j), and color black all the cells of the jth column starting from the top row down to the ith row.

The grid score is the sum of all grid[i][j] such that cell (i, j) is white and it has a horizontally adjacent black cell.

Return the maximum score that can be achieved after some number of operations.



Example 1:

Input: grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]

Output: 11

Explanation:


In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is grid[3][0] + grid[1][2] + grid[3][3] which is equal to 11.

Example 2:

Input: grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]

Output: 94

Explanation:


We perform operations on 1, 2, and 3 down to rows 1, 4, and 0, respectively. The score of the resulting grid is grid[0][0] + grid[1][0] + grid[2][1] + grid[4][1] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] + grid[0][4] which is equal to 94.



Constraints:

1 <= n == grid.length <= 100
n == grid[i].length
0 <= grid[i][j] <= 109
*/
// Solution
// C++ O(N^3) O(N^3) DynamicProgramming
class Solution {
public:
    long long maximumScore(vector<vector<int>>& grid) {
        size_t n = grid[0].size();
        if (n == 1) return 0;
        vector<vector<std::vector<long long>>> dp(n, vector<std::vector<long long>>(n + 1, std::vector<long long>(n + 1, 0)));
        vector<std::vector<long long>> prevMax(n + 1, std::vector<long long>(n + 1, 0));
        vector<std::vector<long long>> prevSuffixMax(n + 1, std::vector<long long>(n + 1, 0));
        vector<std::vector<long long>> colSum(n, std::vector<long long>(n + 1, 0));
        for (int c = 0; c < n; ++c) {
            for (int r = 1; r <= n; ++r) colSum[c][r] = colSum[c][r - 1] + grid[r - 1][c];
        }
        for (int i = 1; i < n; ++i) {
            for (int currH = 0; currH <= n; ++currH) {
                for (int prevH = 0; prevH <= n; ++prevH) {
                    if (currH <= prevH) {
                        long long extraScore = colSum[i][prevH] - colSum[i][currH];
                        dp[i][currH][prevH] = std::max(dp[i][currH][prevH], prevSuffixMax[prevH][0] + extraScore);
                    } else {
                        long long extraScore = colSum[i - 1][currH] - colSum[i - 1][prevH];
                        dp[i][currH][prevH] = std::max({dp[i][currH][prevH], prevSuffixMax[prevH][currH], prevMax[prevH][currH] + extraScore});
                    }
                }
            }
            for (int currH = 0; currH <= n; ++currH) {
                prevMax[currH][0] = dp[i][currH][0];
                for (int prevH = 1; prevH <= n; ++prevH) {
                    long long penalty = (prevH > currH) ? (colSum[i][prevH] - colSum[i][currH]) : 0;
                    prevMax[currH][prevH] = std::max(prevMax[currH][prevH - 1], dp[i][currH][prevH] - penalty);
                }
                prevSuffixMax[currH][n] = dp[i][currH][n];
                for (int prevH = n - 1; prevH >= 0; --prevH) {
                    prevSuffixMax[currH][prevH] = std::max(prevSuffixMax[currH][prevH + 1], dp[i][currH][prevH]);
                }
            }
        }
        long long output = 0;
        for (int k = 0; k <= n; ++k) {
            output = std::max({output, dp[n - 1][n][k], dp[n - 1][0][k]});
        }
        return output;
    }
};