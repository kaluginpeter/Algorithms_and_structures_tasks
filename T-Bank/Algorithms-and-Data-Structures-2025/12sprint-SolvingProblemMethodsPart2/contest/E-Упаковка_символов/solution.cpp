#include <iostream>
#include <vector>
#include <string>
#include <climits>

using namespace std;


void solution() {
    /*
    Time Complexity O(N^3)
    Memory Complexity O(N^3)
    */
    string s;
    std::cin >> s;
    int n = s.size();
    vector<vector<string>> dp(n, vector<string>(n));
    for (int i = 0; i < n; ++i) dp[i][i] = s[i];

    for (int length = 2; length <= n; ++length) {
        for (int left = 0; left <= n - length; ++left) {
            int right = left + length - 1;
            dp[left][right] = s.substr(left, length);

            for (int k = left; k < right; ++k) {
                string candidate = dp[left][k] + dp[k + 1][right];
                if (candidate.size() < dp[left][right].size()) dp[left][right] = candidate;
            }

            string sub = s.substr(left, length);
            int sub_len = sub.size();
            for (int k = 1; k <= sub_len / 2; ++k) {
                if (sub_len % k != 0) continue;
                bool is_repeat = true;
                for (int l = k; l < sub_len; ++l) {
                    if (sub[l] != sub[l % k]) {
                        is_repeat = false;
                        break;
                    }
                }
                if (is_repeat) {
                    string compressed = to_string(sub_len / k) + "(" + dp[left][left + k - 1] + ")";
                    if (compressed.size() < dp[left][right].size()) dp[left][right] = compressed;
                }
            }
        }
    }
    cout << dp[0][n - 1] << "\n";
}


int main() {
    solution();
}