# Task
# You are given an 2D array arr, find out the largest "X" hidden in the array.
#
# Rules
# A "X" in the 2D array like this:
#
# [
# ["X"," "," "," ","X"],
# [" ","X"," ","X"," "],
# [" "," ","X"," "," "],
# [" ","X"," ","X"," "],
# ["X"," "," "," ","X"]
# ]
# Of course, the "X" can also be made of other letters:
#
# [
# ["A"," "," "," ","A"],
# [" ","A"," ","A"," "],
# [" "," ","A"," "," "],
# [" ","A"," ","A"," "],
# ["A"," "," "," ","A"]
# ]
# Of course, the location of the space can also be other characters, so it is more difficult to distinguish:
#
# [
# ["A","B","C","D","A"],
# ["P","A","Q","A","E"],
# ["N","O","A","H","F"],
# ["M","A","K","A","G"],
# ["A","L","J","I","A"]
# ]
# Can you find this "X"? Please return the location of the center of "X" using an array [row,column].
#
# If there are more than one "X" in the array, you should return the location of the largest "X"; If there are two or more "X" have the same length, please return the first one(In order from top to bottom, from left to right); If no "X" found, return []
#
# See more examples in the example testcases ;-)
#
# PuzzlesGames
# Solution
def largest_x(arr):
    n = len(arr)
    m = len(arr[0])
    best_size = 0
    best_pos = []
    for r in range(n):
        for c in range(m):
            ch = arr[r][c]
            size = 0
            while True:
                nr1, nc1 = r - size, c - size
                nr2, nc2 = r - size, c + size
                nr3, nc3 = r + size, c - size
                nr4, nc4 = r + size, c + size
                if (
                    nr1 < 0 or nc1 < 0 or
                    nr2 < 0 or nc2 >= m or
                    nr3 >= n or nc3 < 0 or
                    nr4 >= n or nc4 >= m
                ):
                    break
                if not (
                    arr[nr1][nc1] == ch and
                    arr[nr2][nc2] == ch and
                    arr[nr3][nc3] == ch and
                    arr[nr4][nc4] == ch
                ):
                    break
                size += 1
            arm = size - 1
            if arm > best_size:
                best_size = arm
                best_pos = [r, c]
    return best_pos if best_size > 0 else []