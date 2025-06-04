# Simulate placing tokens on a Connect Four board.
#
# Connect Four Example
# INPUT
# A list of integers representing the columns (from 0 to 6) where tokens are dropped, in order. The first player is yellow (Y), followed by red (R), alternating turns.
#
# OUTPUT
# The final state of the board after all tokens have been placed. Empty cells are marked with -.
#
# ASSUMPTIONS
# The board has 7 columns and 6 rows (standard Connect Four size).
# Tokens fall to the lowest available position in the chosen column.
# All input values are valid and within the allowed range.
# The input list must not be modified.
# Output format: rows are listed from top to bottom, with the top row first and the bottom row last.
# EXAMPLES
# Example 1:
#
# Moves = [0,1,2,5,6]
#
# Result:
# ['-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-']
# ['Y', 'R', 'Y', '-', '-', 'R', 'Y']
# Example 2:
#
# Moves = [0,1,2,5,6,2,0,0]
#
# Result:
# ['-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-']
# ['R', '-', '-', '-', '-', '-', '-']
# ['Y', '-', 'R', '-', '-', '-', '-']
# ['Y', 'R', 'Y', '-', '-', 'R', 'Y']
# ArraysFundamentals