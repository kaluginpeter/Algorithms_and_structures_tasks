#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool isMatchingPair(char a, char b) {
    return (a == '(' && b == ')') || (a == '[' && b == ']') || (a == '{' && b == '}');
}

void solution() {
    /*
    Time Complexity O(N**3)
    Memory Complexity O(N**3)
    */
    string s;
    cin >> s;
    int n = s.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    vector<vector<string>> path(n, vector<string>(n, ""));

    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i <= n - len; ++i) {
            int j = i + len - 1;
            if (isMatchingPair(s[i], s[j])) {
                if (len == 2) {
                    dp[i][j] = 2;
                    path[i][j] = string(1, s[i]) + string(1, s[j]);
                } else {
                    dp[i][j] = 2 + dp[i+1][j-1];
                    path[i][j] = string(1, s[i]) + path[i+1][j-1] + string(1, s[j]);
                }
            }
            for (int k = i; k < j; ++k) {
                if (dp[i][j] < dp[i][k] + dp[k+1][j]) {
                    dp[i][j] = dp[i][k] + dp[k+1][j];
                    path[i][j] = path[i][k] + path[k+1][j];
                }
            }
        }
    }
    cout << path[0][n-1] << endl;
}

int main() {
    solution();
}