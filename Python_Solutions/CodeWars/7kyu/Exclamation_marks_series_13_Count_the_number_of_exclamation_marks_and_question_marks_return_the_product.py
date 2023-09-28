# Description:
# Count the number of exclamation marks and question marks, return the product.
#
# Examples
# ""          --->   0
# "!"         --->   0
# "!ab? ?"    --->   2
# "!!"        --->   0
# "!??"       --->   2
# "!???"      --->   3
# "!!!??"     --->   6
# "!!!???"    --->   9
# "!???!!"    --->   9
# "!????!!!?" --->  20
# FUNDAMENTALS
# Solution
def product(s):
    return int(s.count('!'))*int(s.count('?'))