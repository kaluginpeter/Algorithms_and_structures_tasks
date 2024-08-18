# Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:
#
# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
# c = Vector([5, 6, 7, 8])
#
# a.add(b)      # should return a new Vector([4, 6, 8])
# a.subtract(b) # should return a new Vector([-2, -2, -2])
# a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
# a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# a.add(c)      # raises an exception
# If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!
#
# Also provide:
#
# a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
# an equals method, to check that two vectors that have the same components are equal
# Note: the test cases will utilize the user-provided equals method.
#
# OBJECT-ORIENTED PROGRAMMINGALGORITHMSLINEAR ALGEBRA
# Solution
class Vector:
    def __init__(self, arr: list):
        self.vector = arr
    def add(self, new_vector):
        if len(new_vector.vector) != len(self.vector):
            raise Error
        return Vector([x + y for x, y in zip(self.vector, new_vector.vector)])
    def equals(self, new_vector):
        return all(i == j for i,j in zip(self.vector, new_vector.vector))
    def subtract(self, new_vector):
        return Vector([x - y for x, y in zip(self.vector, new_vector.vector)])
    def dot(self, new_vector):
        return sum(x * y for x, y in zip(self.vector, new_vector.vector))
    def norm(self):
        return sum(i**2 for i in self.vector) ** .5
    def __str__(self):
        return f"({','.join(str(i) for i in self.vector)})"