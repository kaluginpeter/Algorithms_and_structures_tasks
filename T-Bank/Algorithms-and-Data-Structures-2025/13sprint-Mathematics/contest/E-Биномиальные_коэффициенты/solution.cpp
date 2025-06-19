#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;
const int MAX = 1e6;

vector<long long> fact(MAX + 1);
vector<long long> inv_fact(MAX + 1);

long long power(long long x, long long y, long long p) {
    long long output = 1;
    x = x % p;
    while (y > 0) {
        if (y & 1) output = (output * x) % p;
        y = y >> 1;
        x = (x * x) % p;
    }
    return output;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i <= MAX; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv_fact[MAX] = power(fact[MAX], MOD - 2, MOD);
    for (int i = MAX - 1; i >= 0; --i) inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;
}

long long binomialCoefficient(int n, int k) {
    if (k < 0 || k > n) return 0;
    return (fact[n] * inv_fact[k] % MOD) * inv_fact[n - k] % MOD;
}


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n, k;
    std::scanf("%d %d\n", &n, &k);
    precompute();
    std::printf("%lld\n", binomialCoefficient(n, k));
}


int main() {
    solution();
}