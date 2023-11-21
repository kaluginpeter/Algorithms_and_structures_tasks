# Given a list of directions to spin, "left" or "right", return an integer of how many full 360° rotations were made. Note that each word in the array counts as a 90° rotation in that direction.
#
# Worked Example
# ["right", "right", "right", "right", "left", "right"] ➞ 1
# # You spun right 4 times (90 * 4 = 360)
# # You spun left once (360 - 90 = 270)
# # But you spun right once more to make a full rotation (270 + 90 = 360)
# Examples
# ["left", "right", "left", "right"] ➞ 0
#
# ["right", "right", "right", "right", "right", "right", "right", "right"] ➞ 2
#
# ["left", "left", "left", "left"] ➞ 1
# Notes
# Return a positive number.
# All tests will only include the words "right" and "left".
# ALGORITHMSARRAYS
# Solution
def spin_around(lst):
    count = 0
    for i in lst:
        if i == 'left':
            count -= 1
        else:
            count += 1
    return abs(count) // 4