#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <random>

using namespace std;

vector<long long> generateRandomWeights(int maxNum) {
    vector<long long> weights(maxNum + 1);
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<long long> dist(1, 1e18);
    for (int i = 1; i <= maxNum; ++i) {
        weights[i] = dist(gen);
    }
    return weights;
}

struct pair_hash {
    template <class T1, class T2>
    size_t operator() (const pair<T1, T2>& p) const {
        auto hash1 = hash<T1>{}(p.first);
        auto hash2 = hash<T2>{}(p.second);
        return hash1 ^ (hash2 << 1);
    }
};

unordered_map<pair<long long, long long>, unordered_set<int>, pair_hash> generateSubstrings(const vector<int>& arr, const vector<long long>& weights1, const vector<long long>& weights2) {
    unordered_map<pair<long long, long long>, unordered_set<int>, pair_hash> hashMap;
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        long long hash1 = 0;
        long long hash2 = 0;
        for (int j = i; j < n; ++j) {
            hash1 += weights1[arr[j]];
            hash2 += weights2[arr[j]];
            int len = j - i + 1;
            hashMap[{hash1, hash2}].insert(len);
        }
    }
    return hashMap;
}

void solution() {
    /*
    Time Complexity O(N**2 + M**2)
    Memory Complexity O(N**2)
    */
    int n, m;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cin >> m;
    vector<int> b(m);
    for (int i = 0; i < m; ++i) cin >> b[i];

    const int maxNum = 1e5;
    auto weights1 = generateRandomWeights(maxNum);
    auto weights2 = generateRandomWeights(maxNum);

    auto hashMap = generateSubstrings(a, weights1, weights2);

    vector<long long> prefixSum1(m + 1, 0);
    vector<long long> prefixSum2(m + 1, 0);
    for (int i = 0; i < m; ++i) {
        prefixSum1[i + 1] = prefixSum1[i] + weights1[b[i]];
        prefixSum2[i + 1] = prefixSum2[i] + weights2[b[i]];
    }

    int maxLen = 0;

    for (int i = 0; i < m; ++i) {
        for (int j = i + 1; j <= m; ++j) {
            long long hashCode1 = prefixSum1[j] - prefixSum1[i];
            long long hashCode2 = prefixSum2[j] - prefixSum2[i];
            int len = j - i;
            if (hashMap.count({hashCode1, hashCode2}) && hashMap[{hashCode1, hashCode2}].count(len)) {
                maxLen = max(maxLen, len);
            }
        }
    }

    cout << maxLen << "\n";
}


int main() {
    solution();
}