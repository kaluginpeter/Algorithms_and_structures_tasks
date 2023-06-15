# Build Tower Advanced
# Build Tower by the following given arguments:
#
# number of floors (integer and always greater than 0)
# block size (width, height) (integer pair and always greater than (0, 0))
# Tower block unit is represented as *. Tower blocks of block size (2, 1) and (2, 3) would look like respectively:
#
#   **
#   **
#   **
#   **
# for example, a tower of 3 floors with block size = (2, 3) looks like below
#
# [
#   '    **    ',
#   '    **    ',
#   '    **    ',
#   '  ******  ',
#   '  ******  ',
#   '  ******  ',
#   '**********',
#   '**********',
#   '**********'
# ]
# and a tower of 6 floors with block size = (2, 1) looks like below
#
# [
#   '          **          ',
#   '        ******        ',
#   '      **********      ',
#   '    **************    ',
#   '  ******************  ',
#   '**********************'
# ]
# Don't return a whole string containing line-endings but a list/array/vector of strings instead!
#
# This kata might looks like a 5.5kyu one. So challenge yourself!
#
# Go take a look at Build Tower which is a more basic version :)
#
# STRINGSASCII ARTFUNDAMENTALS
# Solution
def tower_builder(n_floors, block_size):
    w, h = block_size
    l = []
    n = n_floors
    for i in range(n_floors):
        n -= 1
        for j in range(h): l.append(' '*n * w + '*' * (i * 2 + 1) * w + ' ' * n* w)
    return l