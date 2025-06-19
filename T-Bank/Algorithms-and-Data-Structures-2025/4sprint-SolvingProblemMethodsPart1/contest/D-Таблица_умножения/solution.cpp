#include <iostream>


long long getLE(long long& middle, long long& n) {
    long long le = 0;
    for (long long num = 1; num <= n; ++num) {
        le += std::min(middle / num, n);
    }
    return le;
}


void solution() {
    /*
    Time Complexity O(Nlog(N^2))
    Memory Complexity O(1)
    */
    long long n, k;
    std::scanf("%lld %lld", &n, &k);
    long long left = 1;
    long long right = n * n;
    while (left <= right) {
        long long middle = left + (right - left) / 2;
        long long lessThanOrEqual = getLE(middle, n);
        if (lessThanOrEqual < k) {
            left = middle + 1;
        } else right = middle - 1;
    }
    std::printf("%lld\n", left);
}


int main() {
    solution();
}