# Do you know how to make a spiral? Let's test it!
# Classic definition: A spiral is a curve which emanates from a central point, getting progressively farther away as it revolves around the point.
#
# Your objective is to complete a function createSpiral(N) that receives an integer N and returns an NxN two-dimensional array with numbers 1 through NxN represented as a clockwise spiral.
#
# Return an empty array if N < 1 or N is not int / number
#
# Examples:
#
# N = 3 Output: [[1,2,3],[8,9,4],[7,6,5]]
#
# 1    2    3
# 8    9    4
# 7    6    5
# N = 4 Output: [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
#
# 1   2   3   4
# 12  13  14  5
# 11  16  15  6
# 10  9   8   7
# N = 5 Output: [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
#
# 1   2   3   4   5
# 16  17  18  19  6
# 15  24  25  20  7
# 14  23  22  21  8
# 13  12  11  10  9
# ARRAYSPUZZLES
# Solution
def create_spiral(n):
    if not isinstance(n, int) or n < 1:
        return []
    l = [None] * n
    for i in range(n):
        l[i] = [None] * n
    x, y, dx, dy = 0, 0, 1, 0
    for i in range(n*n):
        l[y][x] = i+1
        test = x + dx if dx else y + dy
        if test < 0 or test == n or l[y + dy][x + dx] != None:
            dx, dy = -dy, dx
        x += dx
        y += dy
    return l