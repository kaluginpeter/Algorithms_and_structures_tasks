#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


void solution() {
    /*
    Time Complexity O(N^2)
    Memory Complexity O(N^2)
    */
    string s;
    cin >> s;
    int n = s.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int i = 0; i < n; ++i) dp[i][i] = 1;

    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i <= n - len; ++i) {
            int j = i + len - 1;
            if (s[i] == s[j]) dp[i][j] = 2 + (len == 2 ? 0 : dp[i + 1][j - 1]);
            else dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
        }
    }

    int length = dp[0][n-1];
    string output;
    int i = 0, j = n - 1;
    while (i <= j) {
        if (s[i] == s[j]) {
            output += s[i];
            ++i;
            --j;
        } else {
            if (dp[i + 1][j] > dp[i][j - 1]) ++i;
            else --j;
        }
    }
    string reversed_part = output.substr(0, output.size() - (length & 1));
    reverse(reversed_part.begin(), reversed_part.end());
    output += reversed_part;
    printf("%d\n", output.size());
    cout << output << "\n";
}


int main() {
    solution();
}