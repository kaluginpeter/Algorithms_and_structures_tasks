# You are given a non-negative integer N representing a 2N x 2N grid. You must fill the grid with integers from 0 to 22N - 1 to make it special. A grid is special if it satisfies all the following conditions:
#
# All numbers in the top-right quadrant are smaller than those in the bottom-right quadrant.
# All numbers in the bottom-right quadrant are smaller than those in the bottom-left quadrant.
# All numbers in the bottom-left quadrant are smaller than those in the top-left quadrant.
# Each of its quadrants is also a special grid.
# Return the special 2N x 2N grid.
#
# Note: Any 1x1 grid is special.
#
#
#
# Example 1:
#
# Input: N = 0
#
# Output: [[0]]
#
# Explanation:
#
# The only number that can be placed is 0, and there is only one possible position in the grid.
#
# Example 2:
#
# Input: N = 1
#
# Output: [[3,0],[2,1]]
#
# Explanation:
#
# The numbers in each quadrant are:
#
# Top-right: 0
# Bottom-right: 1
# Bottom-left: 2
# Top-left: 3
# Since 0 < 1 < 2 < 3, this satisfies the given constraints.
#
# Example 3:
#
# Input: N = 2
#
# Output: [[15,12,3,0],[14,13,2,1],[11,8,7,4],[10,9,6,5]]
#
# Explanation:
#
#
#
# The numbers in each quadrant are:
#
# Top-right: 3, 0, 2, 1
# Bottom-right: 7, 4, 6, 5
# Bottom-left: 11, 8, 10, 9
# Top-left: 15, 12, 14, 13
# max(3, 0, 2, 1) < min(7, 4, 6, 5)
# max(7, 4, 6, 5) < min(11, 8, 10, 9)
# max(11, 8, 10, 9) < min(15, 12, 14, 13)
# This satisfies the first three requirements. Additionally, each quadrant is also a special grid. Thus, this is a special grid.
#
#
#
# Constraints:
#
# 0 <= N <= 10
# Solution
# Python O(N^2) O(N^2) Matrix Recursion Math
class Solution:
    def proccess_quad(self, top: int, left: int, size: int, value: int, grid: list[list[int]]) -> None:
            if size == 1:
                grid[top][left] = value
                return
            half: int = size // 2
            self.proccess_quad(top, left + half, half, value, grid)
            self.proccess_quad(top + half, left + half, half, value + half * half, grid)
            self.proccess_quad(top + half, left, half, value + 2 * half * half, grid)
            self.proccess_quad(top, left, half, value + 3 * half * half, grid)

    def specialGrid(self, N: int) -> List[List[int]]:
        n: int = 2**N
        grid: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]
        self.proccess_quad(0, 0, n, 0, grid)
        return grid

# C++ O(N^2) O(N^2) Math Recursion Matrix
class Solution {
public:
    void proccessQuad(int top, int left, int size, int value, vector<vector<int>> &grid) {
        if (size == 1) {
            grid[top][left] = value;
            return;
        }
        int half = size / 2;
        proccessQuad(top, left + half, half, value, grid);
        proccessQuad(top + half, left + half, half, value + half * half, grid);
        proccessQuad(top + half, left, half, value + 2 * half * half, grid);
        proccessQuad(top, left, half, value + 3 * half * half, grid);
    }
    vector<vector<int>> specialGrid(int N) {
        int n = std::pow(2, N);
        vector<vector<int>> grid(n, std::vector<int>(n, 0));
        proccessQuad(0, 0, n, 0, grid);
        return grid;
    }
};