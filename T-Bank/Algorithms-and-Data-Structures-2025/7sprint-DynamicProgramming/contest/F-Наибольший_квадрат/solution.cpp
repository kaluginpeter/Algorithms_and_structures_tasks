#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void solution() {
    /*
    Time Complexity O(NM)
    Memory Complexity O(NM)
    */
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> matrix (n, vector<int>(m, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            scanf("%d", &matrix[i][j]);
        }
    }
    
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    int maxSquare = 0;
    int maxSquareRow = 0, maxSquareCol = 0;
    for (int r = 1; r <= n; ++r) {
        for (int c = 1; c <= m; ++c) {
            if (!matrix[r - 1][c - 1]) continue;
            dp[r][c] = min({
                dp[r - 1][c], dp[r - 1][c - 1], dp[r][c - 1]
            }) + 1;
            if (dp[r][c] > maxSquare) {
                maxSquare = dp[r][c];
                maxSquareRow = r - dp[r][c] + 1;
                maxSquareCol = c - dp[r][c] + 1;
            }
        }
    }
    printf("%d\n%d %d\n", maxSquare, maxSquareRow, maxSquareCol);
}

int main() {
    solution();
}