# In this kata you have a 20 x 20 preloaded array of oil saturation in some region. Your task is to answer whether it is efficient to place the well at the given point. A well is efficient if its efficiency is bigger or equal to given threshold.
#
# Input parameters in that function are:
#
# x and y integer coordinates of the well (indexes of 2D array, using x for rows, y for columns)
# efficiency threshold (float or integer)
# The preloaded FIELD contains values from 0.00 to 0.99 inclusive, such as:
#
# 0.98, 0.65, 0.23, 0.39, 0.99...
# (In Python and Ruby each value is stored as a float. In C each value is stored as a double)
#
# Examples of usage:
#
# x = 10
# y = 10
# threshold = 3.5
# expected result => True / true
#
# x = 7
# y = 3
# threshold = 4.5
# expected result => False / false
# To calculate the current efficiency of a well, you should sum up all saturations of cells adjacent to the specified cell plus the saturation of the specified cell itself.
#
# The efficiency of the marked point with 0.43 is 5.3 (sum of all cells in square).
#
# If you need to calculate the efficiency at the edge of the field, you should just take in account only cells in the field.
#
# ArraysFundamentals
# Solution
from preloaded import FIELD

def is_efficient(x, y, threshold):
    total = 0.0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < 20 and 0 <= j < 20: total += FIELD[i][j]
    return total >= threshold