# Given an array representing the height of towers on a 2d plane, with each tower being of width 1, Whats's the maximum amount of units of water that can be captured between the towers when it rains?
#
# Each tower is immediately next to the tower next to it in the array, except in instances where a height of 0 is shown, then no tower would be present.
#
# A single unit can be thought of as a 2d square with a width 1.
#
# Examples
#           [5,2,10] should return 3
#   [1,0,5,2,6,3,10] should return 7
# [15,0,6,10,11,2,5] should return 20
#            [1,5,1] should return 0
#              [6,5] should return 0
#                 [] should return 0
# Performances:
# Watch out for performances: you'll need a solution linear with the number of towers.
#
# PUZZLESMATHEMATICSALGORITHMS
# Solution Two Pointers O(N) O(1)
def rain_volume(towers):
    if not towers:
        return 0
    left, left_boundary = 0, 0
    mx_idx: int = 0
    ans: int = 0
    for i in range(len(towers)):
        mx_idx = i if towers[i] > towers[mx_idx] else mx_idx
    while left < mx_idx:
        if towers[left] > left_boundary:
            left_boundary = towers[left]
        ans += left_boundary - towers[left]
        left += 1
    right_boundary = towers[-1]
    for i in range(len(towers) - 1, left, -1):
        if towers[i] > right_boundary:
            right_boundary = towers[i]
        ans += right_boundary - towers[i]
    return ans