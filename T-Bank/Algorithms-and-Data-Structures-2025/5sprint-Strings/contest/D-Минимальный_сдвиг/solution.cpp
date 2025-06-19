#include <iostream>
#include <string>
#include <vector>

using namespace std;

int findLexMinShift(const string& s) {
    int n = s.length();
    string t = s + s;
    vector<int> lcp(2 * n, -1);
    int k = 0;
    for (int right = 1; right < 2 * n; ++right) {
        int left = lcp[right - k - 1];
        while (left != -1 && t[right] != t[k + left + 1]) {
            if (t[right] < t[k + left + 1]) {
                k = right - left - 1;
            }
            left = lcp[left];
        }
        if (left == -1 && t[right] != t[k + left + 1]) {
            if (t[right] < t[k + left + 1]) {
                k = right;
            }
            lcp[right - k] = -1;
        } else {
            lcp[right - k] = left + 1;
        }
    }
    return k;
}


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    string s;
    cin >> s;
    int start = findLexMinShift(s);
    string result = s.substr(start) + s.substr(0, start);
    cout << result << endl;
}


int main() {
    solution();
}