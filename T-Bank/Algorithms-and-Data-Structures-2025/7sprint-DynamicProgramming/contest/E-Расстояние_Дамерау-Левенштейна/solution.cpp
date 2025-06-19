#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <algorithm>

void solution() {
    /*
    Time Complexity O(NM)
    Memory Complexity O(NM)
    */
    std::string a, b;
    std::cin >> a >> b;
    int n = a.size(), m = b.size();
    std::vector<std::vector<std::vector<int>>> dp(n + 1, std::vector<std::vector<int>>(m + 1, std::vector<int>(2, INT_MAX)));
    for (int i = 0; i <= n; ++i) {
        dp[i][0][0] = i;
        dp[i][0][1] = i;
    }
    for (int j = 0; j <= m; ++j) {
        dp[0][j][0] = j;
        dp[0][j][1] = j;
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            dp[i][j][0] = std::min({
                dp[i-1][j-1][0] + (a[i-1] != b[j-1]),
                dp[i-1][j][0] + 1,
                dp[i][j-1][0] + 1,
            });

            if (i >= 2 && j >= 2 && a[i-1] == b[j-2] && a[i-2] == b[j-1]) {
                dp[i][j][1] = dp[i-2][j-2][0] + 1;
            } else {
                dp[i][j][1] = INT_MAX;
            }
            dp[i][j][0] = std::min(dp[i][j][0], dp[i][j][1]);
        }
    }
    std::printf("%d\n", dp[n][m][0]);
}

int main() {
    solution();
}