# The following figure shows a cell grid with 6 cells (2 rows by 3 columns), each cell separated from the others by walls:
#
# +--+--+--+
# |  |  |  |
# +--+--+--+
# |  |  |  |
# +--+--+--+
# This grid has 6 connectivity components of size 1. We can describe the size and number of connectivity components by the list [(1, 6)], since there are 6 components of size 1.
#
# If we tear down a couple of walls, we obtain:
#
# +--+--+--+
# |  |     |
# +  +--+--+
# |  |  |  |
# +--+--+--+
# , which has two connectivity components of size 2 and two connectivity components of size 1. The size and number of connectivity components is described by the list [(2, 2), (1, 2)].
#
# Given the following grid:
#
# +--+--+--+
# |     |  |
# +  +--+--+
# |     |  |
# +--+--+--+
# we have the connectivity components described by [(4, 1), (1, 2)].
#
# Your job is to define a function components(grid) that takes as argument a string representing a grid like in the above pictures and returns a list describing the size and number of the connectivity components. The list should be sorted in descending order by the size of the connectivity components. The grid may have any number of rows and columns.
#
# Note: The grid is always rectangular and will have all its outer walls. Only inner walls may be missing. The + are considered bearing pillars, and are always present.
#
# StringsAlgorithmsGraph Theory