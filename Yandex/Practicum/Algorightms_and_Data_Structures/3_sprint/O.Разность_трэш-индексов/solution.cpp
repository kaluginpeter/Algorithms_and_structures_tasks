#include <iostream>
#include <vector>
#include <algorithm>

long long getPairsLowerOrEqualThatDiff(long long diff, std::vector<int>& nums, int n) {
    long long pairs = 0;
    int right = 0;
    for (int left = 0; left < n; ++left) {
        while (right < n && nums[right] - nums[left] <= diff) {
            ++right;
        }
        pairs += right - left - 1;
    }
    return pairs;
}

void solution(int n, std::vector<int>& nums, long long k) {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    */
    std::sort(nums.begin(), nums.end());
    long long left = 0;
    long long right = nums[n - 1] - nums[0];
    while (left <= right) {
        long long middle = left + (right - left) / 2;
        if (getPairsLowerOrEqualThatDiff(middle, nums, n) < k) {
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }
    std::cout << left << "\n";
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> nums;
    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;
        nums.push_back(num);
    }
    long long k;
    std::cin >> k;
    solution(n, nums, k);
}
