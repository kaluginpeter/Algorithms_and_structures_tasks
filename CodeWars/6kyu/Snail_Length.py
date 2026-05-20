# This kata was inspired by this kata. You do not need either kata to solve the other.
#
# Task
# The figure below shows the snail coordinates. The sequence of its points begins as follows: (0, 0), (1, 0), (1, 1), (-1, 1), ....Bpgn7st.md.png
#
# The spiral:
#
# starts by moving right,
# then continues counterclockwise,
# expanding outward forever.
# Given the coordinates (x, y), return the length of the line connecting the coordinate to the origin (0,0) following this snail-like path.
#
# Examples
# snail_length(-2, -1) => 19
# Explanation:
#
# The spiral reaches (-2,-1) after completing two full spirals, shown in the image above.
#
# The value at (-2,-1) is 19.
#
# snail_length(8,10) => 382
# Explanation:
#
# The spiral fills points in expanding square layers around the origin.
#
# By the time the spiral reaches the outer boundary containing (8,10), all previous layers are already filled.
#
# From the structure of the outer ring, (10,10) is reached first, and (8,10) is a few steps back along the same edge, giving a final value of 382.
#
# Constraints
# x
# ,
# y
# ∈
# [
# −
# 5
# ∗
# 1
# 0
# 4
# ,
# 5
# ∗
# 1
# 0
# 4
# ]
# x,y∈[−5∗10
# 4
#  ,5∗10
# 4
#  ]
#
# A naive solution that simply walks the line from (0,0) to (x,y) will NOT pass. You have to think of a faster solution.
#
# AlgorithmsMathematics
# Solution
def snail_length(x, y):
    if x == 0 and y == 0: return 0
    k = max(abs(x), abs(y))
    mx = (2 * k + 1) ** 2 - 1
    if y == -k: return mx - (k - x)
    if x == -k: return mx - 2 * k - (y + k)
    if y == k: return mx - 4 * k - (x + k)
    return mx - 6 * k - (k - y)