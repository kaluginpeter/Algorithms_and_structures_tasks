#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    */
    long long m, n;
    std::cin >> m >> n;
    std::vector<std::pair<long long, long long>> coins;
    for (int i = 0; i < n; ++i) {
        long long cost, freq;
        std::cin >> cost >> freq;
        coins.push_back({cost, freq});
    }
    std::sort(coins.begin(), coins.end());
    long long profit = 0;
    for (int idx = n - 1; idx >= 0; --idx) {
        std::pair<long long, long long>& p = coins[idx];
        int t = std::min(m, p.second);
        profit += p.first * t;
        m -= t;
        if (!m) break;
    }
    std::cout << profit << "\n";
}


int main() {
    solution();
}