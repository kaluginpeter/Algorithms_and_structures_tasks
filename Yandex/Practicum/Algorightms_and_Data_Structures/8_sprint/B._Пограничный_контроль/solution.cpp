#include <iostream>
#include <string>
#include <cmath>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    std::string a, b;
    std::cin >> a >> b;
    int n = a.size(), m = b.size();
    if (std::abs(n - m) > 1) {
        std::printf("FAIL\n");
        return;
    }
    if (n < m) {
        std::swap(a, b);
        std::swap(n, m);
    }
    bool alreadySkipped = false;
    int left = 0, right = 0;
    while (left < n && right < m) {
        if (a[left] == b[right]) {
            ++left;
            ++right;
        } else if (!alreadySkipped) {
            if (n != m) ++left;
            else {
                ++left;
                ++right;
            }
            alreadySkipped = true;
        } else {
            std::printf("FAIL\n");
            return;
        }
    }
    std::cout << ((left == n && right == m) || !alreadySkipped? "OK" : "FAIL") << "\n";

}


int main() {
    solution();
}