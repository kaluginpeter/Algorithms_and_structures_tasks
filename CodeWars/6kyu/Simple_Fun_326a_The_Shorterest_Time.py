# Task
# John is a programmer. He treasures his time very much. He lives on the n floor of a building. Every morning he will go downstairs as quickly as possible to begin his great work today.
#
# There are two ways he goes downstairs: walking or taking the elevator.
#
# When John uses the elevator, he will go through the following steps:
#
# 1. Waiting the elevator from m floor to n floor;
# 1a. Or take the stairs to m floor;
# 2. Waiting the elevator open the door and go in;
# 3. Waiting the elevator close the door;
# 4. Waiting the elevator down to 0 floor;
# 5. Waiting the elevator open the door and go out;
# (the time of go in/go out the elevator will be ignored)
# Given the following arguments:
#
# n: An integer. The floor of John(0-based).
# m: An integer. The floor of the elevator(0-based).
# speeds: An array of integer. It contains four integer [a,b,c,d]
#         a: The seconds required when the elevator rises or falls 1 floor
#         b: The seconds required when the elevator open the door
#         c: The seconds required when the elevator close the door
#         d: The seconds required when John walks to n-1 or n+1 floor
# Please help John to calculate the shortest time to go downstairs.
#
# Example
# For n = 4, m = 5 and speeds = [1,2,3,10], the output should be 12.
#
# John go downstairs by using the elevator:
#
# 1 + 2 + 3 + 4 + 2 = 12
#
# For n = 0, m = 5 and speeds = [1,2,3,10], the output should be 0.
#
# John is already at 0 floor, so the output is 0.
#
# For n = 4, m = 3 and speeds = [2,3,4,5], the output should be 20.
#
# John go downstairs by walking:
#
# 5 x 4 = 20
#
# For n = 7, m = 6 and speeds = [3,1,1,4], the output should be 25.
#
# John walks down 1 floor and takes the elevator from there.
#
# 1×4 + 1 + 1 + 6×3 + 1 = 25
#
# Pure walk would have taken 7×4 = 28; pure elevator would have taken 1×3 + 1 + 1 + 7×3 + 1 = 27.
#
# Note
# These are Dutch floors. They are numbered 0-based. (0 is usually called "begane grond".)
#
# PuzzlesGamesFundamentals
# Solution
def shorterest_time(n, m, speeds):
    a, b, c, d = speeds
    if n == 0: return 0
    ans = n * d
    for k in range(1, n + 1):
        t = (
            (n - k) * d +
            abs(m - k) * a +
            b +
            c +
            k * a +
            b
        )
        ans = min(ans, t)
    return ans