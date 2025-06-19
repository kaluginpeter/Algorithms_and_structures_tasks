#include <iostream>
#include <string>
#include <vector>


using namespace std;


void solution() {
    /*
    Time Complexity O(Q(N+L))
    Memory Complexity O(N + L)
    */
    string text;
    cin >> text;
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        string pattern;
        cin >> pattern;
        string S = pattern + "#" + text;
        vector<int> lcp (pattern.size());
        int freq = 0;
        vector<int> positions;
        int prevLcp = 0;
        for (int idx = 1; idx < S.size(); ++idx) {
            int k = prevLcp;
            while (k && S[k] != S[idx]) k = lcp[k - 1];
            if (S[k] == S[idx]) ++k;
            prevLcp = k;
            if (idx < pattern.size()) lcp[idx] = k;
            if (k == pattern.size()) {
                ++freq;
                positions.push_back(idx - 2 * pattern.size());
            }
        }
        printf("%d", freq);
        for (int& pos : positions) printf(" %d", pos);
        printf("\n");
    }
}


int main() {
    solution();
}