#include <iostream>
#include <vector>
#include <deque>
#include <climits>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n, k;
    std::scanf("%d %d", &n, &k);
    std::vector<long long> dp(n + 1, LLONG_MAX);
    dp[1] = 0;
    std::vector<int> nums = {0, 0};
    for (int i = 0; i < n - 2; ++i) {
        int num;
        std::scanf("%d", &num);
        nums.push_back(num);
    }
    nums.push_back(0);
    std::deque<int> q;
    q.push_back(1);
    std::vector<int> prev (n + 1, -1);
    for (int i = 2; i <= n; ++i) {
        if (!q.empty() && q.front() < i - k) q.pop_front();
        dp[i] = dp[q.front()] + nums[i];
        prev[i] = q.front();
        while (!q.empty() && dp[q.back()] <= dp[i]) q.pop_back();
        q.push_back(i);
    }
    std::vector<int> path;
    int i = n;
    while (prev[i] != -1) {
        path.push_back(prev[i]);
        i = prev[i];
    }
    
    std::printf("%lld\n%d\n", dp[n], path.size());
    for (int j = path.size() - 1; j >= 0; --j) std::printf("%d ", path[j]);
    std::printf("%d\n", n);
}


int main() {
    solution();
}