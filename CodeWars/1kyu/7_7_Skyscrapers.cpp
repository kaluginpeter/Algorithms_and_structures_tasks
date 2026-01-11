/*
In a grid of 7 by 7 squares you want to place a skyscraper in each square with only some clues:

The height of the skyscrapers is between 1 and 7
No two skyscrapers in a row or column may have the same number of floors
A clue is the number of skyscrapers that you can see in a row or column from the outside
Higher skyscrapers block the view of lower skyscrapers located behind them
Can you write a program that can solve this puzzle in time?

This kata is based on 4 By 4 Skyscrapers and 6 By 6 Skyscrapers by FrankK. By now, examples should be superfluous; you should really solve Frank's kata first, and then probably optimise some more. A naive solution that solved a 4×4 puzzle within 12 seconds might need time somewhere beyond the Heat Death of the Universe for this size. It's quite bad.

Task
Create

def solve_puzzle(clues)
Clues are passed in as a list(28) of integers.
The return value is a list(7) of list(7) of integers.

All puzzles have one possible solution.
All this is the same as with the earlier kata.

Caveat: The tests for this kata have been tailored to run in ~10 seconds with the JavaScript reference solution. You'll need to do better than that! Please note the performance tag.

Conceptis Puzzles have heaps of these puzzles, from 4×4 up to 7×7 and unsolvable within CodeWars time constraints. Old puzzles from there were used for the tests. They also have lots of other logic, numbers and mathematical puzzles, and their puzzle user interface is generally nice, very nice.

AlgorithmsGamesPerformance
*/
// Solution
#include <bits/stdc++.h>
using namespace std;

const int GRID_SIZE = 7;
const int DIR_COUNT = 4;
const int ALL_BITS = (1 << GRID_SIZE) - 1;

const int lineStart[DIR_COUNT * GRID_SIZE] = {
    0,1,2,3,4,5,6,
    6,13,20,27,34,41,48,
    48,47,46,45,44,43,42,
    42,35,28,21,14,7,0
};

const int lineStep[DIR_COUNT * GRID_SIZE] = {
    7,7,7,7,7,7,7,
    -1,-1,-1,-1,-1,-1,-1,
    -7,-7,-7,-7,-7,-7,-7,
    1,1,1,1,1,1,1
};

int cellMask[GRID_SIZE * GRID_SIZE];
int finalGrid[GRID_SIZE][GRID_SIZE];
bool locked[GRID_SIZE * GRID_SIZE];
vector<int> cluesData;

void assignCell(int index, int value) {
    int forbid = ALL_BITS ^ (1 << value);
    int rowBase = index - index % GRID_SIZE;
    int colBase = index % GRID_SIZE;
    for (int i = 0; i < GRID_SIZE; i++) {
        cellMask[rowBase + i] &= forbid;
        cellMask[colBase + i * GRID_SIZE] &= forbid;
    }
    cellMask[index] = 1 << value;
}

int propagateUnique() {
    int changes = 0;
    for (int i = 0; i < DIR_COUNT / 2 * GRID_SIZE; i++) {
        map<int, vector<int>> valueCells;
        for (int p = lineStart[i], k = 0; k < GRID_SIZE; p += lineStep[i], k++) {
            for (int v = 0; v < GRID_SIZE; v++)
                if (cellMask[p] & (1 << v)) valueCells[v].push_back(p);
        }
        for (auto &e : valueCells) {
            if (e.second.size() == 1) {
                int pos = e.second[0];
                if (cellMask[pos] != (1 << e.first)) {
                    assignCell(pos, e.first);
                    changes++;
                }
            }
        }
    }
    return changes;
}

