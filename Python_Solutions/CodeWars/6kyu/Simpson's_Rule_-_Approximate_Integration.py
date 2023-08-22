# An integral:
#
# ∫
# �
# �
# �
# (
# �
# )
# �
# �
# ∫
# a
# b
# ​
#  f(x)dx
# can be approximated by the so-called Simpson’s rule:
#
# �
# −
# �
# 3
# �
# (
# �
# (
# �
# )
# +
# �
# (
# �
# )
# +
# 4
# ∑
# �
# =
# 1
# �
# /
# 2
# �
# (
# �
# +
# (
# 2
# �
# −
# 1
# )
# ℎ
# )
# +
# 2
# ∑
# �
# =
# 1
# �
# /
# 2
# −
# 1
# �
# (
# �
# +
# 2
# �
# ℎ
# )
# )
# 3n
# b−a
# ​
#  (f(a)+f(b)+4∑
# i=1
# n/2
# ​
#  f(a+(2i−1)h)+2∑
# i=1
# n/2−1
# ​
#  f(a+2ih))
# Here h = (b - a) / n, n being an even integer and a <= b.
#
# We want to try Simpson's rule with the function f:
#
# �
# (
# �
# )
# =
# 3
# 2
# sin
# ⁡
# (
# �
# )
# 3
# f(x)=
# 2
# 3
# ​
#  sin(x)
# 3
#
# The task is to write a function called simpson with parameter n which returns the value of the integral of f on the interval [0, pi] (pi being 3.14159265359...).
#
# Notes:
# Don't round or truncate your results. See in "RUN EXAMPLES" the function assertFuzzyEquals or testing.
# n will always be even.
# We know that the exact value of the integral of f on the given interval is 2.
# Please ask before translating.
# Complement: you can see: https://www.codewars.com/kata/5562ab5d6dca8009f7000050/ about rectangle method and trapezoidal rule.
#
# MATHEMATICS
# Solution
from math import pi, sin
def simpson(n, f=lambda x: 3 / 2 * sin(x) ** 3, a=0, b=pi):
    h = (b - a) / n
    return h / 3 * (f(a) + f(b)+ 4 * sum(f(a + i * h) for i in range(1, n, 2))+ 2 * sum(f(a + i * h) for i in range(2, n, 2)))