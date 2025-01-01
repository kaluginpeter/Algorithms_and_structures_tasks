#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

void solution(std::vector<long long>& nums, long long target) {
    /*
    Time Complexity O(N**3)
    Memory Complexity O(N**4)
    */
    std::sort(nums.begin(), nums.end());
    std::set<std::vector<long long>> result;
    int n = nums.size();

    for (int i = 0; i < n - 3; ++i) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        for (int j = i + 1; j < n - 2; ++j) {
            if (j > i + 1 && nums[j] == nums[j - 1]) continue;
            int left = j + 1, right = n - 1;
            while (left < right) {
                long long current_sum = nums[i] + nums[j] + nums[left] + nums[right];
                if (current_sum < target) {
                    left++;
                } else if (current_sum > target) {
                    right--;
                } else {
                    result.insert({nums[i], nums[j], nums[left], nums[right]});
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1]) left++;
                    while (left < right && nums[right] == nums[right + 1]) right--;
                }
            }
        }
    }

    std::cout << result.size() << "\n";
    for (const auto& quadruplet : result) {
        for (long long num : quadruplet) {
            std::cout << num << " ";
        }
        std::cout << "\n";
    }
}

int main() {
    int n;
    long long target;
    std::cin >> n >> target;
    std::vector<long long> nums(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> nums[i];
    }
    solution(nums, target);
    return 0;
}
