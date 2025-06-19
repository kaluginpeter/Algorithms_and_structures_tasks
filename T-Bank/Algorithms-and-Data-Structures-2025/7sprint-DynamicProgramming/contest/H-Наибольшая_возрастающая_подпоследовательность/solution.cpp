#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(N^2)
    Memory Complexity O(N)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<int> nums (n, 0);
    std::vector<int> prev (n, -1);
    for (int i = 0; i < n; ++i) std::scanf("%d", &nums[i]);
    std::vector<int> dp(n, 1);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (nums[i] > nums[j] && dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }
    }
    int i = 0;
    for (int j = 1; j < n; ++j) {
        if (dp[i] < dp[j]) i = j;
    }
    std::vector<int> path;
    path.push_back(nums[i]);
    while (prev[i] != -1) {
        path.push_back(nums[prev[i]]);
        i = prev[i];
    }
    std::printf("%d\n", path.size());
    for (int j = path.size() - 1; j >= 0; --j) {
        std::printf("%d ", path[j]);
    }
    std::printf("\n");
    
}


int main() {
    solution();
}