
# Given an array of seats, return the maximum number of new people which can be seated, as long as there is at least a gap of 2 seats between people.
#
# Empty seats are given as 0.
# Occupied seats are given as 1.
# Don't move any seats which are already occupied, even if they are less than 2 seats apart. Consider only the gaps between new seats and existing seats.
# Examples
# [0, 0, 0, 1, 0, 0, 1, 0, 0, 0] ➞ 2
# // [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
#
# [0, 0, 0, 0] ➞ 2
# // [1, 0, 0, 1]
#
# [1, 0, 0, 0, 0, 1] ➞ 0
# // There is no way to have a gap of at least 2 chairs when adding someone else.
# Notes
# Notice how there may be several possibilities for assigning seats to people, but these cases won't affect the results.
# All seats will be valid.
# ArraysLogic
# Solution
def check(lst: list[int] , i: int) -> bool:
    left: bool = True
    for j in range(i, max(-1, i - 3), -1):
        if lst[j]: left = False
    right: bool = True
    for j in range(i, min(len(lst), i + 3)):
        if lst[j]: right = False
    return left and right

def maximum_seating(lst):
    output: int = 0
    n: int = len(lst)
    left: int = 0
    while left < n:
        if check(lst, left):
            output += 1
            left += 3
        else: left += 1
    return output