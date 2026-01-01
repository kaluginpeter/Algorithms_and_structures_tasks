# Find the minimum value
#
# Given an input of a certain equality of the form
# ∑
# i
# =
# 1
# k
# λ
# i
# z
# i
# =
# n
# ∑
# i=1
# k
# ​
#  λ
# i
# ​
#  z
# i
# ​
#  =n, with
# λ
# i
# λ
# i
# ​
#   being the coefficients,
# z
# i
# z
# i
# ​
#   being the variables and
# k
# k being the number of terms. For example:
#
# 3
# x
# +
# 4
# y
# =
# 5
# 3x+4y=5
#
# Your task is to return the minimum value of
# ∑
# i
# =
# 1
# k
# (
# z
# i
# )
# 2
# ∑
# i=1
# k
# ​
#  (z
# i
# ​
#  )
# 2
#
#
# For the example above, the answer would be 1. Cause if:
#
# x
# =
# 3
# 5
# ,
# y
# =
# 4
# 5
# ⇒
# x
# 2
# +
# y
# 2
# =
# 1
# x=
# 5
# 3
# ​
#  ,y=
# 5
# 4
# ​
#  ⇒x
# 2
#  +y
# 2
#  =1
#
# There are no lower values than that.
#
# Input
# A string, which represents the equality.
#
# Output
# An integer, representing the minimum value of the expression, given above.
#
#
# A few notes:
#
# Note that, the number of variables can go up to 26, just because I do not feel like including Greek letters and/or uppercase Latin letters.
# Every coefficient will be an integer ranging from [-100000, 100000], excluding 0.
# Every equation will have at least 2 variables.
# There will be 300 random tests.
# Most of the outputs will not be integers. Do not round your answers. The tests will approximate your output to 1e-6 and then test it.
# In case you're interested in math katas, you might want to check this collection.
#
# Good luck!
#
# MathematicsAlgebraParsing
# Solution
import re
def minimum_value(equality):
    left, right = equality.split("=")
    n = int(right)
    terms = re.findall(r'([+-]?\d*)([a-z])', left)
    lambdas = []
    for coef, _ in terms:
        if coef in ("", "+"): lambdas.append(1)
        elif coef == "-": lambdas.append(-1)
        else: lambdas.append(int(coef))
    return n * n / sum(c * c for c in lambdas)