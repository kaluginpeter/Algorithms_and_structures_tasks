# Euler's Method
# We want to calculate the shape of an unknown curve which starts at a given point with a given slope. This curve satisfies an ordinary differential equation (ODE):
#
# d
# y
# d
# x
# =
# f
# (
# x
# ,
# y
# )
# ;
# y
# (
# x
# 0
# )
# =
# y
# 0
# dx
# dy
# ​
#  =f(x,y);
# y(x
# 0
# ​
#  )=y
# 0
# ​
#
# The starting point
# A
# 0
# (
# x
# 0
# ,
# y
# 0
# )
# A
# 0
# ​
#  (x
# 0
# ​
#  ,y
# 0
# ​
#  ) is known as well as the slope to the curve at
# A
# 0
# A
# 0
# ​
#   and then the tangent line at
# A
# 0
# A
# 0
# ​
#   .
#
# Take a small step along that tangent line up to a point
# A
# 1
# A
# 1
# ​
#  . Along this small step, the slope does not change too much, so
# A
# 1
# A
# 1
# ​
#   will be close to the curve. If we suppose that
# A
# 1
# A
# 1
# ​
#   is close enough to the curve, the same reasoning as for the point
# A
# 1
# A
# 1
# ​
#   above can be used for other points. After several steps, a polygonal curve
# A
# 0
# ,
# A
# 1
# ,
# .
# .
# .
# ,
# A
# n
# A
# 0
# ​
#  ,A
# 1
# ​
#  ,...,A
# n
# ​
#   is computed. The error between the two curves will be small if the step is small.
#
# We define points
# A
# 0
# ,
# A
# 1
# ,
# A
# 2
# ,
# .
# .
# .
# ,
# A
# n
# A
# 0
# ​
#  ,A
# 1
# ​
#  ,A
# 2
# ​
#  ,...,A
# n
# ​
#   whose x-coordinates are
# x
# 0
# ,
# x
# 1
# ,
# .
# .
# .
# ,
# x
# n
# x
# 0
# ​
#  ,x
# 1
# ​
#  ,...,x
# n
# ​
#   and y-coordinates are such that
# y
# k
# +
# 1
# =
# y
# k
# +
# f
# (
# x
# k
# ,
# y
# k
# )
# ×
# h
# y
# k+1
# ​
#  =y
# k
# ​
#  +f(x
# k
# ​
#  ,y
# k
# ​
#  )×h where
# h
# h is the common step. If
# T
# T is the length
# x
# n
# −
# x
# 0
# x
# n
# ​
#  −x
# 0
# ​
#   we have
# h
# =
# T
# /
# n
# h=T/n.
#
# Task
# For this kata we will focus on the following differential equation:
#
# d
# y
# d
# x
# =
# 2
# −
# e
# −
# 4
# x
# −
# 2
# y
# ;
# A
# 0
# =
# (
# 0
# ,
# 1
# )
# dx
# dy
# ​
#  =2−e
# −4x
#  −2y;
# A
# 0
# ​
#  =(0,1)
# with
# x
# ∈
# [
# 0
# ,
# 1
# ]
# x∈[0,1]. We will then take a uniform partition of the region of
# x
# x between
# 0
# 0 and
# 1
# 1 and split it into
# n
# n sections (hence
# n
# +
# 1
# n+1 points).
# n
# n will be the input to the function ex_euler(n) and since
# T
# T is always 1,
# h
# =
# 1
# /
# n
# h=1/n.
#
# We know that an exact solution is
#
# z
# =
# 1
# +
# 0.5
# e
# −
# 4
# x
# −
# 0.5
# e
# −
# 2
# x
# .
# z=1+0.5e
# −4x
#  −0.5e
# −2x
#  .
# For each
# x
# k
# x
# k
# ​
#   we are able to calculate the
# y
# k
# y
# k
# ​
#   as well as the values
# z
# k
# z
# k
# ​
#   of the exact solution.
#
# Our task is, for a given number
# n
# n of steps, to return the mean (truncated to 6 decimal places) of the relative errors between the
# y
# k
# y
# k
# ​
#   (our aproximation) and the
# z
# k
# z
# k
# ​
#   (the exact solution). For that we can use:
#
# error in
# A
# k
# =
# a
# b
# s
# (
# y
# k
# −
# z
# k
# )
# /
# z
# k
# A
# k
# ​
#  =abs(y
# k
# ​
#  −z
# k
# ​
#  )/z
# k
# ​
#   and then the mean is sum(errors in
# A
# k
# A
# k
# ​
#  )/ (
# n
# n + 1)
#
# Examples
# ex_euler(10) should return: 0.026314 (truncated from 0.026314433214799246)
# with
# Y = [1.0,0.9..., 0.85..., 0.83..., 0.83..., 0.85..., 0.86..., 0.88..., 0.90..., 0.91..., 0.93...]
# Z = [1.0, 0.9..., 0.88..., 0.87..., 0.87..., 0.88..., 0.89..., 0.90..., 0.91..., 0.93..., 0.94...]
# Relative errors = [0.0, 0.02..., 0.04..., 0.04..., 0.04..., 0.03..., 0.03..., 0.02..., 0.01..., 0.01..., 0.01...]
# ex_euler(17) should return: 0.015193 (truncated from 0.015193336263370796). As expected, as
# n
# n increases, our error reduces.
#
# Links and graphs
# Wiki article
#
# alternative text
#
# Below comparison between approximation (red curve) and exact solution(blue curve) for n=100:alternative text
#
# Thanks to @rge123 for a better description
# Algorithms
# Solution
import math

def ex_euler(n):
    h = 1.0 / n
    y = 1.0
    total_error = 0.0
    for k in range(n + 1):
        x = k * h
        z = 1 + 0.5 * math.exp(-4 * x) - 0.5 * math.exp(-2 * x)
        total_error += abs(y - z) / z
        if k < n: y = y + h * (2 - math.exp(-4 * x) - 2 * y)
    mean_error = total_error / (n + 1)
    return math.floor(mean_error * 1_000_000) / 1_000_000