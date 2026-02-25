# This kata is inspired by davazp's one
# Context
# So, here we go again:
#
# You are given an ASCII diagram, containing minus signs "-", plus signs "+", vertical bars "|" and whitespaces " " . Your task is to write a function which will break the diagram in the minimal pieces it is made of.
#
# For example, if the input of your function is the diagram on the left below, the expected answer will be the list of strings representing the three individual shapes on the right (note how the biggest shape lost a "+" sign in the extraction) :
#
# Input:                          Expected:
# +------------+                  +------------+
# |            |                  |            |    +------+    +-----+
# |            |                  |            |    |      |    |     |
# |            |                  |            |    |      |    |     |
# +------+-----+                  +------------+    +------+    +-----+
# |      |     |
# |      |     |
# +------+-----+
# If you encounter imbricated pieces, both outer and inner shapes have to be returned. For example:
#
# Input:                          Expected:
# +------------+                  +------------+
# |            |                  |            |
# |    +--+    |                  |    +--+    |
# |    |  |    |                  |    |  |    |
# |    |  |    |                  |    |  |    |    +--+
# |    +--+    |                  |    +--+    |    |  |
# |            |                  |            |    |  |
# +------------+                  +------------+    +--+
# So... What's new!?
# What is new in this "evilized" version is that you'll have to manage the extraction of shapes without inner whitespaces.
#
# For example, the input below should lead to the following list of strings:
#
# Input:                          Expected:
# +------------+                  +------------+
# |            |                  |            |    +------+    +----+    ++
# |            |                  |            |    |      |    |    |    ||
# |            |                  |            |    |      |    |    |    ||
# +------++----+                  +------------+    +------+    +----+    ++
# |      ||    |
# |      ||    |
# +------++----+
# From there, you'll have two approaches...:
#
# The "easy" (better) one...
# ... or the hard one: if you stumble frequently going through the fixed tests, might be you didn't made the right move and you're on this path. It's doable that way either, but it is way harder than the other one (1 or 2 kyu ranks higher! But if you like challenges, you can try that really evilized way... ;) )
# TASK
# You have to find all the individual pieces contained in the original diagram. Note that you are only searching for the smallest possible ones.
#
# You may find below some important indications about what you will have to deal with:
#
# The pieces should not have any spaces on their right (ie. no trailing spaces).
#
# However, they could have leading spaces if the figure is not a rectangle, as shown below:
#
#     +---+
#     |   |
# +---+   |
# |       |
# +-------+
# It is not allowed to use more leading spaces than necessary. It is to say, the first character of at least one of the lines has to be different from a space.
#
# Only explicitly closed pieces have to be considered (meaning, in the diagram above, there is one and only one piece).
#
# The borders of each shape have to contain only the meaningful plus signs "+" (those in corners or at the intersections of several straight lines).
#
# Keep an eye on the performances. You won't have to make your code unreadable to pass the tests, but be clever with what you choose to implement.
#
# After all of that, you still will have to pass the random tests...
#
# Note: In the display, to make it easier to see where whitespaces are or not, the spaces characters will be replaced with dots:
#
#  ```
#     +---+              ....+---+                  +---+                  +---+
#     |   |              ....|...|                  |   |                  |...|..      <- there are spaces here, on the right
# +---+   |      =>      +---+...|                  |   +---+      =>      |...+---+
# |       |              |.......|                  |       |              |.......|
# +-------+              +-------+                  +-------+              +-------+
# ```
#
# Input
# The diagrams are given as ordinary multiline strings of various lengths.
# Output
# A list of multilines strings (see the example tests).
# The order of the individual shapes in the list does not matter.
#
# Final notes...
# If you're following the "hard path", this kata might make you crazy...
# Tests design: about 80 fixed tests (each of them doubled) and the random ones with shapes up to around 80x80 characters (100 for python and ruby, 200 for Rust and 250 for Java). If your solution times out, do not hesitate to do a second try before to do any modification to your code.
# GamesAlgorithmsPuzzles
# Solution
USE_BREAK_DISPLAY = True

fn = lambda col: {(col[0] + 1, col[1]), (col[0] - 1, col[1]), (col[0], col[1] + 1), (col[0], col[1] - 1)}
fn8 = lambda c: {(c[0] + i, c[1] + j) for i in {1, -1, 0} for j in {1, -1, 0}}
fvn = lambda c: {(c[0] + 1, c[1]), (c[0] - 1, c[1])}
fhn = lambda c: {(c[0], c[1] + 1), (c[0], c[1] - 1)}

def traverse(s):
    shape = s.split('\n')
    while not shape[0].strip(): shape = shape[1:]
    while not shape[-1].strip(): shape = shape[:-1]
    lines = len(shape)
    max_len_line = max(len(shape[line]) for line in range(lines))
    for row in range(lines): shape[row] += ' ' * (max_len_line - len(shape[row]))
    new_shape = [[]] * (2 * lines - 1)
    for row in range(2 * lines - 1):
        new_shape[row] = [' '] * (2 * max_len_line - 1)
        if row % 2:
            for col in range(max_len_line):
                if shape[row // 2][col] in '|+' and shape[row // 2 + 1][col] in '|+': new_shape[row][2 * col] = '|'
        else:
            for col in range(2 * max_len_line - 1):
                if col % 2:
                    if shape[row // 2] [col // 2] in '-+' and shape[row // 2][col // 2 + 1] in '-+': new_shape[row][col] = '-'
                else: new_shape[row][col] = shape[row // 2][col // 2]
    return 2 * lines - 1, 2 * max_len_line - 1, new_shape

def break_evil_pieces(shape):
    if not shape.strip(): return []
    (rows, cols, shape) = traverse(shape)
    empty_spaces = {(row, col) for row in range(rows) for col in range(cols) if shape[row][col] == ' '}
    regions = []
    while empty_spaces:
        R = {empty_spaces.pop()}
        row_empty_neighbors = R
        while row_empty_neighbors:
            row_empty_neighbors = {j for i in row_empty_neighbors for j in fn(i) & empty_spaces} - R
            R.update(row_empty_neighbors)
        empty_spaces = empty_spaces - R
        boundary = {j for i in R for j in fn8(i)} - R
        mnrow: int = min(row for row, col in boundary)
        mxrow: int = max(row for row, col in boundary) + 1
        mncol: int = min(col for row, col in boundary)
        mxcol: int = max(col for row, col in boundary) + 1
        if mnrow < 0 or mncol < 0 or mxrow > rows or mxcol > cols: continue
        region = [list(row[mncol:mxcol]) for row in shape[mnrow:mxrow]]
        for row in range(len(region)):
            for col in range(len(region[row])):
                if region[row][col] != ' ' and (row + mnrow, col + mncol) not in boundary: region[row][col] = ' '
                elif region[row][col] == '+':
                    c = (row + mnrow, col + mncol)
                    if not (fhn(c) & boundary and fvn(c) & boundary): region[row][col] = '-' if fhn(c) & boundary else '|'
        regions.append('\n'.join(''.join(row[::2]).rstrip() for row in region[::2]))
    return regions