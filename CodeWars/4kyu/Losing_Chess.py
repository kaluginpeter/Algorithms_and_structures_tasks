# Task
# Write a function that takes a chess position and computes all possible sequences of consecutive captures. Kings may be captured like any other piece. (This is a form of chess called Losing Chess - https://en.wikipedia.org/wiki/Losing_chess.) Each sequence of captures must end in a position where the side whose move it is has no captures. The function should return a two-dimensional list, with each sequence of captures being a one-dimensional list in it. The order of the sequences in the list is not important.
#
# Example
# Consider the position below. Uppercase letters denote white pieces and lowercase black. The function will receive positions as shown on the right, but it's easier to describe using the letter/number coordinate system shown on the left. White moves up the board, and it is always white's move in the original position.
#
#   abcdefgh
# 8 ........ 8                    [ [".", ".", ".", ".", ".", ".", ".", "."],
# 7 R..p.... 7                      ["R", ".", ".", "p", ".", ".", ".", "."],
# 6 ........ 6                      [".", ".", ".", ".", ".", ".", ".", "."],
# 5 ........ 5                      [".", ".", ".", ".", ".", ".", ".", "."],
# 4 ......q. 4                      [".", ".", ".", ".", ".", ".", "q", "."],
# 3 ..N..... 3                      [".", ".", "N", ".", ".", ".", ".", "."],
# 2 .P...... 2                      [".", "P", ".", ".", ".", ".", ".", "."],
# 1 ...b.... 1                      [".", ".", ".", "b", ".", ".", ".", "."] ]
#   abcdefgh
# White can capture either (1) a7xd7 (Rxp) or (2) c3xd1 (Nxb). What sequences of captures does each case lead to?
#
# (1) Black can capture the R (now on d7) using the q on g4. Then white's N can capture the b. Then black's q on d7 can capture the N on d1. At that point it's white's move, and no captures are possible, as seen below.
#
#   abcdefgh
# 8 ........ 8
# 7 ........ 7
# 6 ........ 6
# 5 ........ 5
# 4 ........ 4
# 3 ........ 3
# 2 .P...... 2
# 1 ...q.... 1
#   abcdefgh
# (2) After white's c3xd1 (Nxb), black can capture the N with the q. Then white's R captures the p, and black's q takes the R. Again, white has no captures left:
#
#   abcdefgh
# 8 ........ 8
# 7 ...q.... 7
# 6 ........ 6
# 5 ........ 5
# 4 ........ 4
# 3 ........ 3
# 2 .P...... 2
# 1 ........ 1
#   abcdefgh
# So, in this example, the function should return either
#
# [ ["a7xd7", "g4xd7", "c3xd1", "d7xd1"], ["c3xd1", "g4xd1", "a7xd7", "d1xd7"] ]
# or
# [ ["c3xd1", "g4xd1", "a7xd7", "d1xd7"], ["a7xd7", "g4xd7", "c3xd1", "d7xd1"] ]
# If white has no captures in the original position, the function should return [ ]. If different sequences of captures lead to the same board position, they should all be included in the returned list.
#
# Positions where a pawn makes a capture and thereby reaches the eighth rank will not occur. However, the original position might contain promoted pieces - e.g. two or more queens, multiple kings of either color, etc.
#
# GamesListsStringsAlgorithms