# In this kata, you should calculate the type of triangle with three given sides a, b and c (given in any order).
#
# If each angle is less than 90°, this triangle is acute and the function should return 1.
#
# If one angle is strictly 90°, this triangle is right and the function should return 2.
#
# If one angle is more than 90°, this triangle is obtuse and the function should return 3.
#
# If three sides cannot form a triangle, or one angle is 180° (which turns the triangle into a segment) - the function should return 0.
#
# Three input parameters are sides of given triangle. All input values are non-negative floating point or integer numbers (or both, depending on the language).
#
#
# Acute
#
# Right
#
# Obtuse
# Examples:
# (2, 4, 6) ---> return 0 (Not triangle)
# (8, 5, 7) ---> return 1 (Acute, angles are approx. 82°, 38° and 60°)
# (3, 4, 5) ---> return 2 (Right, angles are approx. 37°, 53° and exactly 90°)
# (7, 12, 8) ---> return 3 (Obtuse, angles are approx. 34°, 106° and 40°)
# If you stuck, this can help you: http://en.wikipedia.org/wiki/Law_of_cosines. But you can solve this kata even without angle calculation.
#
# There is a very small chance of random test to fail due to round-off error, in such case resubmit your solution.
#
# GEOMETRYMATHEMATICSALGORITHMS
# Solution
import math
def triangle_type(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b: return 0
    angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_c = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
    l = [angle_a, angle_b, angle_c]
    if all(i < 90 for i in l): return 1
    if any(i == 90 for i in l): return 2
    if any(i > 90 for i in l): return 3