#include <iostream>


long long gcd(long long x, long long y) {
    if (x == 0) return y;
    return gcd(y % x, x);
}



long long lcm(long long x, long long y) {
    return x * y / gcd(x, y);
}


void solution() {
    /*
    Time Complexity O(log(N))
    Memory Complexity O(log(N))
    */
    long long n, k;
    std::scanf("%lld %lld", &n, &k);
    std::printf("%lld\n", lcm(n, k));
}


int main() {
    solution();
}