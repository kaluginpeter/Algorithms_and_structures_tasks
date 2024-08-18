# A rectangle is can be defined by two factors: height and width.
#
# Its area is defined as the multiplication of the two: height * width.
#
# Its perimeter is the sum of its four edges: height + height + width + width.
#
# It is possible to create rectangles of the same area but different perimeters. For example, given an area of 45, the possible heights, widths and resultant perimeters would be:
#
# (1, 45) = 92
#
# (9, 5) = 28
#
# (15, 3) = 36
#
# Note that (6, 7.5) has an area of 45 too, but is discarded in this kata because its width is non integral.
#
# The task is to write a function that, given an area as a positive integer, returns the smallest perimeter possible of a rectangle with integral side lengths.
#
# Input range:
# 1 <= area <= 5 x 10 ^ 10
#
# FUNDAMENTALSALGORITHMS
# Solution
def minimum_perimeter(area):
    i = int(area ** .5)
    while area % i:
        i -= 1
    return 2 * i + 2 * (area // i)