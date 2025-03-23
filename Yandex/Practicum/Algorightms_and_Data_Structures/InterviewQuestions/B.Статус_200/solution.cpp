#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<int> nums (n, 0);
    for (int i = 0; i < n; ++i) std::scanf("%d", &nums[i]);
    long long totalPairs = 0;
    std::vector<long long> hashmap (200, 0);
    for (int& num : nums) {
        int remainder = num % 200;
        totalPairs += hashmap[remainder];
        ++hashmap[remainder];
    }
    std::printf("%lld\n", totalPairs);
}


int main() {
    solution();
}