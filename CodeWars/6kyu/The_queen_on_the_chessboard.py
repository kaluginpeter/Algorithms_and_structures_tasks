# In chess, the queen can be moved across any number of unoccupied squares in a straight line vertically, horizontally, or diagonally, thus combining the moves of the rook and bishop.
#
# Task
# Given the square of a queen on a chessboard, your function must output an array of the squares the queen can move to. Squares are represented as strings using chess algebraic notation.
#
# Input
# A valid input position is a string of one letter from A to H followed by a digit from 1 to 8, for example "A1", "C8", "B3".
# If the input is anything else (e.g. not a string, or an invalid position such as A10 or H0), return an empty array.
# Output
# An array of positions (strings). It should be sorted in lexicographical order and should not include the starting square of the queen.
#
# Example
# For example when input position is A1 return value should be:
#
# ["A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "C1", "C3", "D1", "D4", "E1", "E5", "F1", "F6", "G1", "G7", "H1", "H8"]
#      A   B   C   D   E   F   G   H
#    + - + - + - + - + - + - + - + - +
# 1  | Q | x | x | x | x | x | x | x |
#    + - + - + - + - + - + - + - + - +
# 2  | x | x |   |   |   |   |   |   |
#    + - + - + - + - + - + - + - + - +
# 3  | x |   | x |   |   |   |   |   |
#    + - + - + - + - + - + - + - + - +
# 4  | x |   |   | x |   |   |   |   |
#    + - + - + - + - + - + - + - + - +
# 5  | x |   |   |   | x |   |   |   |
#    + - + - + - + - + - + - + - + - +
# 6  | x |   |   |   |   | x |   |   |
#    + - + - + - + - + - + - + - + - +
# 7  | x |   |   |   |   |   | x |   |
#    + - + - + - + - + - + - + - + - +
# 8  | x |   |   |   |   |   |   | x |
#    + - + - + - + - + - + - + - + - +
#
# Q = queen
# x = available move
# ArraysFundamentals
def available_moves(position) -> list[str]:
    output: list[str] = []
    if not isinstance(position, str) or len(position) != 2 or not position[1].isdigit() or not position[0].isupper():
        return output
    i: int = ord(position[0]) - 64
    j: int = int(position[1])
    if not (1 <= j <= 8) or not (1 <= i <= 8): return output
    # upper left direciton
    i_: int = i - 1
    j_: int = j - 1
    while i_ and j_:
        output.append(chr(i_ + 64) + str(j_))
        i_ -= 1
        j_ -= 1
    # upper right direction
    i_ = i - 1
    j_ = j + 1
    while i_ and j_ < 9:
        output.append(chr(i_ + 64) + str(j_))
        i_ -= 1
        j_ += 1
    # lower left direction
    i_ = i + 1
    j_ = j - 1
    while i_ < 9 and j_:
        output.append(chr(i_ + 64) + str(j_))
        i_ += 1
        j_ -= 1
    # lower right direction
    i_ = i + 1
    j_ = j + 1
    while i_ < 9 and j_ < 9:
        output.append(chr(i_ + 64) + str(j_))
        i_ += 1
        j_ += 1
    # left direction
    j_ = j - 1
    while j_:
        output.append(chr(i + 64) + str(j_))
        j_ -= 1
    # right direction
    j_ = j + 1
    while j_ < 9:
        output.append(chr(i + 64) + str(j_))
        j_ += 1
    # up direction
    i_ = i - 1
    while i_:
        output.append(chr(i_ + 64) + str(j))
        i_ -= 1
    # down direction
    i_ = i + 1
    while i_ < 9:
        output.append(chr(i_ + 64) + str(j))
        i_ += 1
    output.sort()
    return output