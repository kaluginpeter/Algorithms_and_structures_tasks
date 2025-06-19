#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

long long modPow(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

void solution() {
    /*
    Time Complexity O(|a| + |b|)
    Memory Complexity O(|a| + |b|)
    */
    string a, b;
    cin >> a >> b;
    int k = b.size();
    if (k > a.size()) {
        printf("0\n");
        return;
    }
    const long long q1 = 100000009;
    const long long m1 = 100000003;
    const long long q2 = 100000007;
    const long long m2 = 100000019;
    unordered_map<long long, unordered_map<long long, int>> hashmap;
    vector<long long> prefixSum1 = {0}, prefixSum2 = {0};
    long long h1 = 0, h2 = 0;
    for (int i = 0; i < k * 2 - 1; ++i) {
        h1 = (h1 * q1 + static_cast<int>(b[i % k])) % m1;
        h2 = (h2 * q2 + static_cast<int>(b[i % k])) % m2;
        if (i + 1 >= k) {
            if (i >= k) {
                long long qPow1 = modPow(q1, k, m1);
                long long qPow2 = modPow(q2, k, m2);
                long long hashCode1 = (h1 - prefixSum1[i - k + 1] * qPow1 % m1 + m1) % m1;
                long long hashCode2 = (h2 - prefixSum2[i - k + 1] * qPow2 % m2 + m2) % m2;
                ++hashmap[hashCode1][hashCode2];
            } else ++hashmap[h1][h2];
        }
        prefixSum1.push_back(h1);
        prefixSum2.push_back(h2);
    }
    long long output = 0;
    prefixSum1 = {0};
    prefixSum2 = {0};
    h1 = 0, h2 = 0;
    for (int i = 0; i < a.size(); ++i) {
        h1 = (h1 * q1 + static_cast<int>(a[i])) % m1;
        h2 = (h2 * q2 + static_cast<int>(a[i])) % m2;
        if (i + 1 >= k) {
            if (i >= k) {
                long long qPow1 = modPow(q1, k, m1);
                long long qPow2 = modPow(q2, k, m2);
                long long hashCode1 = (h1 - prefixSum1[i - k + 1] * qPow1 % m1 + m1) % m1;
                long long hashCode2 = (h2 - prefixSum2[i - k + 1] * qPow2 % m2 + m2) % m2;
                if (hashmap.count(hashCode1) && hashmap[hashCode1].count(hashCode2)) ++output;
            } else if (hashmap.count(h1) && hashmap[h1].count(h2)) ++output;
        }
        prefixSum1.push_back(h1);
        prefixSum2.push_back(h2);
    }
    printf("%lld\n", output);
}

int main() {
    solution();
}