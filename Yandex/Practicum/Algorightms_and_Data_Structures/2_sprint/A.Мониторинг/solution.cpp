#include <iostream>
#include <vector>

void solution(int n, int m, std::vector<std::vector<int>>& matrix) {
    /*
    Time Complexity O(NM)
    Memory Complexity O(1)
    */
    for (int col = 0; col < m; ++col) {
        for (int row = 0; row < n; ++row) {
            if (row) {
                std::cout << " ";
            }
            std::cout << matrix[row][col];
        }
        std::cout << "\n";
    }
}

int main() {
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> matrix;
    for (int r = 0; r < n; ++r) {
        std::vector<int> row;
        for (int c = 0; c < m; ++c) {
            int num;
            std::cin >> num;
            row.push_back(num);
        }
        matrix.push_back(row);
    }
    solution(n, m, matrix);
}