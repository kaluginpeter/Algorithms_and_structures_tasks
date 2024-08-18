# For this kata you will have to forget how to add two numbers.
#
# It can be best explained using the following meme:
#
# Dayane Rivas adding up a sum while competing in the Guatemalan television show "Combate" in May 2016
#
# In simple terms, our method does not like the principle of carrying over numbers and just writes down every number it calculates :-)
#
# You may assume both integers are positive integers.
#
# Examples
# 1
# 6
# +
# 1
# 8
# 2
# 14
# 2
# 6
# +
# 3
# 9
# 5
# 15
# +
# ​
#
# 1
# 1
# 2
# ​
#
# 6
# 8
# 14
# ​
#
# ​
#
# +
# ​
#
# 2
# 3
# 5
# ​
#
# 6
# 9
# 15
# ​
#
# ​
#
#
#
# 1
# 2
# 2
# +
# 8
# 1
# 1
# 10
# 3
# 7
# 2
# +
# 9
# 7
# 11
# +
# ​
#
# 1
# 1
# ​
#
# 2
# 8
# 10
# ​
#
# 2
# 1
# 3
# ​
#
# ​
#
# +
# ​
#
# 7
# 7
# ​
#
# 2
# 9
# 11
# ​
#
# ​
#
# ALGORITHMSMATHEMATICS
# Solution
def add(a ,b):
    return int(str(add(a // 10, b // 10)) + str(a % 10 + b % 10)) if bool(a*b) else a+b