# Two robots are placed on a 2D XY-plane grid at positions (x1, y1) and (x2, y2) respectively. A command sequence consisting of the characters U, D, L, and R is given to both robots:
#
# U: Move up by one unit
# D: Move down by one unit
# L: Move left by one unit
# R: Move right by one unit
# Since both robots follow the exact same commands at the same time, they move in the same direction each step. This means their movement patterns are identical, just shifted by their starting positions — so unless they started in the same spot, they’ll never collide.
#
# However, there’s a catch: due to a programming glitch, a robot may occasionally miss a command — that is, it might skip a move at any step.
#
# (A robot can skip any number of commands, and both robots may skip the same or different commands independently.)
#
# If at any point during the execution of the command sequence both robots occupy the same position, they collide and explode.
#
# Your task:
# Given the initial coordinates of both robots and the command sequence, determine if there is any possibility that the two robots collide at any point in time, due to the skipped commands.
#
# Examples:
# Example 1
# Inputs: x1 = 0, y1 = 0, x2 = 1, y2 = 0, commands = "UL"
#
# Output: true
#
# Explanation: If Robot 1 skips "L" the command and Robot 2 doesn't skip any, there will be a collision.
#
# Example 2
# Inputs: x1 = 0, y1 = 0, x2 = 0, y2 = 1, commands = "LRLR"
#
# Output: false
#
# Explanation: Their vertical positions differ (y1=0 and y2=1), and none of the commands affect the y-axis.
#
# Constraints
# 0 <= x1, y1, x2, y2 <= 500
# 0 <= len(commands) <= 500
# Performance
# Solution
def will_robots_collide(x1, y1, x2, y2, commands):
    for move in commands:
        if move == 'U' and y1 < y2: y1 += 1
        elif move == 'D' and y1 > y2: y1 -= 1
        elif move == 'L' and x1 > x2: x1 -= 1
        elif move == 'R' and x1 < x2: x1 += 1
    for move in commands:
        if move == 'U' and y2 < y1: y2 += 1
        elif move == 'D' and y2 > y1: y2 -= 1
        elif move == 'L' and x2 > x1: x2 -= 1
        elif move == 'R' and x2 < x1: x2 += 1
    return x1 == x2 and y1 == y2