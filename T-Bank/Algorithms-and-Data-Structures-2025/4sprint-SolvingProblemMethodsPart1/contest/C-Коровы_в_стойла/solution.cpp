#include <iostream>
#include <vector>



bool canPlace(int& dist, int k, std::vector<long long>& nums) {
    long long prev = 0;
    for (long long& num : nums) {
        if (num >= prev) {
            --k;
            prev = num + dist;
        }
    }
    return k <= 0;
}


void solution() {
    /*
    Time Complexity O(NlogM)
    Memory Complexity O(1)
    */
    int n, k;
    std::scanf("%d %d", &n, &k);
    std::vector<long long> nums (n, 0);
    for (int i = 0; i < n; ++i) std::scanf("%lld", &nums[i]);
    int left = 1;
    int right = nums[n - 1];
    int answer = 0;
    while (left <= right) {
        int middle = left + (right - left) / 2;
        if (canPlace(middle, k, nums)) {
            answer = middle;
            left = middle + 1;
        } else right = middle - 1;
    }
    std::printf("%d\n", answer);
}


int main() {
    solution();
}