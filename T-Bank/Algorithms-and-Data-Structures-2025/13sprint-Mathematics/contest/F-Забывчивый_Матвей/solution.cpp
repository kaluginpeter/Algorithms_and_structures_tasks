#include <iostream>


long long power(long long base, long long exp, long long mod) {
    long long output = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) output = (output * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return output;
}


long long modInverse(long long n, long long mod) {
    return power(n, mod - 2, mod);
}


void solution() {
    /*
    Time Complexity O(logN)
    Memory Complexity O(1)
    */
    long long N, M, K, MOD;
    std::scanf("%lld %lld %lld %lld", &N, &M, &K, &MOD);
    long long mPowN = power(M, N, MOD);
    long long kInverse = modInverse(K, MOD);
    long long finalTime = (mPowN * kInverse) % MOD;
    std::printf("%lld\n", finalTime);
}


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    solution();
}