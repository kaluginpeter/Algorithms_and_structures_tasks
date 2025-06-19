#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<long long> nums (n + 1, 0);
    for (int i = 1; i <= n; ++i) std::scanf("%lld", &nums[i]);
    std::vector<long long> dp (n + 1, 0);
    dp[1] = nums[1];
    for (int level = 2; level <= n; ++level) {
        dp[level] = std::min(dp[level - 1], dp[level - 2]) + nums[level];
    }
    std::printf("%lld\n", dp[n]);
}


int main() {
    solution();
}