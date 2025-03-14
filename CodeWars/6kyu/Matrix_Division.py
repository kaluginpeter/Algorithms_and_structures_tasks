# When multiplying matrices, the
# e
# l
# e
# m
# e
# n
# t
# i
# j
# element
# ij
# ​
#   of the product matrix C is equal to the sum of pairwise products of the elements of
# r
# o
# w
# i
# row
# i
# ​
#   of the left matrix A and elements of
# c
# o
# l
# u
# m
# n
# j
# column
# j
# ​
#   of the right matrix B. For this kata, we will redefine matrix multiplication by removing the step with summation so that division of matrices can be unambiguously defined:
#
# c
# i
# j
# =
# (
# a
# i
# 0
# ∗
# b
# 0
# j
# ,
# a
# i
# 1
# ∗
# b
# 1
# j
# ,
# .
# .
# .
# ,
# a
# i
# k
# ∗
# b
# k
# j
# )
# c
# ij
# ​
#  =(a
# i0
# ​
#  ∗b
# 0j
# ​
#  ,a
# i1
# ​
#  ∗b
# 1j
# ​
#  ,...,a
# ik
# ​
#  ∗b
# kj
# ​
#  )
# Task:
#
# Implement a function matrix_div with 3 parameters:
#
# result represents the product matrix C
#
# factor represents one of the two factors (either A or B).
#
# position is either 0 or 1: 0 means that factor is the right factor while 1 means it's the left one.
#
# Func should return the other factor.
#
# Examples:
#
# matrix_div([[[1,10],[4,4]],[[3,5],[12,2]]], [[1,4],[5,2]], 0)  should return [[1,2], [3,1]].
#
# matrix_div([[[1,10],[4,4]],[[3,5],[12,2]]], [[1,4],[5,2]], 1)  should return [[1,4], [2,1]].
#
# Note:
#
# 1<=k<=30. All matrix elements lie between 1 and 100 inclusive. Division of elements is integer division.
#
# MatrixArrays