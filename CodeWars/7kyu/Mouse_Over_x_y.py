# You are tasked with implementing a MouseOver(x, y) functionality.
#
# This is an easier version of this kata.
#
# Given a list of rectangles displayed on a screen, your program must process a series of queries to determine which rectangle, if any, contains a given point.
#
# In the graphic below, you can see examples of a point inside a rectangle, one on the border, one inside two overlapping rectangles, and one outside any rectangle.
#
# Implement a class that takes a list of rectangles during initialization and provides a method to process query points (x, y). Each query should be processed independently, and there may be many such queries.
#
# Input
# Constructor input:
# A list of rectangles, where each is defined by (x, y, width, height). This represents a rectangle that extends from x to x + width along the x-axis and from y to y + height along the y-axis.
# Query input:
# A single point represented as a tuple (x, y).
# Output:
# For each query point, return the rectangle that contains it, or indicate that no such rectangle exists.
#
# Rules:
# All coordinates and dimensions are integers.
# Rectangles may overlap
# A point that lies on the border of a rectangle is considered to be inside the rectangle
# If a point is contained in multiple rectangles, return the first rectangle from the input list that contains it.
# Example:
# The following example corresponds to the graphic above.
#
# List of rectangles:
#
# [(9, 8, 9, 3),  (6, 4, 15, 3),  (9, 16, 9, 3),  (6, 20, 15, 3),  (5, 9, 3, 9),  (1, 6, 3, 15),  (19, 9, 3, 9),  (23, 6, 3, 15), (15, 15, 10, 10)]
# Query points:
#
# (3, 18)   ->  (1, 6, 3, 15)       # Inside a rectangle
# (6, 15)   ->  (5, 9, 3, 9)        # Inside a rectangle
# (10, 11)  ->  (9, 8, 9, 3)        # On the border
# (15, 13)  ->  None                # Outside all rectangles
# (18, 21)  ->  (6, 20, 15, 3)      # Inside multiple, return first
# Input size:
# there will be roughly 15 tests
# There will be no more than 400 rectangles in each test.
# There will be 100 queries to process for each test