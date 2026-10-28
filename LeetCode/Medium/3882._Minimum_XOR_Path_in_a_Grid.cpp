/*
You are given a 2D integer array grid of size m * n.

You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).

At each step, you may move either right or down.

The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.

Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

 

Example 1:

Input: grid = [[1,2],[3,4]]

Output: 6

Explanation:

There are two valid paths:

(0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
(0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6
The minimum XOR value among all valid paths is 6.

Example 2:

Input: grid = [[6,7],[5,8]]

Output: 9

Explanation:

There are two valid paths:

(0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
(0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11
The minimum XOR value among all valid paths is 9.

Example 3:

Input: grid = [[2,7,5]]

Output: 0

Explanation:

There is only one valid path:

(0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0
The XOR value of this path is 0, which is the minimum possible.

 

Constraints:

1 <= m == grid.length <= 1000
1 <= n == grid[i].length <= 1000
m * n <= 1000
0 <= grid[i][j] <= 1023​
 

*/
// Solution
// C++ O(NMK) O(NMK) Matrix Bit
class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        size_t n = grid.size(), m = grid[0].size();
        std::vector<std::vector<std::unordered_set<int>>> dp(n, std::vector<std::unordered_set<int>>(m));
        dp[0][0].insert(grid[0][0]);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (j) {
                    for (const int& num : dp[i][j - 1]) dp[i][j].insert(num ^ grid[i][j]);
                }
                if (i) {
                    for (const int& num : dp[i - 1][j]) dp[i][j].insert(num ^ grid[i][j]);
                }
            }
        }
        return *std::min_element(dp[n - 1][m - 1].begin(), dp[n - 1][m - 1].end());
    }
};

// Go O(NMK) O(NMK) Bit Matrix
func newDpState(n, upperBound int) *[][]bool {
    var state [][]bool = make([][]bool, n)
    for i := 0; i < n; i++ {
        state[i] = make([]bool, upperBound)
    }
    return &state
}
func minCost(grid [][]int) int {
    var m, n, upperBound int = len(grid), len(grid[0]), 1024
    var prevDp [][]bool = *newDpState(n, upperBound)
    for i := 0; i < m; i++ {
        var curDp [][]bool = *newDpState(n, upperBound)
        if i == 0 { curDp[0][grid[0][0]] = true }
        for j := 0; j < n; j++ {
            for target := 0; target < upperBound; target++ {
                // move from above cell
                if i > 0 && prevDp[j][target] { 
                    curDp[j][target ^ grid[i][j]] = true
                }
                // move from left cell to right
                if j > 0 && curDp[j - 1][target] {
                    curDp[j][target ^ grid[i][j]] = true
                }
            }
        }
        copy(prevDp, curDp)
        curDp = *newDpState(n, upperBound)
    }
    for target := 0; target < upperBound; target++ {
        if prevDp[n - 1][target] { return target }
    }
    return -1
}