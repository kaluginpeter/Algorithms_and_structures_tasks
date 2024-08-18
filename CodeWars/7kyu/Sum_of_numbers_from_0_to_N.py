# Description:
#
# We want to generate a function that computes the series starting from 0 and ending until the given number.
#
# Example:
# Input:
#
# > 6
# Output:
#
# 0+1+2+3+4+5+6 = 21
#
# Input:
#
# > -15
# Output:
#
# -15<0
#
# Input:
#
# > 0
# Output:
#
# 0=0
#
# FUNDAMENTALS
# Solution
def show_sequence(n):
    sum=0
    s=''
    if n==0:
        return "0=0"
    elif n<0:
        return str(n)+"<0"
    else:
        for i in range(0,n+1):
            sum += i
            s+=str(i)+'+'
        s = s.strip('+')
        s = s +" = "+str(sum)
        return s