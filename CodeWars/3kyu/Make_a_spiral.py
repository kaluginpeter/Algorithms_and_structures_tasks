# Your task, is to create a NxN spiral with a given size.
#
# For example, spiral with size 5 should look like this:
#
# 00000
# ....0
# 000.0
# 0...0
# 00000
# and with the size 10:
#
# 0000000000
# .........0
# 00000000.0
# 0......0.0
# 0.0000.0.0
# 0.0..0.0.0
# 0.0....0.0
# 0.000000.0
# 0........0
# 0000000000
# Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given size 5 result should be:
#
# [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Because of the edge-cases for tiny spirals, the size will be at least 5.
#
# General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
#
# ALGORITHMSARRAYSLOGIC
# Solution
def check_right(output, up, right, n):
    moves = [[-1, 1], [1, 1]]
    for m in moves:
        x, y = m
        if (not 0 <= up + x <= n - 1) or (not 0 <= right + y <= n - 1):
            continue
        if output[up + x][right + y] == 1:
            return False
    return True

def check_left(output, up, right, n):
    moves = [[1, -1], [-1, -1]]
    for m in moves:
        x, y = m
        if (not 0 <= up + x <= n - 1) or (not 0 <= right + y <= n - 1):
            continue
        if output[up + x][right + y] == 1:
            return False
    return True

def spiralize(size):
    right, up = 0, 0
    output: list[list[int]] = [[0 for _ in range(size)] for _ in range(size)]
    n: int = size
    for rep in range(n):

        for i in range(size - 1):
            if not check_right(output, up, right, n):
                break
            if output[up][min(right + 1, n - 1)] == 1:
                break
            output[up][right] = 1
            if output[up][min(right + 2, n - 1)] == 1:
                break
            right += 1

        for i in range(size - 1):
            if output[min(up + 1, n - 1)][right] == 1:
                break
            output[up][right] = 1
            if output[min(up + 2, n - 1)][right] == 1:
                break
            up += 1

        for i in range(size - 1):
            if not check_left(output, up, right, n):
                break
            if output[up][max(0, right - 1)] == 1:
                break
            output[up][right] = 1
            if output[up][max(0, right - 2)] == 1:
                break
            right -= 1
            move_left = True
        size -= 2

        for i in range(size - 1):
            if output[max(0, up - 1)][right] == 1:
                break
            output[up][right] = 1
            if output[max(0, up - 2)][right] == 1:
                break
            up -= 1
        if size <= 0: break
    return output