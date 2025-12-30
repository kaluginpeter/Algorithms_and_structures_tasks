# Task
# Write a function that takes a chess position and computes all possible sequences of consecutive captures. Kings may be captured like any other piece. (This is a form of chess called Losing Chess - https://en.wikipedia.org/wiki/Losing_chess.) Each sequence of captures must end in a position where the side whose move it is has no captures. The function should return a two-dimensional list, with each sequence of captures being a one-dimensional list in it. The order of the sequences in the list is not important.
#
# Example
# Consider the position below. Uppercase letters denote white pieces and lowercase black. The function will receive positions as shown on the right, but it's easier to describe using the letter/number coordinate system shown on the left. White moves up the board, and it is always white's move in the original position.
#
#   abcdefgh
# 8 ........ 8                    [ [".", ".", ".", ".", ".", ".", ".", "."],
# 7 R..p.... 7                      ["R", ".", ".", "p", ".", ".", ".", "."],
# 6 ........ 6                      [".", ".", ".", ".", ".", ".", ".", "."],
# 5 ........ 5                      [".", ".", ".", ".", ".", ".", ".", "."],
# 4 ......q. 4                      [".", ".", ".", ".", ".", ".", "q", "."],
# 3 ..N..... 3                      [".", ".", "N", ".", ".", ".", ".", "."],
# 2 .P...... 2                      [".", "P", ".", ".", ".", ".", ".", "."],
# 1 ...b.... 1                      [".", ".", ".", "b", ".", ".", ".", "."] ]
#   abcdefgh
# White can capture either (1) a7xd7 (Rxp) or (2) c3xd1 (Nxb). What sequences of captures does each case lead to?
#
# (1) Black can capture the R (now on d7) using the q on g4. Then white's N can capture the b. Then black's q on d7 can capture the N on d1. At that point it's white's move, and no captures are possible, as seen below.
#
#   abcdefgh
# 8 ........ 8
# 7 ........ 7
# 6 ........ 6
# 5 ........ 5
# 4 ........ 4
# 3 ........ 3
# 2 .P...... 2
# 1 ...q.... 1
#   abcdefgh
# (2) After white's c3xd1 (Nxb), black can capture the N with the q. Then white's R captures the p, and black's q takes the R. Again, white has no captures left:
#
#   abcdefgh
# 8 ........ 8
# 7 ...q.... 7
# 6 ........ 6
# 5 ........ 5
# 4 ........ 4
# 3 ........ 3
# 2 .P...... 2
# 1 ........ 1
#   abcdefgh
# So, in this example, the function should return either
#
# [ ["a7xd7", "g4xd7", "c3xd1", "d7xd1"], ["c3xd1", "g4xd1", "a7xd7", "d1xd7"] ]
# or
# [ ["c3xd1", "g4xd1", "a7xd7", "d1xd7"], ["a7xd7", "g4xd7", "c3xd1", "d7xd1"] ]
# If white has no captures in the original position, the function should return [ ]. If different sequences of captures lead to the same board position, they should all be included in the returned list.
#
# Positions where a pawn makes a capture and thereby reaches the eighth rank will not occur. However, the original position might contain promoted pieces - e.g. two or more queens, multiple kings of either color, etc.
#
# GamesListsStringsAlgorithms
# Solution
from copy import deepcopy
files = "abcdefgh"
def in_bounds(r, c):
    return 0 <= r < 8 and 0 <= c < 8

def is_white(p):
    return p.isupper()

def is_black(p):
    return p.islower()

def square_name(r, c):
    return files[c] + str(8 - r)

def compute_all_sequences_of_captures(board):
    results = []

    def gen_captures(board, white_turn):
        captures = []
        for r in range(8):
            for c in range(8):
                p = board[r][c]
                if p == ".":
                    continue
                if white_turn and not is_white(p):
                    continue
                if not white_turn and not is_black(p):
                    continue

                enemy = is_black if white_turn else is_white

                def add_line(dr, dc):
                    rr, cc = r + dr, c + dc
                    while in_bounds(rr, cc):
                        if board[rr][cc] != ".":
                            if enemy(board[rr][cc]):
                                captures.append((r, c, rr, cc))
                            break
                        rr += dr
                        cc += dc

                if p.lower() == "p":
                    d = -1 if white_turn else 1
                    for dc in (-1, 1):
                        rr, cc = r + d, c + dc
                        if in_bounds(rr, cc) and enemy(board[rr][cc]):
                            captures.append((r, c, rr, cc))

                elif p.lower() == "n":
                    for dr, dc in [(2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)]:
                        rr, cc = r + dr, c + dc
                        if in_bounds(rr, cc) and enemy(board[rr][cc]):
                            captures.append((r, c, rr, cc))

                elif p.lower() == "b":
                    for dr, dc in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                        add_line(dr, dc)

                elif p.lower() == "r":
                    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        add_line(dr, dc)

                elif p.lower() == "q":
                    for dr, dc in [(1,1),(1,-1),(-1,1),(-1,-1),
                                   (1,0),(-1,0),(0,1),(0,-1)]:
                        add_line(dr, dc)

                elif p.lower() == "k":
                    for dr in (-1,0,1):
                        for dc in (-1,0,1):
                            if dr or dc:
                                rr, cc = r + dr, c + dc
                                if in_bounds(rr, cc) and enemy(board[rr][cc]):
                                    captures.append((r, c, rr, cc))
        return captures

    def dfs(board, white_turn, seq):
        caps = gen_captures(board, white_turn)
        if not caps:
            if seq: results.append(seq)
            return

        for r1, c1, r2, c2 in caps:
            b2 = deepcopy(board)
            piece = b2[r1][c1]
            b2[r1][c1] = "."
            b2[r2][c2] = piece
            move = square_name(r1, c1) + "x" + square_name(r2, c2)
            dfs(b2, not white_turn, seq + [move])
    dfs(board, True, [])
    return results