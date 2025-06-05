# Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.
#
# The knight is not allowed to move off the board. The board is 8x8.
#
# For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29
#
# For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29
#
# (Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input, output, and expected output; please post them.)
#
# Algorithms
# Solution
def knight(p1, p2):
    seen: list[list[bool]] = [[False] * 9 for _ in range(9)]
    cur_nodes: list[tuple[int, int]] = [(ord(p1[0]) - 96, int(p1[1]))]
    next_nodes: list[tuple[int, int]] = []
    target_r: int = ord(p2[0]) - 96
    target_c: int = int(p2[1])
    moves: list[tuple[int, int]] = [
        (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (1, -2), (-1, -2)
    ]
    step: int = 0
    while cur_nodes:
        for r, c in cur_nodes:
            if r == target_r and c == target_c: return step
            for x, y in moves:
                new_r: int = r + x
                new_c: int = c + y
                if not (1 <= new_r <= 8) or not (1 <= new_c <= 8) or seen[new_r][new_c]: continue
                seen[new_r][new_c] = True
                next_nodes.append((new_r, new_c))
        cur_nodes = next_nodes
        next_nodes = []
        step += 1
    return -1