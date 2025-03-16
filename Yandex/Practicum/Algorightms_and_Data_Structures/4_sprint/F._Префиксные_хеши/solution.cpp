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

void solution(int q, int m, const string& s) {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    vector<long long> prefix = {0};
    long long h = 0;
    for (char ch : s) {
        h = (h * q + static_cast<int>(ch)) % m;
        prefix.push_back(h);
    }

    int t;
    cin >> t;
    while (t--) {
        int l, r;
        cin >> l >> r;
        long long q_pow = mod_pow(q, r - l + 1, m);
        long long result = (prefix[r] - prefix[l - 1] * q_pow % m + m) % m;
        cout << result << '\n';
    }
}

int main() {
    int q, m;
    string s;
    cin >> q >> m;
    cin.ignore();
    getline(cin, s);
    solution(q, m, s);
    return 0;
}