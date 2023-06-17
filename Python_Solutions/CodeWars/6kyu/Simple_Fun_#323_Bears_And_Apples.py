# Task
# There are n bears in the orchard and they picked a lot of apples.
#
# They distribute apples like this:
#
# The first bear divided the apple into n piles, each with the same number. leaving an apple at last, and the apple was thrown away. Then he took 1 pile and left the n-1 pile.
#
# The second bear divided the apple into n piles, each with the same number. leaving an apple at last, and the apple was thrown away. Then he took 1 pile and left the n-1 pile.
#
# and so on..
# Hmm.. your task is coming, please calculate the minimum possible number of these apples (before they start distributing)
#
# Input/Output
# [input] integer n
#
# The number of bears.
#
# 2 <= n <= 9 (JS, Crystal and C) 2 <= n <= 50 (Ruby and Python)
#
# [output] an integer
#
# The minimum possible number of apples.
#
# Example
# For n = 5, the output should be 3121.
#
# 5 bears distribute apples:
#
# 1st bear divided the apples into 5 piles, each pile has 624 apples, and 1 apple was thrown away.
# 3121 - 1 = 624 x 5
# 1st bear took 1 pile of apples, 2496 apples left.
# 3121 - 1 - 624 = 2496
#
# 2nd bear divided the apples into 5 piles, each pile has 499 apples, and 1 apple was thrown away.
# 2496 - 1 = 499 x 5
# 2nd bear took 1 pile of apples, 1996 apples left.
# 2496 - 1 - 499 = 1996
#
# 3rd bear divided the apples into 5 piles, each pile has 399 apples, and 1 apple was thrown away.
# 1996 - 1 = 399 x 5
# 3rd bear took 1 pile of apples, 1596 apples left.
# 1996 - 1 - 399 = 1596
#
# 4th bear divided the apples into 5 piles, each pile has 319 apples, and 1 apple was thrown away.
# 1596 - 1 = 319 x 5
# 4th bear took 1 pile of apples, 1276 apples left.
# 1596 - 1 - 319 = 1276
#
# 5th bear divided the apples into 5 piles, each pile has 255 apples, and 1 apple was thrown away.
# 1276 - 1 = 255 x 5
# 5th bear took 1 pile of apples, 1020 apples left.
# 1276 - 1 - 255 = 1020
# PUZZLES