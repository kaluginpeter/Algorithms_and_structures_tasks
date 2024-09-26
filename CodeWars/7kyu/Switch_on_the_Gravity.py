# Given a 2D array of some suspended blocks (represented as hastags), return another 2D array which shows the end result once gravity is switched on.
#
# Examples
# switch_gravity([
#   ["-", "#", "#", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"]
# ]) ➞ [
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "#", "#", "-"]
# ]
#
# switch_gravity([
#   ["-", "#", "#", "-"],
#   ["-", "-", "#", "-"],
#   ["-", "-", "-", "-"],
# ]) ➞ [
#   ["-", "-", "-", "-"],
#   ["-", "-", "#", "-"],
#   ["-", "#", "#", "-"]
# ]
#
# switch_gravity([
#   ["-", "#", "#", "#", "#", "-"],
#   ["#", "-", "-", "#", "#", "-"],
#   ["-", "#", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-", "-"]
# ]) ➞ [
#   ["-", "-", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-", "-"],
#   ["-", "#", "-", "#", "#", "-"],
#   ["#", "#", "#", "#", "#", "-"]
# ]
# Notes
# Each block falls individually, meaning there are no rigid objects. Think about it like falling sand in Minecraft as opposed to the rigid blocks in Tetris.
#
# ALGORITHMSMATRIXARRAYS
def switch_gravity(lst):
    for cur_col in range(len(lst[0])):
        cur_row: int = len(lst) - 1
        while cur_row >= 0 and lst[cur_row][cur_col] == '#':
            cur_row -= 1
        if cur_row < 0: continue
        for row in range(cur_row, -1, -1):
            if lst[row][cur_col] == '#':
                lst[cur_row][cur_col], lst[row][cur_col] = lst[row][cur_col], lst[cur_row][cur_col]
                cur_row -= 1
    return lst