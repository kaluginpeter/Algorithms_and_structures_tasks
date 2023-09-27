# Task:
# You have to write a function pattern which creates the following pattern upto n number of rows. If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
#
# Examples:
# pattern(4):
#
# 1234
# 234
# 34
# 4
# pattern(6):
#
# 123456
# 23456
# 3456
# 456
# 56
# 6
# Note: There are no blank spaces
#
# Hint: Use \n in string to jump to next line
#
# ASCII ARTFUNDAMENTALS
# Solution
def pattern(n):
    l = list(range(1, n + 1))
    return '\n'.join(''.join(map(str, l[i:])) for i in range(n))