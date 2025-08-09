/*
Connect Four
Take a look at wiki description of Connect Four game:

Wiki Connect Four

The grid is 6 row by 7 columns, those being named from A to G.

You will receive a list of strings showing the order of the pieces which dropped in columns:

std::vector<std::string> pieces_position_list
{
  "A_Red",
  "B_Yellow",
  "A_Red",
  "B_Yellow",
  "A_Red",
  "B_Yellow",
  "G_Red",
  "B_Yellow"
}
The list may contain up to 42 moves and shows the order the players are playing.

The first player who connects four items of the same color is the winner.

You should return "Yellow", "Red" or "Draw" accordingly.

Fundamentals
*/
// Solution
#include <string>
#include <vector>
#include <iostream>


int makeMove(int column, int player, std::vector<std::vector<int>> &grid) {
    for (int i = 5; i >= 0; --i) {
      if (grid[i][column] == -1) {
          grid[i][column] = player;
          return i;
      }
    }
    return -1;
};
bool checkPlayer(int column, int row, const std::vector<std::vector<int>> &grid) {
    int left = column, right = column;
    while (left >= 0 && grid[row][left] == grid[row][column]) --left;
    while (right < 7 && grid[row][right] == grid[row][column]) ++right;
    if (right - left - 1 >= 4) return true;
    left = row;
    right = row;
    while (left >= 0 && grid[left][column] == grid[row][column]) --left;
    while (right < 6 && grid[right][column] == grid[row][column]) ++right;
    if (right - left - 1 >= 4) return true;
    left = 0;
    right = 0;
    while (row - left >= 0 && column - left >= 0 && grid[row - left][column - left] == grid[row][column]) ++left;
    while (row + right < 6 && column + right < 7 && grid[row][column] == grid[row + right][column + right]) ++right;
    if (left + right - 1 >= 4) return true;
    left = 0;
    right = 0;
    while (row - left >= 0 && column + left < 7 && grid[row][column] == grid[row - left][column + left]) ++left;
    while (row + right < 6 && column - right >= 0 && grid[row][column] == grid[row + right][column - right]) ++right;
    return left + right - 1 >= 4;
};


std::string who_is_winner(std::vector<std::string> pieces_position_list)
{
  std::vector<std::vector<int>> grid(6, std::vector<int>(7, -1));
  for (const std::string &move : pieces_position_list) {
      int row = makeMove(move[0] - 'A', (move.substr(2) == "Red" ? 1 : 0), grid);
      if (checkPlayer(move[0] - 'A', row, grid)) return move.substr(2);
  }
  return "Draw";
}