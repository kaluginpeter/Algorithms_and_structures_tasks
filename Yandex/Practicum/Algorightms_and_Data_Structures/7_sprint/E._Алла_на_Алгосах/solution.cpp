#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(NM)
    Memory Complexity O(M)
    */
    int x;
    std::scanf("%d", &x);
    int k;
    std::scanf("%d", &k);
    std::vector<int> coins (k);
    for (int i = 0; i < k; ++i) std::cin >> coins[i];
    std::vector<int> dp (x + 1, 10001);
    dp[0] = 0;
    for (int exchange = 1; exchange <= x; ++exchange) {
        for (int& coin : coins) {
            if (coin > exchange) continue;
            dp[exchange] = std::min(dp[exchange], dp[exchange - coin] + 1);
        }
    }
    std::cout << (dp[x] != 10001? dp[x] : -1) << "\n";
}


int main() {
    solution();
}