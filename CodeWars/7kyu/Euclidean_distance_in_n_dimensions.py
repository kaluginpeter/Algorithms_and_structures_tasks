# Implement a function to calculate the distance between two points in n-dimensional space. The two points will be passed to your function as arrays of the same length (tuples in Python).
#
# Round your answers to two decimal places.
#
# MATHEMATICSALGORITHMSFUNDAMENTALS
# Solution
def euclidean_distance(point1, point2):
    return round(sum((j - i)**2 for i, j in zip(point1, point2)) ** 0.5, 2)