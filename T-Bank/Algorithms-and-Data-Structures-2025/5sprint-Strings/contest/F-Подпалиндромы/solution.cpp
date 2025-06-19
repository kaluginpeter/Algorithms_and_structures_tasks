#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


void solution() {
    /*
    Time Complexity O(|S|)
    Memory Complexity O(|S|)
    */
    string s;
    cin >> s;
    string transformed = "^#";
    for (char c : s) {
        transformed += c;
        transformed += '#';
    }
    transformed += '$';
    int n = transformed.size();
    vector<int> p(n, 0);
    int center = 0, right = 0;
    for (int i = 1; i < n - 1; ++i) {
        if (i < right) {
            p[i] = min(right - i, p[2 * center - i]);
        }
        while (i + p[i] + 1 < n && i - p[i] - 1 >= 0 &&
               transformed[i + p[i] + 1] == transformed[i - p[i] - 1]) {
            p[i]++;
        }
        if (i + p[i] > right) {
            center = i;
            right = i + p[i];
        }
    }

    long long total = 0;
    for (int length : p) total += (length + 1) / 2;
    printf("%lld\n", total);
}


int main() {
    solution();
}