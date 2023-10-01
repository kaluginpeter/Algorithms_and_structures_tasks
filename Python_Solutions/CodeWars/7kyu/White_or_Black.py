# Complete the function that returns the color of the given square on a normal, 8x8 chess board:
#
# chessboard
#
# Examples
# "a", 8  ==>  "white"
# "b", 2  ==>  "black"
# "f", 5  ==>  "white"
# ALGORITHMS
# Solution
def square_color(file, c):
    return 'white' if (ord(file) + c) % 2 else 'black'