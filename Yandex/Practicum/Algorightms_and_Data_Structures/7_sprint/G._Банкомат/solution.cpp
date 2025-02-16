#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(NM)
    Memory Complexity O(M)
    */
    int m;
    std::scanf("%d", &m);
    int n;
    std::scanf("%d", &n);
    std::vector<int> coins (n);
    for (int i = 0; i < n; ++i) std::cin >> coins[i];
    std::vector<int> dp (m + 1, 0);
    dp[0] = 1;
    for (int i = 0; i < n; ++i) {
        for (int exchange = coins[i]; exchange <= m; ++exchange) {
            dp[exchange] += dp[exchange - coins[i]];
        }
    }
    std::cout << dp[m] << "\n";
}


int main() {
    solution();
}