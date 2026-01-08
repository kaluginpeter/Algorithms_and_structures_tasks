# A "Lucky Seven" is the number seven surrounded by numbers that add up to form a perfect cube. The surrounding numbers will be described as the numbers directly above, below, and next to (not diagonally) the number 7. You will be given a 2D array containing at least 1 lucky seven. Your function should return the number of lucky sevens in the array.
#
# Here are some "Lucky Sevens" for example:
#
# [ [ 'x', 513, 'x', 'x', 'x' ],
#   [ 82,   7,  32,  'x', 'x' ],
#   [ 'x', 102, 'x', 'x', 'x' ],
#   [ 'x', 'x', 'x', 'x', 'x' ],
#   [ 'x', 'x', 'x', 'x', 'x' ] ]
#
# [ [ 'x', 'x', 'x', 'x', 'x' ],
#   [ 'x', 'x', 'x', 'x', 'x' ],
#   [ 'x', 'x', 'x', 'x', 'x' ],
#   [ 'x', 'x', 'x', 'x',  9  ],
#   [ 'x', 'x', 'x', 55,   7  ] ]
#
# [ [ 'x', 'x', 'x', 'x', 'x' ],
#   [ 'x',  1,  'x', 'x', 'x' ],
#   [  0,   7,   0,  'x', 'x' ],
#   [ 'x',  0,  'x', 'x', 'x' ],
#   [ 'x', 'x', 'x', 'x', 'x' ] ]
# Good luck!
#
# Fundamentals
# Solution
from math import cbrt

moves: list[tuple[int, int]] = [
    (1, 0), (-1, 0), (0, 1), (0, -1)
]
def lucky_sevens(arr: list[list[int]]) -> int:
    output: int = 0
    n: int = len(arr)
    m: int = len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 7: continue
            cube: int = 0
            for x, y in moves:
                ni: int = i + x
                nj: int = j + y
                if not (0 <= ni < n) or not (0 <= nj < m): continue
                cube += arr[ni][nj]
            if cube != int(cbrt(cube))**3: continue
            output += 1
    return output