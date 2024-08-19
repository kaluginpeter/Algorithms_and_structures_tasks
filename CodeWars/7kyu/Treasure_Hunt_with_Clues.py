# Inputs:
#
# A n × n grid with 1 ≤ n ≤ 9, and 2 integers row,col with 1 ≤ row,col ≤ n, indicating the starting position of the treasure hunt.
#
# Clues:
#
# Every cell of the grid contains a number between 11 and n2. These values provide the coordinates of the next cell to search. The treasure is found in a cell whose value matches its location. (The clue says "stay where you are"!) There will always be treasure reachable from the starting position.
#
# Output:
#
# The value in the treasure cell reached by following the clues from the starting position.
#
# Example:
#
# Consider the grid below, with starting position row=3,col=4.
# 34 21 32 44 25
# 21 41 43 14 31
# 31 45 52 42 23
# 33 15 51 44 35
# 21 52 33 13 44
#
# Indexes start from 1, so the value in cell 3,4 is 42. Thus the next clue is found in cell 4,2. The value there is 15. Seeking in cell 1,5 uncovers the clue 25, and cell 2,5 contains 31. Since the value in cell 3,1 is 31, that is the location of the treasure.
#
# Source: This kata extends a problem found on GitHub.
#
# Other Treasure-Hunt Kata:
#
# Bob's Treasure Map
#
# Treasure Map
#
# Pirate treasure chest codes
#
# Treasure hunt
#
# ARRAYS
# Solution
def find_treasure(grid, row, col):
    while row * 10 + col != grid[row - 1][col - 1]:
        row, col = grid[row - 1][col - 1] // 10, grid[row - 1][col - 1] % 10
    return grid[row - 1][col - 1]