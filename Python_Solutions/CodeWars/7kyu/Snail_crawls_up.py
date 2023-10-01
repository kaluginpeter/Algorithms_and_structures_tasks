# The snail crawls up the column. During the day it crawls up some distance. During the night she sleeps, so she slides down for some distance (less than crawls up during the day).
#
# Your function takes three arguments:
#
# The height of the column (meters)
# The distance that the snail crawls during the day (meters)
# The distance that the snail slides down during the night (meters)
# Calculate number of day when the snail will reach the top of the column.
#
# FUNDAMENTALSMATHEMATICS
# Solution
def snail(column, day, night):
    count = 0
    while column > 0:
        count += 1
        if column - day <= 0:
            return count
        column -= day - night
    return count