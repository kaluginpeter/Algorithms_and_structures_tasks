#include <iostream>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    int n;
    std::scanf("%d", &n);
    if (n <= 1) {
        std::printf("1\n");
        return;
    }
    int MOD = 1000000007;
    int a = 1;
    int b = 1;
    for (int i = 2; i <= n; ++i) {
        int c = b;
        b = (a % MOD + b % MOD) % MOD;
        a = c;
    }
    std::printf("%d\n", b);
}


int main() {
    solution();
}