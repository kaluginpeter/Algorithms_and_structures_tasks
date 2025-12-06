# This series of katas will introduce you to basics of doing geometry with computers.
#
# Vector objects (struct in C) have x, y, and z attributes. x, y and z are floating-point numbers.
#
# Write a function calculating the cross product of Vector a and Vector b, the result should be a Vector object.
#
# You can read more about cross product on Wikipedia.
#
# GeometryFundamentals
# Solution
from preloaded import Vector

def cross_product(a: Vector, b: Vector) -> Vector:
    x: int = a.y * b.z - a.z * b.y
    y: int = a.z * b.x - a.x * b.z
    z: int = a.x * b.y - a.y * b.x
    return Vector(x, y, z)