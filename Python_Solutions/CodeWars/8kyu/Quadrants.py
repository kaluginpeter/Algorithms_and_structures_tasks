# Given a point in a Euclidean plane (x and y), return the quadrant the point exists in: 1, 2, 3 or 4 (integer). x and y are non-zero integers, therefore the given point never lies on the axes.
#
# Examples
# (1, 2)     => 1
# (3, 5)     => 1
# (-10, 100) => 2
# (-1, -9)   => 3
# (19, -56)  => 4
#
# There are four quadrants:
#
# First quadrant, the quadrant in the top-right, contains all points with positive X and Y
# Second quadrant, the quadrant in the top-left, contains all points with negative X, but positive Y
# Third quadrant, the quadrant in the bottom-left, contains all points with negative X and Y
# Fourth quadrant, the quadrant in the bottom-right, contains all points with positive X, but negative Y
# More on quadrants: Quadrant (plane geometry) - Wikipedia
#
# Task Series
# Quadrants (this kata)
# Quadrants 2: Segments
# Solution
def quadrant(x, y):
    return 1 if x > 0 and y > 0 else 2 if x < 0 and y > 0 else 3 if x < 0 and y < 0 else 4