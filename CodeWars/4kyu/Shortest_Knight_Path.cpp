/*
Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.

The knight is not allowed to move off the board. The board is 8x8.

For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29

For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29

(Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input, output, and expected output; please post them.)

Algorithms
*/
// Solution
#include <string>
#include <vector>
int knight(std::string start, std::string finish) {
  std::vector<std::pair<int, int>> directions = {
    {-2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {-1, -2}, {1, -2}
  };
  std::vector<std::vector<int>> seen(9, std::vector<int>(9, false));
  std::vector<std::pair<int, int>> curMoves = {{start[0] - 'a' + 1, start[1] - '0'}}, nextMoves;
  int steps = -1;
  while (!curMoves.empty()) {
    ++steps;
    for (const std::pair<int, int> &move : curMoves) {
      if (move.first == finish[0] - 'a' + 1 && move.second == (finish[1] - '0')) return steps;
      for (const std::pair<int, int> &direction : directions) {
        int nextRow = move.first + direction.first;
        int nextCol = move.second + direction.second;
        if (nextRow <= 0 || nextRow > 8 || nextCol <= 0 || nextCol > 8 || seen[nextRow][nextCol]) continue;
        seen[nextRow][nextCol] = true;
        nextMoves.push_back({nextRow, nextCol});
      }
    }
    curMoves = nextMoves;
    nextMoves.clear();
  }
  return -1;
}