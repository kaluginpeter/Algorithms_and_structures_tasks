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