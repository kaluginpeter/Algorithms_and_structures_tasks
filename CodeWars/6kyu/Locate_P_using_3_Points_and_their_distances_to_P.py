# Task
# Given Points A, B, C ∈ ℤ2 and dA, dB, dC ∈ ℕ their respective squared euclidian distances to a certain point P ∈ ℤ2, return the value of P.
#
# Note
# A, B, and C will always be distinct and non-collinear
#
# MathematicsGeometry
# Solution
def triangulate(A, dA, B, dB, C, dC):
    xA, yA = A
    xB, yB = B
    xC, yC = C
    a1 = 2 * (xB - xA)
    b1 = 2 * (yB - yA)
    c1 = dA - dB + xB**2 - xA**2 + yB**2 - yA**2
    a2 = 2 * (xC - xA)
    b2 = 2 * (yC - yA)
    c2 = dA - dC + xC**2 - xA**2 + yC**2 - yA**2
    det = a1 * b2 - a2 * b1
    x = (c1 * b2 - c2 * b1) // det
    y = (a1 * c2 - a2 * c1) // det
    return (x, y)