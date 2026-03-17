/*
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
More info at: http://en.wikipedia.org/wiki/Sudoku

Sudoku Solution Validator
Write a function that accepts a Sudoku board, and returns true if it is a valid Sudoku solution, or false otherwise. The cells of the input Sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

Examples
Valid board:

  5 3 4|6 7 8|9 1 2
  6 7 2|1 9 5|3 4 8
  1 9 8|3 4 2|5 6 7
  -----+-----+-----
  8 5 9|7 6 1|4 2 3
  4 2 6|8 5 3|7 9 1
  7 1 3|9 2 4|8 5 6
  -----+-----+-----
  9 6 1|5 3 7|2 8 4
  2 8 7|4 1 9|6 3 5
  3 4 5|2 8 6|1 7 9
Invalid board:

              This column has two 3's
                        v
This cell has a 0 > 0 3 4|6 7 8|9 1 2
                    6 7 2|1 9 5|3 4 8
                    1 9 8|3 4 2|5 6 7
                    -----+-----+-----
                    8 5 9|7 6 1|4 2 3
                    4 2 6|8 5 3|7 9 1
                    7 1 3|9 2 4|8 5 6
                    -----+-----+-----
    This box has   /9 6 1|5 3 7|2 8 4
         two 3's >| 2 8 3|4 1 9|6 3 5 < This row has two 3's
                   \3 4 5|2 8 6|1 7 9
Details
All inputs are guaranteed to be 2D boards of size 9x9 with possible values in range 0-9.
Rows, columns and blocks (3x3 small squares) must contain each number from range 1-9 exactly once.
User solution must not modify input boards.
AlgorithmsGames
*/
// Solution
#include <array>

bool is_valid_group(const int* nums) {
    bool seen[10] = {false};
    for (int i = 0; i < 9; ++i) {
        int val = nums[i];
        if (val == 0 || seen[val]) return false;
        seen[val] = true;
    }
    return true;
}

bool validate(const std::array<std::array<int, 9>, 9>& board) {
    int temp[9];
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) temp[j] = board[i][j];
        if (!is_valid_group(temp)) return false;
    }
    for (int j = 0; j < 9; ++j) {
        for (int i = 0; i < 9; ++i) temp[i] = board[i][j];
        if (!is_valid_group(temp)) return false;
    }
    for (int block_row = 0; block_row < 3; ++block_row) {
        for (int block_col = 0; block_col < 3; ++block_col) {
            int idx = 0;
            for (int i = 0; i < 3; ++i) {
                for (int j = 0; j < 3; ++j) {
                    temp[idx++] = board[block_row * 3 + i][block_col * 3 + j];
                }
            }
            if (!is_valid_group(temp)) return false;
        }
    }
    return true;
}