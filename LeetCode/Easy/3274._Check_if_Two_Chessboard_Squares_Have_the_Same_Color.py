# You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square on an 8 x 8 chessboard.
#
# Below is the chessboard for reference.
#
#
#
# Return true if these two squares have the same color and false otherwise.
#
# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first (indicating its column), and the number second (indicating its row).
#
#
#
# Example 1:
#
# Input: coordinate1 = "a1", coordinate2 = "c3"
#
# Output: true
#
# Explanation:
#
# Both squares are black.
#
# Example 2:
#
# Input: coordinate1 = "a1", coordinate2 = "h3"
#
# Output: false
#
# Explanation:
#
# Square "a1" is black and "h3" is white.
#
#
#
# Constraints:
#
# coordinate1.length == coordinate2.length == 2
# 'a' <= coordinate1[0], coordinate2[0] <= 'h'
# '1' <= coordinate1[1], coordinate2[1] <= '8'
# C++
# Complexity
# Time complexity: O(1)
#
# Space complexity: O(1)
#
# Code
class Solution {
public:
    bool checkTwoChessboards(string c1, string c2) {
        string alphabet = "abcdefgh";
        int col1= alphabet.find(c1[0]) + 1;
        int row1 = stoi(c1.substr(1));
        int col2 = alphabet.find(c2[0]) + 1;
        int row2 = stoi(c2.substr(1));
        return (
            (
                (col1 % 2 != 0 && row1 % 2 != 0 || col1 % 2 == 0 && row1 % 2 == 0) &&
                (col2 % 2 != 0 && row2 % 2 != 0 || col2 % 2 == 0 && row2 % 2 == 0)
             ) ||
            (
                (col1 % 2 != 0 && row1 % 2 == 0 || col1 % 2 == 0 && row1 % 2 != 0) &&
                (col2 % 2 != 0 && row2 % 2 == 0 || col2 % 2 == 0 && row2 % 2 != 0)
            )
        );
    }
};

# Python
# Simulation
# Complexity
# Time complexity: O(1)
#
# Space complexity: O(1)
#
# Code
class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        mtrx: list[list[bool]] = []
        flag: bool = True
        for i in range(8):
            cur_row: list[bool] = []
            for j in range(8):
                cur_row.append(flag)
                flag = not flag
            flag = not flag
            mtrx.append(cur_row)
        return mtrx[int(c1[1]) - 1][ord(c1[0]) - 97] == mtrx[int(c2[1]) - 1][ord(c2[0]) - 97]