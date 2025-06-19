#include <iostream>
#include <string>
#include <vector>

using namespace std;


long long mod_pow(long long base, long long exp, long long mod) {
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
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    const long long q = 100000009;
    const long long m = 100000003;
    string pattern;
    cin >> pattern;
    int n = pattern.size();
    vector<long long> prefixSum = {0};
    long long h = 0;
    for (char ch : pattern) {
        h = (h * q + static_cast<int>(ch)) % m;
        prefixSum.push_back(h);
    }
    int M;
    scanf("%d", &M);
    for (int i = 0; i < M; ++i) {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        if ((b - a + 1) != (d - c + 1)) {
            printf("No\n");
            continue;
        }
        long long q_pow = mod_pow(q, b - a + 1, m);
        long long x = (prefixSum[b] - prefixSum[a - 1] * q_pow % m + m) % m;
        q_pow = mod_pow(q, d - c + 1, m);
        long long y = (prefixSum[d] - prefixSum[c - 1] * q_pow % m + m) % m;
        cout << (x == y? "Yes" : "No") << "\n";
        
    }
}


int main() {
    solution();
}