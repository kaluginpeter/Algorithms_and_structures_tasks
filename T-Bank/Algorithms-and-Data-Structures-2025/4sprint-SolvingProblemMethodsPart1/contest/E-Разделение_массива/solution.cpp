#include <iostream>
#include <vector>


bool canDistribute(int& n, int k, std::vector<long long>& nums, long long& bound) {
    --k;
    long long curSum = 0;
    for(long long& num : nums) {
        if (curSum + num > bound) {
            curSum = num;
            --k;
        } else curSum += num;
    }
    return k >= 0;
}


void solution() {
    /*
    Time Complexity O(NlogM)
    Memory Complexity O(1)
    */
    int n, k;
    std::scanf("%d %d", &n, &k);
    std::vector<long long> nums (n, 0);
    long long left = 0;
    long long right = 0;
    for (int i = 0; i < n; ++i) {
        std::scanf("%lld", &nums[i]);
        right += nums[i];
        left = std::max(left, nums[i]);
    }
    while (left <= right) {
        long long middle = left + (right - left) / 2;
        if (canDistribute(n, k, nums, middle)) {
            right = middle - 1;
        } else left = middle + 1;
    }
    std::printf("%lld\n", left);
}


int main() {
    solution();
}