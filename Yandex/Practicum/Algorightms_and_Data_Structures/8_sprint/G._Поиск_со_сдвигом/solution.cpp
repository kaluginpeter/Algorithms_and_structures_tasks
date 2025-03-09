#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(NM)
    Memory Complexity O(1)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<int> a (n, 0);
    for (int i = 0; i < n; ++i) std::scanf("%d", &a[i]);
    int m;
    std::scanf("%d", &m);
    std::vector<int> b (m, 0);
    for (int i = 0; i < m; ++i) std::scanf("%d", &b[i]);
    for (int left = 0; left < n - m + 1; ++left) {
        bool match = true;
        int diff = a[left] - b[0];
        for (int right = 1; right < m; ++right) {
            if (a[left + right] - b[right] != diff) {
                match = false;
                break;
            }
        }
        if (match) std::printf("%d ", left + 1);
    }
    std::printf("\n");
}


int main() {
    solution();
}