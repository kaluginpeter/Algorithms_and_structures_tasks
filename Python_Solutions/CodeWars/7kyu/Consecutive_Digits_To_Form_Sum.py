# Positive integers have so many gorgeous features. Some of them could be expressed as a sum of two or more consecutive positive numbers.
#
# Consider an Example :
# 10 could be expressed as the sum of 1 + 2 + 3 + 4 .
# Task
# Given Positive integer, N , return true if it could be expressed as a sum of two or more consecutive positive numbers , otherwise return false .
#
# Notes
# Guaranteed constraint : 2 ≤ N ≤ (2^32) -1 .
# Input >> Output Examples:
#
# * consecutiveDucks(9)  ==>  return (true)  //  9 , could be expressed as a sum of ( 2 + 3 + 4 ) or ( 4 + 5 ) .
#
# * consecutiveDucks(64)  ==>  return (false)
#
# * consecutiveDucks(42)  ==>  return (true) //  42 , could be expressed as a sum of ( 9 + 10 + 11 + 12 )  .
# Playing with Numbers Series
# Playing With Lists/Arrays Series
# Bizarre Sorting-katas
# For More Enjoyable Katas
# ALL translations are welcomed
# Enjoy Learning !!
# Zizou
# FUNDAMENTALSMATHEMATICSPUZZLES
# Solution
import math
def consecutive_ducks(n):
    return not math.log2(n).is_integer()