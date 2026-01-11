# In a grid of 7 by 7 squares you want to place a skyscraper in each square with only some clues:
#
# The height of the skyscrapers is between 1 and 7
# No two skyscrapers in a row or column may have the same number of floors
# A clue is the number of skyscrapers that you can see in a row or column from the outside
# Higher skyscrapers block the view of lower skyscrapers located behind them
# Can you write a program that can solve this puzzle in time?
#
# This kata is based on 4 By 4 Skyscrapers and 6 By 6 Skyscrapers by FrankK. By now, examples should be superfluous; you should really solve Frank's kata first, and then probably optimise some more. A naive solution that solved a 4×4 puzzle within 12 seconds might need time somewhere beyond the Heat Death of the Universe for this size. It's quite bad.
#
# Task
# Create
#
# def solve_puzzle(clues)
# Clues are passed in as a list(28) of integers.
# The return value is a list(7) of list(7) of integers.
#
# All puzzles have one possible solution.
# All this is the same as with the earlier kata.
#
# Caveat: The tests for this kata have been tailored to run in ~10 seconds with the JavaScript reference solution. You'll need to do better than that! Please note the performance tag.
#
# Conceptis Puzzles have heaps of these puzzles, from 4×4 up to 7×7 and unsolvable within CodeWars time constraints. Old puzzles from there were used for the tests. They also have lots of other logic, numbers and mathematical puzzles, and their puzzle user interface is generally nice, very nice.
#
# AlgorithmsGamesPerformance
# Solution
def solve_puzzle(clues):
    GRID_SIZE = 7
    DIR_COUNT = 4
    ALL_BITS = (1 << GRID_SIZE) - 1
    lineStart = [
        0,1,2,3,4,5,6,
        6,13,20,27,34,41,48,
        48,47,46,45,44,43,42,
        42,35,28,21,14,7,0
    ]
    lineStep = [
        7,7,7,7,7,7,7,
        -1,-1,-1,-1,-1,-1,-1,
        -7,-7,-7,-7,-7,-7,-7,
        1,1,1,1,1,1,1
    ]
    cellMask = [ALL_BITS] * (GRID_SIZE * GRID_SIZE)
    finalGrid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    locked = [True] * (GRID_SIZE * GRID_SIZE)
    cluesData = clues[:]
    def assignCell(index, value):
        forbid = ALL_BITS ^ (1 << value)
        rowBase = index - index % GRID_SIZE
        colBase = index % GRID_SIZE
        for i in range(GRID_SIZE):
            cellMask[rowBase + i] &= forbid
            cellMask[colBase + i * GRID_SIZE] &= forbid
        cellMask[index] = 1 << value

    def propagateUnique():
        changes = 0
        for i in range(DIR_COUNT // 2 * GRID_SIZE):
            valueCells = {}
            p = lineStart[i]
            for _ in range(GRID_SIZE):
                for v in range(GRID_SIZE):
                    if cellMask[p] & (1 << v):
                        valueCells.setdefault(v, []).append(p)
                p += lineStep[i]
            for v, cells in valueCells.items():
                if len(cells) == 1:
                    pos = cells[0]
                    if cellMask[pos] != (1 << v):
                        assignCell(pos, v)
                        changes += 1
        return changes

    def pruneTwoClue():
        cnt = 0
        for i in range(DIR_COUNT * GRID_SIZE):
            if cluesData[i] != 2:
                continue
            allowed = ALL_BITS
            for v in range(GRID_SIZE - 1, -1, -1):
                allowed ^= 1 << v
                if cellMask[lineStart[i]] & (1 << v):
                    break
            p = lineStart[i] + lineStep[i]
            for _ in range(1, GRID_SIZE):
                if cellMask[p] & (1 << (GRID_SIZE - 1)):
                    break
                if (cellMask[p] | allowed) != allowed:
                    cellMask[p] &= allowed
                    cnt += 1
                p += lineStep[i]
        return cnt

    def countBits(x):
        return x.bit_count()

    def checkConsistency():
        for i in range(DIR_COUNT * GRID_SIZE):
            if cluesData[i] == 0:
                continue
            p = lineStart[i]
            complete = True
            for _ in range(GRID_SIZE):
                if countBits(cellMask[p]) != 1:
                    complete = False
                    break
                p += lineStep[i]
            if complete:
                tallest = 0
                visible = 0
                p = lineStart[i]
                for _ in range(GRID_SIZE):
                    if cellMask[p] > tallest:
                        tallest = cellMask[p]
                        visible += 1
                    p += lineStep[i]
                if visible != cluesData[i]:
                    return False
        return True

    def extractSolution():
        for i in range(GRID_SIZE * GRID_SIZE):
            r, c = divmod(i, GRID_SIZE)
            for v in range(GRID_SIZE):
                if cellMask[i] == (1 << v):
                    finalGrid[r][c] = v + 1

    def search():
        chosen = -1
        best = 10**9
        for i in range(GRID_SIZE * GRID_SIZE):
            options = countBits(cellMask[i])
            if options < best and not locked[i]:
                best = options
                chosen = i
        if chosen == -1:
            if checkConsistency():
                extractSolution()
                return True
            return False

        backup = cellMask[:]
        for v in range(GRID_SIZE - 1, -1, -1):
            if not (cellMask[chosen] & (1 << v)):
                continue
            locked[chosen] = True
            assignCell(chosen, v)
            if checkConsistency() and search():
                return True
            locked[chosen] = False
            cellMask[:] = backup[:]
        return False

    def resetState():
        for i in range(GRID_SIZE * GRID_SIZE):
            cellMask[i] = ALL_BITS
            locked[i] = True

    def preprocess():
        for i in range(DIR_COUNT * GRID_SIZE):
            if cluesData[i] == 0:
                continue
            p = lineStart[i]
            for k in range(GRID_SIZE):
                mask = ALL_BITS
                for v in range(GRID_SIZE + k - cluesData[i] + 1, GRID_SIZE):
                    mask ^= 1 << v
                cellMask[p] &= mask
                p += lineStep[i]
        while propagateUnique() > 0:
            pass
        pruneTwoClue()
    resetState()
    preprocess()
    for i in range(GRID_SIZE * GRID_SIZE):
        if countBits(cellMask[i]) > 1: locked[i] = False
    search()
    return [row[:] for row in finalGrid]