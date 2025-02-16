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
    for (int i = 0; i < n; ++i) {
        std::cin >> nums[i];
    }
    std::vector<int> dp (n + 1, 0);
    std::vector<std::vector<int>> paths (n + 1, std::vector<int>());
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            if ((nums[j - 1] < nums[i - 1]) && (dp[i] < dp[j])) {
                dp[i] = dp[j];
                paths[i] = paths[j];
            }
        }
        ++dp[i];
        paths[i].push_back(i);
    }
    int lisIdx = 0;
    for (int idx = 1; idx <= n; ++idx) {
        if (dp[idx] > dp[lisIdx]) lisIdx = idx;
    }
    std::printf("%d\n", dp[lisIdx]);
    if (dp[lisIdx]) {
        for (int& num : paths[lisIdx]) std::cout << num << " ";
        std::cout << "\n";
    }
}


int main() {
    solution();
}