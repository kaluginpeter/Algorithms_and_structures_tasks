#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(NM)
    Memory Complexity O(N)
    */
    int MOD = 1000000007;
    int n, k;
    std::cin >> n >> k;
    std::vector<int> dp (n + 1, 0);
    dp[1] = 1;
    for (int i = 2; i <= n; ++i) {
        for (int prev = std::max(1, i - k); prev < i; ++prev) {
            dp[i] = (dp[i] % MOD + dp[prev] % MOD) % MOD;
        }
    }
    std::cout << dp[n] << "\n";
}


int main() {
    solution();
}