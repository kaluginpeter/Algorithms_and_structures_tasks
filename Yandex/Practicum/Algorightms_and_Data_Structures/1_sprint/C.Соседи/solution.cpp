#include <iostream>
#include <vector>
#include <algorithm>

void solution(int n, int m, std::vector<std::vector<int>>& matrix, int row, int col) {
    /*
    Time Complexity O(1)
    Memory Complexity O(1)
    */
    std::vector<int> neighbors;
    std::vector<std::pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for (std::pair<int, int>& dir : dirs) {
        int nextRow = row + dir.first;
        int nextCol = col + dir.second;
        if (0 <= std::min(nextRow, nextCol) && nextRow < n && nextCol < m) {
            neighbors.push_back(matrix[nextRow][nextCol]);
        }
    }
    std::sort(neighbors.begin(), neighbors.end());
    for (int index = 0; index < neighbors.size(); ++index) {
        if (index) {
            std::cout << " ";
        }
        std::cout << neighbors[index];
    }
};


int main() {
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> matrix;
    for (int i = 0; i < n; ++i) {
        std::vector<int> row;
        for (int j = 0; j < m; ++j) {
            int num;
            std::cin >> num;
            row.push_back(num);
        }
        matrix.push_back(row);
    }
    int row, col;
    std::cin >> row >> col;
    solution(n, m, matrix, row, col);
}