int pruneTwoClue() {
    int cnt = 0;
    for (int i = 0; i < DIR_COUNT * GRID_SIZE; i++) {
        if (cluesData[i] != 2) continue;
        int allowed = ALL_BITS;
        for (int v = GRID_SIZE - 1; v >= 0; v--) {
            allowed ^= 1 << v;
            if (cellMask[lineStart[i]] & (1 << v)) break;
        }
        for (int p = lineStart[i] + lineStep[i], k = 1; k < GRID_SIZE; p += lineStep[i], k++) {
            if (cellMask[p] & (1 << (GRID_SIZE - 1))) break;
            if ((cellMask[p] | allowed) != allowed) {
                cellMask[p] &= allowed;
                cnt++;
            }
        }
    }
    return cnt;
}

int countBits(int x) {
    int c = 0;
    while (x) {
        c += x & 1;
        x >>= 1;
    }
    return c;
}

bool checkConsistency() {
    for (int i = 0; i < DIR_COUNT * GRID_SIZE; i++) {
        if (cluesData[i] == 0) continue;
        bool complete = true;
        for (int p = lineStart[i], k = 0; k < GRID_SIZE; p += lineStep[i], k++) {
            if (countBits(cellMask[p]) != 1) {
                complete = false;
                break;
            }
        }
        if (complete) {
            int tallest = 0, visible = 0;
            for (int p = lineStart[i], k = 0; k < GRID_SIZE; p += lineStep[i], k++) {
                if (cellMask[p] > tallest) {
                    tallest = cellMask[p];
                    visible++;
                }
            }
            if (visible != cluesData[i]) return false;
        }
    }
    return true;
}

void extractSolution() {
    for (int i = 0; i < GRID_SIZE * GRID_SIZE; i++) {
        int r = i / GRID_SIZE, c = i % GRID_SIZE;
        for (int v = 0; v < GRID_SIZE; v++)
            if (cellMask[i] == (1 << v)) finalGrid[r][c] = v + 1;
    }
}

bool search(int depth) {
    int chosen = -1, best = 10000;
    for (int i = 0; i < GRID_SIZE * GRID_SIZE; i++) {
        int options = countBits(cellMask[i]);
        if (options < best && !locked[i]) {
            best = options;
            chosen = i;
        }
    }
    if (chosen == -1) {
        if (checkConsistency()) {
            extractSolution();
            return true;
        }
        return false;
    }
    int backup[GRID_SIZE * GRID_SIZE];
    memcpy(backup, cellMask, sizeof(int) * GRID_SIZE * GRID_SIZE);
    for (int v = GRID_SIZE - 1; v >= 0; v--) {
        if (!(cellMask[chosen] & (1 << v))) continue;
        locked[chosen] = true;
        assignCell(chosen, v);
        if (checkConsistency() && search(depth + 1)) return true;
        locked[chosen] = false;
        memcpy(cellMask, backup, sizeof(int) * GRID_SIZE * GRID_SIZE);
    }
    return false;
}

void resetState() {
    for (int i = 0; i < GRID_SIZE * GRID_SIZE; i++) {
        cellMask[i] = ALL_BITS;
        locked[i] = true;
    }
}

void preprocess() {
    for (int i = 0; i < DIR_COUNT * GRID_SIZE; i++) {
        if (cluesData[i] == 0) continue;
        for (int p = lineStart[i], k = 0; k < GRID_SIZE; p += lineStep[i], k++) {
            int mask = ALL_BITS;
            for (int v = GRID_SIZE + k - cluesData[i] + 1; v < GRID_SIZE; v++) mask ^= 1 << v;
            cellMask[p] &= mask;
        }
    }
    while (propagateUnique() > 0);
    pruneTwoClue();
}

vector<vector<int>> SolvePuzzle(const vector<int> &clues) {
    vector<vector<int>> result;
    resetState();
    cluesData = clues;
    preprocess();
    for (int i = 0; i < GRID_SIZE * GRID_SIZE; i++)
        if (countBits(cellMask[i]) > 1)
            locked[i] = false;
    search(0);
    for (int i = 0; i < GRID_SIZE; i++) {
        vector<int> row;
        for (int j = 0; j < GRID_SIZE; j++) row.push_back(finalGrid[i][j]);
        result.push_back(row);
    }
    return result;
}