#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<bool> seen (n + 1, false);
    std::vector<int> nums (n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    int zeros = 0;
    int last = n;
    std::cout << '1';
    for (int& num : nums) {
        std::cout << " ";
        seen[num] = true;
        ++zeros;
        while (seen[last]) {
            --last;
            --zeros;
        }
        std::cout << zeros + 1;
    }
    std::cout << "\n";
}


int main() {
    solution();
}