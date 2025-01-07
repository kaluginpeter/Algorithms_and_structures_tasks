#include <iostream>
#include <vector>

long long countBST(int n) {
    std::vector<long long> catalan(n + 1, 0);
    catalan[0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            catalan[i] += catalan[j] * catalan[i - 1 - j];
        }
    }
    return catalan[n];
}

int main() {
    /*
    Time Complexity O(1)
    Memory Complexity O(1)
    */
    int n;
    std::cin >> n;
    std::cout << countBST(n) << std::endl;
}