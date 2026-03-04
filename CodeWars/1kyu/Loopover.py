# Everybody likes sliding puzzles! For this kata, we're going to be looking at a special type of sliding puzzle called Loopover. With Loopover, it is more like a flat rubik's cube than a sliding puzzle. Instead of having one open spot for pieces to slide into, the entire grid is filled with pieces that wrap back around when a row or column is slid.
#
# Try it out: https://www.openprocessing.org/sketch/576328
#
# Note: computer scientists start counting at zero!
#
# Your task: return a List of moves that will transform the unsolved grid into the solved one. All values of the scrambled and unscrambled grids will be unique! Moves will be 2 character long Strings like the ones below.
#
# For example, if we have the grid:
#
# ABCDE
# FGHIJ
# KLMNO
# PQRST
# UVWXY
# and we do R0 (move the 0th row right) then we get:
#
# EABCD
# FGHIJ
# KLMNO
# PQRST
# UVWXY
# Likewise, if we do L0 (move the 0th row left), we get:
#
# ABCDE
# FGHIJ
# KLMNO
# PQRST
# UVWXY
# if we do U2 (2nd column up):
#
# ABHDE
# FGMIJ
# KLRNO
# PQWST
# UVCXY
# and if we do D2 (2nd column down) we will once again return to the original grid. With all of this in mind, I'm going to make a Loopover with a scrambled grid, and your solve method will give me a List of moves I can do to get back to the solved grid I give you.
#
# For example:
#
# SCRAMBLED GRID:
#
# DEABC
# FGHIJ
# KLMNO
# PQRST
# UVWXY
# SOLVED GRID:
#
# ABCDE
# FGHIJ
# KLMNO
# PQRST
# UVWXY
# One possible solution would be ["L0", "L0"] as moving the top row left twice would result in the original, solved grid. Another would be ["R0", "R0", "R0"], etc. etc.
#
# NOTE: The solved grid will not always look as nice as the one shown above, so make sure your solution can always get the mixed up grid to the "solved" grid!
#
# Input
# mixedUpBoard and solvedBoard are two-dimensional arrays (or lists of lists) of symbols representing the initial (unsolved) and final (solved) grids.
#
# Different grid sizes are tested: from 2x2 to 9x9 grids (including rectangular grids like 4x5).
#
# Output
# Return a list of moves to transform the mixedUpBoard grid to the solvedBoard grid.
#
# Some configurations cannot be solved. Return null (None in Python/Rust) for unsolvable configurations.
#
# Good luck! Let me know if there are any issues with the kata! :)
#
# PuzzlesAlgorithmsGame Solvers