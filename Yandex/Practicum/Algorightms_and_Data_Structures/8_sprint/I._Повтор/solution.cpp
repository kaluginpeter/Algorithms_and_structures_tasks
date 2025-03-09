#include <iostream>
#include <string>
#include <vector>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    std::string sequence;
    std::cin >> sequence;
    int n = sequence.size();
    std::vector<int> lcp (n, 0);
    for (int i = 1; i < n; ++i) {
        int k = lcp[i - 1];
        while (k && sequence[k] != sequence[i]) k = lcp[k - 1];
        if (sequence[k] == sequence[i]) ++k;
        lcp[i] = k;
    }
    std::printf("%d\n", (n % (n - lcp[n - 1]) == 0? n / (n - lcp[n - 1]) : 1));
}


int main() {
    solution();
}