/*
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.


Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

This is all you need to solve this kata. If you're interested in more information about the game, visit this link.
GamesArraysAlgorithms
*/
// Solution
#include <vector>

bool validate_battlefield(std::vector< std::vector<int> > field) {
    std::vector<std::vector<bool>> visited(10, std::vector<bool>(10, false));
    std::vector<int> ships(5, 0);

    auto in_bounds = [](int r, int c) {
        return r >= 0 && r < 10 && c >= 0 && c < 10;
    };

    auto has_diagonal = [&](int r, int c) {
        int dr[2] = {-1, 1};
        int dc[2] = {-1, 1};
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 2; ++j) {
                int nr = r + dr[i];
                int nc = c + dc[j];
                if (in_bounds(nr, nc) && field[nr][nc] == 1) return true;
            }
        }
        return false;
    };

    for (int r = 0; r < 10; ++r) {
        for (int c = 0; c < 10; ++c) {
            if (field[r][c] == 1 && !visited[r][c]) {
                if (has_diagonal(r, c)) return false;
                int length = 1;
                visited[r][c] = true;
                if (in_bounds(r, c+1) && field[r][c+1] == 1) {
                    int nc = c + 1;
                    while (in_bounds(r, nc) && field[r][nc] == 1) {
                        if (has_diagonal(r, nc)) return false;
                        if (in_bounds(r+1, nc) && field[r+1][nc] == 1) return false;
                        visited[r][nc] = true;
                        ++length;
                        ++nc;
                    }
                }
                else if (in_bounds(r+1, c) && field[r+1][c] == 1) {
                    int nr = r + 1;
                    while (in_bounds(nr, c) && field[nr][c] == 1) {
                        if (has_diagonal(nr, c)) return false;
                        if (in_bounds(nr, c+1) && field[nr][c+1] == 1) return false;
                        visited[nr][c] = true;
                        ++length;
                        ++nr;
                    }
                }
                if (length > 4) return false;
                ++ships[length];
            }
        }
    }

    return ships[1] == 4 &&
           ships[2] == 3 &&
           ships[3] == 2 &&
           ships[4] == 1;
}