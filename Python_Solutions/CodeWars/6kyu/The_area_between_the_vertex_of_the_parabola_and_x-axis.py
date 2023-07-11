# The area between the vertex of the parabola and x-axis
# 1-) Warning
# If you don't know about the following topics, you will have problems in this kata.
#
# Quadratic equations
# Parabola
# Integral
# 2-) Explanation
# I will give you 3 values as input in the kata. These are a , b , c. The value of a will never be given as 0. These values are the coefficients of the following equation.
#
# �
# (
# �
# )
# =
# �
# �
# 2
# +
# �
# �
# +
# �
# f(x)=ax
# 2
#  +bx+c
# The graph of this equation is a parabola.
#
# This kata asks you for the area between the vertex of the parabola and x-axis.
#
# Don't forget area isn't negative.
#
# 3-) Details
# If the equation hasn't real roots, you should return 0. Because there isn't any area.
#
# If the equation has 2 equal real roots, you should return 0. Because 0 is the real area.
#
# If the equation has 2 unequal real root, you should return the real area.
#
# For example
#
# The real area: 35.265720  --->  return 35.265720
# Given values is definitely between -4000 with 4000. Because the result should be under the DOUBLE_MAX value.
#
# I set up the tolerance to 10-6 for the decimal errors.
#
# Letter for you
# If you like this kata, don't forget to vote please. Take easy...
#
# -founded by theprotagonist
# MATHEMATICS