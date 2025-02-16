#include <iostream>
#include <vector>
#include <string>
#include <algorithm>


void solution() {
    /*
    Time Complexity O(NM)
    Memory Complexity O(NM)
    */
    int n, m;
    std::cin >> n >> m;
    std::vector<std::string> grid;
    for (int i = 0; i < n; ++i) {
        std::string row;
        std::cin >> row;
        grid.push_back(row);
    }
    std::reverse(grid.begin(), grid.end());
    std::vector<std::vector<int>> dp (n, std::vector<int>(m, 0));
    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < m; ++col) {
            dp[row][col] = (grid[row][col] - '0') + std::max((row? dp[row - 1][col] : 0), (col? dp[row][col - 1] : 0));
        }
    }
    std::cout << dp[n - 1][m - 1] << "\n";
}

int main() {
    solution();
}