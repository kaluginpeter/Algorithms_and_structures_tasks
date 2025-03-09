#include <iostream>
#include <string>
#include <vector>



void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    std::string a;
    std::cin >> a;
    int n = a.size();
    std::vector<int> lcp (n, 0);
    for (int i = 1; i < n; ++i) {
        int k = lcp[i - 1];
        while (k && a[k] != a[i]) k = lcp[k - 1];
        if (a[k] == a[i]) ++k;
        lcp[i] = k;
    }
    for (int& p : lcp) std::printf("%d ", p);
    std::printf("\n");
}


int main() {
    solution();
}