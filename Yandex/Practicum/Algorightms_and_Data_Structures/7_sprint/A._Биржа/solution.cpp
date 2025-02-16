#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    int n;
    std::cin >> n;
    std::vector<int> nums (n, 0);
    for (int i = 0; i < n; ++i) {
        std::cin >> nums[i];
    }
    int profit = 0;
    int curPrice = 0;
    for (int idx = 0; idx < n; ++idx) {
        if (!idx || nums[idx] < curPrice) {
            curPrice = nums[idx];
        } else {
            profit += nums[idx] - curPrice;
            curPrice = nums[idx];
        }
    }
    std::cout << profit << "\n";
}


int main() {
    solution();
}