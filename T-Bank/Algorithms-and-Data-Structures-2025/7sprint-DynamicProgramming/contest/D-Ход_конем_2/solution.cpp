#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(NM)
    Memory Complexity O(NM)
    */
    int n, m;
    std::scanf("%d %d", &n, &m);
    std::vector<std::vector<long long>> dp (n, std::vector<long long>(m, 0));
    dp[0][0] = 1;
    std::vector<std::pair<int, int>> moves = {
        {-1, -2}, {-2, -1}, {1, -2}, {-2, 1}
    };
    int mainR = 0;
    while (mainR < n) {
        int r = mainR;
        int c = 0;
        while (r >= 0 && c < m) {
            for (std::pair<int, int>& move : moves) {
                int nextR = r + move.first;
                int nextC = c + move.second;
                if (nextR >= 0 && nextR < n && nextC >= 0 and nextC < m) {
                    dp[r][c] += dp[nextR][nextC];
                }
            }
            --r;
            ++c;
        }
        ++mainR;
    }
    int mainC = 1;
    while (mainC < m) {
        int r = n - 1;
        int c = mainC;
        while (r >= 0 && c < m) {
            for (std::pair<int, int>& move : moves) {
                int nextR = r + move.first;
                int nextC = c + move.second;
                if (nextR >= 0 && nextR < n && nextC >= 0 and nextC < m) {
                    dp[r][c] += dp[nextR][nextC];
                }
            }
            --r;
            ++c;
        }
        ++mainC;
    }
    std::printf("%lld\n", dp[n - 1][m - 1]);
}


int main() {
    solution();
}