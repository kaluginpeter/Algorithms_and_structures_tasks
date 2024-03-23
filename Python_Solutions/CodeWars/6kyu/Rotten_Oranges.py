# Wait long enough and a single rotten orange can turn a whole box of oranges to trash.
#
# You will be given a box of oranges. Find out how long it takes until all oranges are rotten.
#
# a rotten orange will rot every neighboring orange (use Von Neumann neighborhood)
# a box of oranges will be given to you as an int[][] orangeBox (or a list of lists orange_box in Python)
# all inner lists have an equal length
# rotten oranges are represented by 2
# fresh oranges are represented by 1
# empty spaces are represented by 0
# return an int value noting the time needed to fully rot the box
# return -1 in case the box will never completely rot
# Example:
# orangeBox:
#
# 2 1 1
# 1 1 1
# orangeBox after 1 time unit:
#
# 2 2 1
# 2 1 1
# orangeBox after 2 time units:
#
# 2 2 2
# 2 2 1
# orangeBox after 3 time units:
#
# 2 2 2
# 2 2 2
# The box is now fully rotten. Result: 3.
#
# FUNDAMENTALS
# Solution
def calc_rot_time(box):
    mtrx: list[int] = [[-1]  + i + [-1] for i in box]
    mtrx.insert(0, [-1] * (len(box[0]) + 2))
    mtrx.append([-1] * (len(box[0]) + 2))
    new_mtrx: list[int] = list()
    mtrx_moves: list[int] = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    hazard: bool = True
    count: int = 0
    while hazard:
        hazard = False
        rows: list[int] = list()
        for i in range(len(mtrx)):
            for j in range(len(mtrx[0])):
                if mtrx[i][j] == 1:
                    for position in mtrx_moves:
                        if mtrx[i + position[0]][j + position[1]] == 2:
                            hazard = True
                            rows.append(2)
                            break
                    else:
                        rows.append(1)
                else:
                    rows.append(mtrx[i][j])
            new_mtrx.append(rows)
            rows = []
        if hazard:
            mtrx = new_mtrx
            new_mtrx = []
            count += 1
    if all(mtrx[i][j] in {0, 2} for j in range(1, len(mtrx[0]) - 1) for i in range(1, len(mtrx) - 1)):
        return count
    return -1