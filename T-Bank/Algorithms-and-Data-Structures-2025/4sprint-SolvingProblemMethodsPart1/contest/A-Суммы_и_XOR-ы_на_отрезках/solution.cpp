#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<long long> prefixSum (n + 1, 0);
    std::vector<long long> prefixXOR (n + 1, 0);
    for (int i = 0; i < n; ++i) {
        long long num;
        std::scanf("%lld", &num);
        prefixSum[i + 1] = prefixSum[i] + num;
        prefixXOR[i + 1] = prefixXOR[i] ^ num;
    }
    int m;
    std::scanf("%d", &m);
    for (int i = 0; i < m; ++i) {
        int op, l, r;
        std::scanf("%d %d %d", &op, &l, &r);
        if (op == 1) std::printf("%lld\n", prefixSum[r] - prefixSum[l - 1]);
        else std::printf("%lld\n", prefixXOR[r] ^ prefixXOR[l - 1]);
    }
}


int main() {
    solution();
}