# Multiplicative closure of a set is the set of numbers that can be formed via a product of a finite sequence of numbers from the set.
#
# For example, this is closure({2, 3}):
#
# Value	Product of
# 1	[]
# 2	[2]
# 3	[3]
# 4	[2, 2]
# 6	[2, 3]
# 8	[2, 2, 2]
# 9	[3, 3]
# 12	[2, 2, 3]
# ...
# Two different sets may have identical closures. Example:
#
# Value	Product of
# Using {2, 3}	Using {2, 3, 6}
# 1	[]	[]
# 2	[2]	[2]
# 3	[3]	[3]
# 4	[2, 2]	[2, 2]
# 6	[2, 3]	[6] or [2, 3]
# 8	[2, 2, 2]	[2, 2, 2]
# 9	[3, 3]	[3, 3]
# 12	[2, 2, 3]	[2, 6] or [2, 2, 3]
# ...
# Objective
# Given a set, find the smallest set that has the same multiplicative closure.
#
# Next step
# After completing this kata consider trying this one.
#
# Number Theory