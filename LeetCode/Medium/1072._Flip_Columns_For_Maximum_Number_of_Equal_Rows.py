# You are given an m x n binary matrix matrix.
#
# You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).
#
# Return the maximum number of rows that have all values equal after some number of flips.
#
#
#
# Example 1:
#
# Input: matrix = [[0,1],[1,1]]
# Output: 1
# Explanation: After flipping no values, 1 row has all values equal.
# Example 2:
#
# Input: matrix = [[0,1],[1,0]]
# Output: 2
# Explanation: After flipping values in the first column, both rows have equal values.
# Example 3:
#
# Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
# Explanation: After flipping values in the first two columns, the last two rows have equal values.
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is either 0 or 1.
# Solution
# Python O(MN) O(M + N) Matrix Hashmap
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hashmap: dict[str, int] = dict()
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            cur_pattern: list[str] = []
            for col in range(n):
                if col and matrix[row][col - 1] != matrix[row][col]:
                    cur_pattern.append('|')
                cur_pattern.append('*')
            str_cur_pattern: str = ''.join(cur_pattern)
            hashmap[str_cur_pattern] = hashmap.get(str_cur_pattern, 0) + 1
        max_reps: int = 0
        for pattern, freq in hashmap.items():
            if freq > max_reps:
                max_reps = freq
        return max_reps

# C++ O(MN) O(M + N) Matrix Hashmap
class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        std::unordered_map<std::string, int> hashmap;
        int m = matrix.size();
        int n = matrix[0].size();
        for (int row = 0; row < m; ++row) {
            std::string curPattern = "";
            for (int col = 0; col < n; ++col) {
                if (col && matrix[row][col - 1] != matrix[row][col]) {
                    curPattern += '|';
                }
                curPattern += '*';
            }
            ++hashmap[curPattern];
        }
        int maxReps = 0;
        for (auto& pair : hashmap) {
            if (pair.second > maxReps) {
                maxReps = pair.second;
            }
        }
        return maxReps;
    }
};