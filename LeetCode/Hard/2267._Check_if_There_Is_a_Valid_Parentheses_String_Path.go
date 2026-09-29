/*
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:

The path starts from the upper left cell (0, 0).
The path ends at the bottom-right cell (m - 1, n - 1).
The path only ever moves down or right.
The resulting parentheses string formed by the path is valid.
Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.

 

Example 1:


Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.
Example 2:


Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is either '(' or ')'.
*/
// Solution
// Go O(NMK) O(NMK) DynamicProgramming
func hasValidPath(grid [][]byte) bool {
    if rune(grid[0][0]) == ')' { return false }
    var n, m int = len(grid), len(grid[0])
    var k int = (n + m + 1) >> 1
    var dp [][][]bool = make([][][]bool, n + 1)
    for i := 0; i <= n; i++ {
        dp[i] = make([][]bool, m + 1)
        for j := 0; j <= m; j++ {
            dp[i][j] = make([]bool, k + 1)
        }
    }
    dp[0][1][0] = true
    dp[1][0][0] = true
    for i := 1; i <= n; i++ {
        for j := 1; j <= m; j++ {
            var cost int = 1
            if rune(grid[i - 1][j - 1]) == ')' { cost = -1 }
            for target := min(k, i + j + 1); target >= 0; target-- {
                if target - cost > k || target - cost < 0 { continue }
                dp[i][j][target] = dp[i][j][target] || dp[i - 1][j][target - cost] || dp[i][j - 1][target - cost]
            }
        }
    }
    return dp[n][m][0]
}

// C++ O(NMK) O(NMK) DynamicProgramming
class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        if (grid[0][0] == ')') return false;
        int n = grid.size(), m = grid[0].size(), k = (n + m + 1) >> 1;
        std::vector<std::vector<std::vector<bool>>> dp(n + 1, std::vector<std::vector<bool>>(m + 1, std::vector<bool>(k + 1, false)));
        dp[0][1][0] = true;
        dp[1][0][0] = true;
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                int cost = (grid[i - 1][j - 1] == ')' ? -1 : 1);
                for (int target = std::min(k, i + j + 1); target >= 0; --target) {
                    if (target - cost > k || target - cost < 0) continue;
                    dp[i][j][target] = dp[i - 1][j][target - cost] || dp[i][j - 1][target - cost];
                }
            }
        }
        return dp[n][m][0];
    }
};