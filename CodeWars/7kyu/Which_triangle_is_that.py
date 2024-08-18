# Build a function that will take the length of each side of a triangle and return if it's either an Equilateral, an Isosceles, a Scalene or an invalid triangle.
#
# It has to return a string with the type of triangle.
# For example:
#
# type_of_triangle(2, 2, 1) --> "Isosceles"
# GEOMETRYALGORITHMS
# Solution
def type_of_triangle(a, b, c):
    if any(not isinstance(i, int) for i in (a, b, c)): return "Not a valid triangle"
    a, b, c = sorted((a, b, c))
    if a + b <= c: return "Not a valid triangle"
    if a == b and b == c: return "Equilateral"
    if a == b or a == c or b == c: return "Isosceles"
    return "Scalene"