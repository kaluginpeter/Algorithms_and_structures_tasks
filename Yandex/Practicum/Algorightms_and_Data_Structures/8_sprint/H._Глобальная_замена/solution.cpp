#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    std::string s, p, t;
    std::cin >> s >> p >> t;
    int n = p.size();
    std::vector<int> matching;

    std::string S = p + '#' + s;
    int prevK = 0;
    int m = S.size();
    std::vector<int> lcp (p.size(), 0);
    for (int i = 1; i < m; ++i) {
        int k = prevK;
        while (k && (S[k] != S[i])) k = lcp[k - 1];
        if (S[k] == S[i]) ++k;
        if (i < n) lcp[i] = k;
        prevK = k;
        if (k == n) matching.push_back(i - 2 * n);
    }

    std::reverse(matching.begin(), matching.end());
    int i = 0;
    while (i < s.size()) {
        if (!matching.empty() && i == matching.back()) {
            std::cout << t;
            matching.pop_back();
            i += p.size();
        } else {
            std::cout << s[i];
            ++i;
        }
    }
    std::cout << "\n";

}


int main() {
    solution();
}