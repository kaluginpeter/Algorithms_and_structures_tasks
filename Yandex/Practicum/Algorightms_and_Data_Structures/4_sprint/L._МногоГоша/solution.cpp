#include <iostream>
#include <string>
#include <unordered_map>
#include <tuple>
#include <functional>

using namespace std;

const long long MOD1 = 100000003;
const long long MOD2 = 100000019;
const long long MOD3 = 100000037;
const long long q1 = 100000009;
const long long q2 = 100000007;
const long long q3 = 100000021;

struct TupleHash {
    template <class T>
    size_t operator()(const tuple<T, T, T>& t) const {
        auto hash1 = hash<T>()(get<0>(t));
        auto hash2 = hash<T>()(get<1>(t));
        auto hash3 = hash<T>()(get<2>(t));
        return hash1 ^ (hash2 << 1) ^ (hash3 << 2);
    }
};


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n, k;
    std::cin >> n >> k;
    std::string L;
    std::cin >> L;
    bool seen = false;
    std::unordered_map<
        std::tuple<long long, long long, long long>,
        std::pair<int, int>,
        TupleHash
    > hashmap;
    long long cur_hash1 = 0, cur_hash2 = 0, cur_hash3 = 0;
    long long q_pow_k1 = 1, q_pow_k2 = 1, q_pow_k3 = 1;

    for (int i = 0; i < n; ++i) {
        q_pow_k1 = (q_pow_k1 * q1) % MOD1;
        q_pow_k2 = (q_pow_k2 * q2) % MOD2;
        q_pow_k3 = (q_pow_k3 * q3) % MOD3;
    }

    for (int i = 0; i < L.size(); ++i) {
        cur_hash1 = (cur_hash1 * q1 + (L[i] - 'a' + 1)) % MOD1;
        cur_hash2 = (cur_hash2 * q2 + (L[i] - 'a' + 1)) % MOD2;
        cur_hash3 = (cur_hash3 * q3 + (L[i] - 'a' + 1)) % MOD3;
        if (i >= n - 1) {
            if (i >= n) {
                cur_hash1 = (cur_hash1 - (L[i - n] - 'a' + 1) * q_pow_k1 % MOD1 + MOD1) % MOD1;
                cur_hash2 = (cur_hash2 - (L[i - n] - 'a' + 1) * q_pow_k2 % MOD2 + MOD2) % MOD2;
                cur_hash3 = (cur_hash3 - (L[i - n] - 'a' + 1) * q_pow_k3 % MOD3 + MOD3) % MOD3;
            }
            std::tuple<long long, long long, long long> triplet = {cur_hash1, cur_hash2, cur_hash3};
            if (!hashmap.count(triplet)) {
                hashmap[triplet] = {0, i - n + 1};
            }
            ++hashmap[triplet].first;
            if (hashmap[triplet].first == k) {
                if (seen) {
                    std::cout << " ";
                }
                std::cout << hashmap[triplet].second;
                seen = true;
            }
        }
    }
}

int main() {
    solution();
}