# There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1). You are given the integer n and an integer array startPos where startPos = [startrow, startcol] indicates that a robot is initially at cell (startrow, startcol).
#
# You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).
#
# The robot can begin executing from any ith instruction in s. It executes the instructions one by one towards the end of s but it stops if either of these conditions is met:
#
# The next instruction will move the robot off the grid.
# There are no more instructions left to execute.
# Return an array answer of length m where answer[i] is the number of instructions the robot can execute if the robot begins executing from the ith instruction in s.
#
#
#
# Example 1:
#
#
# Input: n = 3, startPos = [0,1], s = "RRDDLU"
# Output: [1,5,4,3,1,0]
# Explanation: Starting from startPos and beginning execution from the ith instruction:
# - 0th: "RRDDLU". Only one instruction "R" can be executed before it moves off the grid.
# - 1st:  "RDDLU". All five instructions can be executed while it stays in the grid and ends at (1, 1).
# - 2nd:   "DDLU". All four instructions can be executed while it stays in the grid and ends at (1, 0).
# - 3rd:    "DLU". All three instructions can be executed while it stays in the grid and ends at (0, 0).
# - 4th:     "LU". Only one instruction "L" can be executed before it moves off the grid.
# - 5th:      "U". If moving up, it would move off the grid.
# Example 2:
#
#
# Input: n = 2, startPos = [1,1], s = "LURD"
# Output: [4,1,0,0]
# Explanation:
# - 0th: "LURD".
# - 1st:  "URD".
# - 2nd:   "RD".
# - 3rd:    "D".
# Example 3:
#
#
# Input: n = 1, startPos = [0,0], s = "LRUD"
# Output: [0,0,0,0]
# Explanation: No matter which instruction the robot begins execution from, it would move off the grid.
#
#
# Constraints:
#
# m == s.length
# 1 <= n, m <= 500
# startPos.length == 2
# 0 <= startrow, startcol < n
# s consists of 'L', 'R', 'U', and 'D'.
# Solution
# Python O(min(N, S)^2) O(S) Matrix
class Solution:
    def simulate(self, start_pos: list[int], n: int, s: str, start: int) -> int:
        moves: int = 0
        row: int = start_pos[0]
        col: int = start_pos[1]
        pointer: int = start
        while pointer < len(s):
            is_valid: bool = True
            match s[pointer]:
                case 'U':
                    if not row:
                        is_valid = False
                    else:
                        row -= 1
                case 'D':
                    if row == n - 1:
                        is_valid = False
                    else:
                        row += 1
                case 'R':
                    if col == n - 1:
                        is_valid = False
                    else:
                        col += 1
                case 'L':
                    if not col:
                        is_valid = False
                    else:
                        col -= 1
            if not is_valid: break
            moves += 1
            pointer += 1
        return moves

    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m: int = len(s)
        output: list[int] = [0] * m
        for i in range(m):
            output[i] = self.simulate(startPos, n, s, i)
        return output

# C++ O(min(N, S)^2) O(S) Matrix
class Solution {
public:
    int simulate(const std::vector<int>& startPos, const int& n, const std::string& s, const size_t& start) {
        int moves = 0;
        size_t row = startPos[0], col = startPos[1], pointer = start;
        while (pointer < s.size()) {
            bool isValid = true;
            switch (s[pointer] - 'A') {
                case 20: // Up
                    if (!row) isValid = false;
                    else --row;
                    break;
                case 3: // Down
                    if (row == n - 1) isValid = false;
                    else ++row;
                    break;
                case 17: // Right
                    if (col == n - 1) isValid = false;
                    else ++col;
                    break;
                case 11: // Left
                    if (!col) isValid = false;
                    else --col;
                    break;
            }
            if (!isValid) break;
            ++moves;
            ++pointer;
        }
        return moves;
    }
    vector<int> executeInstructions(int n, vector<int>& startPos, string s) {
        size_t m = s.size();
        std::vector<int> output(m, 0);
        for (size_t i = 0; i < m; ++i) {
            output[i] = simulate(startPos, n, s, i);
        }
        return output;
    }
};