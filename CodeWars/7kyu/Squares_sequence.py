# Complete the function that returns an array of length n, starting with the given number x and the squares of the previous number. If n is negative or zero, return an empty array/list.
#
# Examples
# 2, 5  -->  [2, 4, 16, 256, 65536]
# 3, 3  -->  [3, 9, 81]
# MATHEMATICSFUNDAMENTALS
# Solution
def squares(x, n):
    if (n<1): return []
    result = [x]
    i=0
    while i < n-1:
        i+=1
        x*=x
        result.append(x)
    return result