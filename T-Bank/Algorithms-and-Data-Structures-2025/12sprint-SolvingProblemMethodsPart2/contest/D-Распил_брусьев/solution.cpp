#include <iostream>
#include <vector>
#include <climits>

using namespace std;


void solution() {
    /*
    Time Complexity O(N^2)
    Memory Complexity O(N^2)
    */
    int L, N;
    scanf("%d %d", &L, &N);
    vector<int> cuts(N + 2);
    cuts[0] = 0;
    for (int i = 1; i <= N; ++i) scanf("%d", &cuts[i]);
    cuts[N + 1] = L;
    vector<vector<int>> dp(N + 2, vector<int>(N + 2, 0));
    for (int len = 2; len <= N + 1; ++len) {
        for (int left = 0; left <= N + 1 - len; ++left) {
            int right = left + len;
            dp[left][right] = INT_MAX;
            for (int k = left + 1; k < right; ++k) {
                dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + cuts[right] - cuts[left]);
            }
        }
    }
    printf("%d\n", dp[0][N + 1]);
}


int main() {
    solution();
}