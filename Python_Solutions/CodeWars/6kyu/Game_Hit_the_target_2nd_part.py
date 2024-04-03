# This is the second part of the kata :3 🎈🎆🎇🎆🎈
# given a matrix n x n (2-7), determine if the arrow is directed to the target (x).
# Now there are one of 4 types of arrows ( '^', '>', 'v', '<' ) and only one target (x)
# An empty spot will be denoted by a space " ", the target with a cross "x", and the scope ">"
# Examples:
# given matrix 4x4:
# [
#
#   [' ', 'x', ' ', ' '],
#
#   [' ', ' ', ' ', ' '], --> return true
#
#   [' ', '^', ' ', ' '],
#
#   [' ', ' ', ' ', ' ']
#
# ]
# given matrix 4x4:
# [
#
#   [' ', ' ', ' ', ' '],
#
#   [' ', 'v', ' ', ' '], --> return false
#
#   [' ', ' ', ' ', 'x'],
#
#   [' ', ' ', ' ', ' ']
#
# ]
# given matrix 4x4:
# [
#
#   [' ', ' ', ' ', ' '],
#
#   ['>', ' ', ' ', 'x'], --> return true
#
#   [' ', '', ' ', ' '],
#
#   [' ', ' ', ' ', ' ']
#
# ]
#
# In this example, only a 4x4 matrix was used, the problem will have matrices of dimensions from 2 to 7
# And here is the first part of this kata - click me ●v●
# Happy hacking as they say! 💻
#
# MATRIXARRAYSSTRINGSFUNDAMENTALS
# Solution
def solution(mtrx):
    for rows in range(len(mtrx)):
        for columns in range(len(mtrx[0])):
            if mtrx[rows][columns] == '^':
                x: int = rows
                while x > 0:
                    x -= 1
                    if mtrx[x][columns] == 'x':
                        return True
                return False
            elif mtrx[rows][columns] == 'v':
                x: int = rows
                while x < len(mtrx) - 1:
                    x += 1
                    if mtrx[x][columns] == 'x':
                        return True
                return False
            elif mtrx[rows][columns] == '>':
                x: int = columns
                while x < len(mtrx[0]) - 1:
                    x += 1
                    if mtrx[rows][x] == 'x':
                        return True
                return False
            elif mtrx[rows][columns] == '<':
                x: int = columns
                while x > 0:
                    x -= 1
                    if mtrx[rows][x] == 'x':
                        return True
                return False
    return False