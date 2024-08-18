# Write function heron which calculates the area of a triangle with sides a, b, and c (x, y, z in COBOL).
#
# Heron's formula:
#
# �
# ∗
# (
# �
# −
# �
# )
# ∗
# (
# �
# −
# �
# )
# ∗
# (
# �
# −
# �
# )
# s∗(s−a)∗(s−b)∗(s−c)
# ​
#
# where
#
# �
# =
# �
# +
# �
# +
# �
# 2
# s=
# 2
# a+b+c
# ​
#
# Output should have 2 digits precision.
#
# FUNDAMENTALS
# Solution
def heron(a, b, c):
    i=(a+b+c)/2
    return round((i*(i-a)*(i-b)*(i-c))**.5, 2)