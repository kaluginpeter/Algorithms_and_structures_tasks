#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<long long> A(n + 1, 0), B(n + 1, 0), C(n + 1, 0);
    A[1] = 1;
    B[1] = 1;
    C[1] = 1;
    for (int i = 2; i <= n; ++i) {
        A[i] = B[i - 1] + C[i - 1];
        B[i] = A[i - 1] + B[i - 1] + C[i - 1];
        C[i] = A[i - 1] + B[i - 1] + C[i - 1];
    }
    std::printf("%lld\n", A[n] + B[n] + C[n]);
}


int main() {
    solution();
}