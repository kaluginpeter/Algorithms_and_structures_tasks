/*
You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


Return the matrix after applying k cyclic rotations to it.



Example 1:


Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.
Example 2:


Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.


Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 50
Both m and n are even integers.
1 <= grid[i][j] <= 5000
1 <= k <= 109
*/
// Solution
// C++ O(NM) O(N + M) Matrix
class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        size_t n = grid.size(), m = grid[0].size();
        for (int start = 0; start < std::min(n, m) >> 1; ++start) {
            std::vector<int> data;
            for (size_t i = start; i < n - start; ++i) {
                data.push_back(grid[i][start]);
            }
            for (size_t j = start + 1; j < m - start; ++j) {
                data.push_back(grid[n - start - 1][j]);
            }
            for (int i = n - start - 2; i >= start; --i) {
                data.push_back(grid[i][m - start - 1]);
            }
            for (int j = m - start - 2; j > start; --j) {
                data.push_back(grid[start][j]);
            }
            size_t bound = data.size(), step = k % bound, idx = 0;
            for (size_t i = start; i < n - start; ++i) {
                grid[i][start] = (data[(idx++ + bound - step) % bound]);
            }
            for (size_t j = start + 1; j < m - start; ++j) {
                grid[n - start - 1][j] = (data[(idx++ + bound - step) % bound]);
            }
            for (int i = n - start - 2; i >= start; --i) {
                grid[i][m - start - 1] = (data[(idx++ + bound - step) % bound]);
            }
            for (int j = m - start - 2; j > start; --j) {
                grid[start][j] = (data[(idx++ + bound - step) % bound]);
            }
        }
        return grid;
    }
};