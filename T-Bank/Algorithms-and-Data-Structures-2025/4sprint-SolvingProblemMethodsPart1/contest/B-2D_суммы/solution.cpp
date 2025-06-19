#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(NM)
    Memory Complexity O(NM)
    */
    int n, m, k;
    std::scanf("%d %d %d", &n, &m, &k);
    std::vector<std::vector<long long>> prefixSum (n + 1, std::vector<long long>(m + 1, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            long long num;
            std::scanf("%lld", &num);
            prefixSum[i + 1][j + 1] = prefixSum[i + 1][j] + prefixSum[i][j + 1] + num - prefixSum[i][j];
        }
    }
    for (int i = 0; i < k; ++i) {
        int y1, x1, y2, x2;
        std::scanf("%d %d %d %d", &y1, &x1, &y2, &x2);
        long long output = prefixSum[y2][x2];
        output -= prefixSum[y1 - 1][x2];
        output -= prefixSum[y2][x1 - 1];
        output += prefixSum[y1 - 1][x1 - 1];
        std::printf("%lld\n", output);
    }
}


int main() {
    solution();
}