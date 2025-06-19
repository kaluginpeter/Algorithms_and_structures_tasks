#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    std::cin >> n;
    std::vector<int> nums (n, 0);
    for (int i = 1; i <= n; ++i) nums[i - 1] = i;
    for (int idx = 2; idx < n; ++idx) {
        std::swap(nums[idx], nums[idx / 2]);
    }
    for (int i = 0; i < n; ++i) {
        if (i) std::cout << " ";
        std::cout << nums[i];
    }
    std::cout << "\n";
}


int main() {
    solution();
}