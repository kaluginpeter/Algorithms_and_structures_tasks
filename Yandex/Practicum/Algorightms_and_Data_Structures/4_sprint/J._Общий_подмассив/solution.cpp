#include <iostream>
#include <vector>
#include <unordered_set>
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

bool has_common_substring_with_length_k(int k, const vector<int>& A, const vector<int>& B) {
    if (k == 0) return true;
    if (A.size() < k || B.size() < k) return false;

    unordered_set<tuple<long long, long long, long long>, TupleHash> pool;
    long long cur_hash1 = 0, cur_hash2 = 0, cur_hash3 = 0;
    long long q_pow_k1 = 1, q_pow_k2 = 1, q_pow_k3 = 1;

    for (int i = 0; i < k; ++i) {
        q_pow_k1 = (q_pow_k1 * q1) % MOD1;
        q_pow_k2 = (q_pow_k2 * q2) % MOD2;
        q_pow_k3 = (q_pow_k3 * q3) % MOD3;
    }

    for (int idx = 0; idx < A.size(); ++idx) {
        cur_hash1 = (cur_hash1 * q1 + A[idx] + MOD1) % MOD1;
        cur_hash2 = (cur_hash2 * q2 + A[idx] + MOD2) % MOD2;
        cur_hash3 = (cur_hash3 * q3 + A[idx] + MOD3) % MOD3;

        if (idx >= k - 1) {
            if (idx >= k) {
                cur_hash1 = (cur_hash1 - A[idx - k] * q_pow_k1 + MOD1) % MOD1;
                cur_hash2 = (cur_hash2 - A[idx - k] * q_pow_k2 + MOD2) % MOD2;
                cur_hash3 = (cur_hash3 - A[idx - k] * q_pow_k3 + MOD3) % MOD3;
            }
            pool.insert({cur_hash1, cur_hash2, cur_hash3});
        }
    }

    cur_hash1 = 0;
    cur_hash2 = 0;
    cur_hash3 = 0;
    for (int idx = 0; idx < B.size(); ++idx) {
        cur_hash1 = (cur_hash1 * q1 + B[idx] + MOD1) % MOD1;
        cur_hash2 = (cur_hash2 * q2 + B[idx] + MOD2) % MOD2;
        cur_hash3 = (cur_hash3 * q3 + B[idx] + MOD3) % MOD3;

        if (idx >= k - 1) {
            if (idx >= k) {
                cur_hash1 = (cur_hash1 - B[idx - k] * q_pow_k1 + MOD1) % MOD1;
                cur_hash2 = (cur_hash2 - B[idx - k] * q_pow_k2 + MOD2) % MOD2;
                cur_hash3 = (cur_hash3 - B[idx - k] * q_pow_k3 + MOD3) % MOD3;
            }
            if (pool.count({cur_hash1, cur_hash2, cur_hash3})) {
                return true;
            }
        }
    }

    return false;
}

void solution() {
    /*
    Time Complexity O( (NM)log(min(N, m)) )
    Memory Complexity O(max(N, M))
    */
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    int m;
    cin >> m;
    vector<int> B(m);
    for (int i = 0; i < m; i++) {
        cin >> B[i];
    }

    int left = 0, right = min(n, m);
    int max_common = 0;
    while (left <= right) {
        int middle = left + (right - left) / 2;
        if (has_common_substring_with_length_k(middle, A, B)) {
            max_common = middle;
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }
    cout << max_common << endl;
}

int main() {
    solution();
    return 0;
}
