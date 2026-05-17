# Write a function to calculate the centroid of 3D coordinates.
#
# Return the results as a list of 3 floats.
#
# Algorithms
# Solution
def centroid(points: list[list[float]]) -> list[float]:
    n = len(points)
    x = sum(p[0] for p in points) / n
    y = sum(p[1] for p in points) / n
    z = sum(p[2] for p in points) / n
    return [x, y, z]