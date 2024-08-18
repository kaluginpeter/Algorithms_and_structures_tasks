# Imagine there's a big cube consisting of
# �
# 3
# n
# 3
#   small cubes. Calculate, how many small cubes are not visible from outside.
#
# For example, if we have a cube which has 4 cubes in a row, then the function should return 8, because there are 8 cubes inside our cube (2 cubes in each dimension)
#
# For a visual representation: --> https://imgur.com/a/AN8A5DJ
#
# PUZZLES
# Solution
def not_visible_cubes(n):
    if n - 2 <= 0:
        return 0
    return (n - 2) ** 3