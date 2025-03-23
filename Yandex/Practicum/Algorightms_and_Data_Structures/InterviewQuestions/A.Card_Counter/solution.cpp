#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(k)
    Memory Complexity O(k)
    */
    int n;
    std::scanf("%d", &n);
    int k;
    std::scanf("%d", &k);
    std::vector<int> nums (n, 0);
    for (int i = 0; i < n; ++i) std::scanf("%d", &nums[i]);
    long long curSum = 0;
    for (int i = 0; i < k; ++i) curSum += nums[i];
    int right = n - 1;
    long long maxSum = curSum;
    for (int i = k - 1; i >= 0; --i) {
        curSum -= nums[i];
        curSum += nums[right];
        --right;
        if (curSum > maxSum) maxSum = curSum;
    }
    std::printf("%lld\n", maxSum);
}


int main() {
    solution();
}