# Task:
# You have to write a function pattern which creates the following pattern up to n/2 number of lines.
#
# If n <= 1 then it should return "" (i.e. empty string).
# If any odd number is passed as argument then the pattern should last up to the largest even number which is smaller than the passed odd number.
# Examples:
# pattern(8):
#
# 22
# 4444
# 666666
# 88888888
# pattern(5):
#
# 22
# 4444
# Note: There are no spaces in the pattern
#
# Hint: Use \n in string to jump to next line
#
# ASCII ARTFUNDAMENTALS
# Solution
def pattern(n):
    if n <= 1:
        return ''
    top, x = [], 2
    while n % 2 != 0:
        n -= 1
    for i in range(2, n + 1, 2):
        top.append(str(i) * x)
        x += 2
    return '\n'.join(top)