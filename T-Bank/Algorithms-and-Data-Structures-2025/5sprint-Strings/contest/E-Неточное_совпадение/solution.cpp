#include <iostream>
#include <string>
#include <vector>


using namespace std;


vector<int> getZFunction(string& s) {
    int n = s.size();
    vector<int> z (n, 0);
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        if (i <= r) z[i] = min(r - i + 1, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}


void solution() {
    /*
    Time Complexity O(|P| + |T|)
    Memory Complexity O(|P| + |T|)
    */
    string p, t;
    cin >> p >> t;
    string s = p + "#" + t;
    vector<int> z = getZFunction(s);
    int pLen = p.size();
    int tLen = t.size();
    vector<int> result;
    for (int i = 0; i < tLen - pLen + 1; ++i) {
        int pos = pLen + i + 1;
        int prefix = z[pos];
        if (prefix >= pLen) {
            result.push_back(i + 1);
            continue;
        }
        int mismatch = 0;
        int remaining = min(pLen - prefix, (int)s.size() - (pos + prefix));
        for (int j = 0; j < remaining; ++j) {
            if (s[prefix + j] != s[pos + prefix + j]) {
                ++mismatch;
                if (mismatch > 1) break;
            }
        }
        if (mismatch <= 1) result.push_back(i + 1);
    }
    printf("%d\n", result.size());
    if (!result.empty()) {
        for (int& num : result) printf("%d ", num);
        printf("\n");
    }
}


int main() {
    solution();
}