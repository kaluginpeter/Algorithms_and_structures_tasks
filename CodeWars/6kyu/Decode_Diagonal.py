# Decode the diagonal.
# Given a grid of characters. Output a decoded message as a string.
#
# Input
#
#   H Z R R Q
#   D I F C A E A !
#   G H T E L A E
#   L M N H P R F
#   X Z R P E
# Output
#
# HITHERE! (diagonally down right ↘ and diagonally up right ↗ if you can't go further).
#
# The message ends when there is no space at the right up or down diagonal.
#
# To make things even clearer: the same example, but in a simplified view
#
#   H _ _ _ _
#   _ I _ _ _ _ _ !
#   _ _ T _ _ _ E
#   _ _ _ H _ R _
#   _ _ _ _ E
# ALGORITHMS
# Solution
def get_diagonal_code(grid):
    if not grid: return ''
    grid = [floor.split() for floor in grid.split('\n')]
    if len(grid) == 1: return grid[0][0]
    output: list[str] = []
    row = col = 0
    swap: bool = True
    while swap:
        swap = False
        while row < len(grid) and col < len(grid[row]):
            output.append(grid[row][col])
            row, col = row + 1, col + 1
        if row < len(grid): break
        row -= 2

        while row >= 0 and col < len(grid[row]):
            output.append(grid[row][col])
            row, col = row - 1, col + 1
            swap = True

        if row > 0: break
        if row == -1: row = 1
        if col >= len(grid[row]): break
    return ''.join(output)
