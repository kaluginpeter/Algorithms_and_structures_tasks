# In computer science, cycle detection is the algorithmic problem of finding a cycle in a sequence of iterated function values.
#
# For any function
# f
# f, and any initial value
# x
# 0
# x
# 0
# ​
#   in S, the sequence of iterated function values
#
# x
# 0
# ,
# x
# 1
# =
# f
# (
# x
# 0
# )
# ,
# …
# ,
# x
# i
# =
# f
# (
# x
# i
# −
# 1
# )
# ,
# …
# x
# 0
# ​
#  ,x
# 1
# ​
#  =f(x
# 0
# ​
#  ),…,x
# i
# ​
#  =f(x
# i−1
# ​
#  ),…
# may eventually use the same value twice under some assumptions: S finite, f periodic ... etc. So there will be some
# i
# ≠
# j
# i
# 
# =j such that
# x
# i
# =
# x
# j
# x
# i
# ​
#  =x
# j
# ​
#  . Once this happens, the sequence must continue by repeating the cycle of values from
# x
# i
# x
# i
# ​
#   to
# x
# j
# −
# 1
# x
# j−1
# ​
#  . Cycle detection is the problem of finding
# i
# i and
# j
# j, given
# ƒ
# ƒ and
# x
# 0
# x
# 0
# ​
#  . Let
# μ
# μ be the smallest index such that the value associated will reappears and
# λ
# λ the smallest value such that
# x
# μ
# =
# x
# λ
# +
# μ
# x
# μ
# ​
#  =x
# λ+μ
# ​
#  ,
# λ
# λ is the loop length.
#
# Example:
#
# Consider the sequence:
#
# 2, 0, 6, 3, 1, 6, 3, 1, 6, 3, 1, ....
# The cycle in this value sequence is 6, 3, 1.
# μ
# μ is 2 (first 6)
# λ
# λ is 3 (length of the sequence or difference between position of consecutive 6).
#
# The goal of this kata is to build a function that will return [
# μ
# μ,
# λ
# λ] when given a short sequence. Simple loops will be sufficient. The sequence will be given in the form of an array. All array will be valid sequence associated with deterministic function. It means that the sequence will repeat itself when a value is reached a second time. (So you treat two cases: non repeating [1,2,3,4] and repeating [1,2,1,2], no hybrid cases like [1,2,1,4]). If there is no repetition you should return [].
#
# This kata is followed by Cycle Detection: Floyd's The Tortoise and the The Hare
#
# MathematicsAlgorithms