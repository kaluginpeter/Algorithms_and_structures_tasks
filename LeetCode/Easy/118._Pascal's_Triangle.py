# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Example 1:
#
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
#
# Input: numRows = 1
# Output: [[1]]
#
# Constraints:
# 1 <= numRows <= 30
# Solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row, l = [1], [[1]]
        for i in range(numRows - 1):
            row = [sum(i) for i in zip([0] + row, row + [0])]
            l.append(row)
        return l
# Solution 2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row, triangle = [1], [[1]]
        for i in range(numRows-1):
            row = [x + y for x, y in zip([0] + row, row + [0])]
            triangle.append(row)
        return triangle


# Python O(N^2) O(N^2) Simulation
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output: list[list[int]] = []
        cur_row: list[int] = [1]
        next_row: list[int] = []
        for _ in range(numRows):
            output.append(cur_row.copy())
            next_row.clear()
            next_row.append(1)
            for i in range(len(cur_row) - 1):
                next_row.append(cur_row[i] + cur_row[i + 1])
            next_row.append(1)
            cur_row = next_row[::]
        return output

# C++ O(N^2) O(N^2) Simulation
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        std::vector<int> curRow = {1}, nextRow;
        std::vector<std::vector<int>> output;
        for (int i = 0; i < numRows; ++i) {
            output.push_back(curRow);
            nextRow.clear();
            nextRow.push_back(1);
            for (int j = 0; j < curRow.size() - 1; ++j) {
                nextRow.push_back(curRow[j] + curRow[j + 1]);
            }
            nextRow.push_back(1);
            curRow = nextRow;
        }
        return output;
    }
};