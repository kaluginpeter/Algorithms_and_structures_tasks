# Squared Spiral #2
# Given the coordinates (x,y) of a number on a square spiral, find out what is it's index in the sequence, like the drawings bellow.
#
# Coordinates
#          ...  ←  1,2  ←  2,2
#                           ↑
#                           ↑
#                           ↑
# -1,1  ←  0,1  ←  1,1     2,1
#   ↓               ↑       ↑
#   ↓               ↑       ↑
#   ↓               ↑       ↑
# -1,0     0,0  →  1,0     2,0
#   ↓                       ↑
#   ↓                       ↑
#   ↓                       ↑
# -1,-1 →  0,-1 →  1,-1 →  2,-1
# Numbers
#          ...  ←  013  ←  012
#                           ↑
#                           ↑
#                           ↑
#  004  ←  003  ←  002     011
#   ↓               ↑       ↑
#   ↓               ↑       ↑
#   ↓               ↑       ↑
#  005     000  →  001     010
#   ↓                       ↑
#   ↓                       ↑
#   ↓                       ↑
#  006  →  007  →  008  →  009
# The spiral starts at 0 which is located at coordinates (0,0), number 1 is at (1,0), number 2 is at (1,1), number 3 is at (0,1) and so on. The spiral always starts to the right and goes in an anti-clockwise direction.
#
# 100 fixed tests and another 500 random tests are performed with coordinates ranging from (-100,-100) to (100,100).
#
# GEOMETRYPUZZLES