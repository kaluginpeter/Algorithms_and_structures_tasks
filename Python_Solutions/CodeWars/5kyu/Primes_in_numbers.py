# Given a positive number n > 1 find the prime factor decomposition of n.
# The result will be a string with the following form :
#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
# Solution
def prime_factors(n):
    i = 2
    res = {}
    while n/i != 1:
        if n%i == 0:
            if i in res:
                res[i] = res[i]+1
            else:
                res[i] = 1
            n = n/i
        else:
            i+=1
    if i in res:
        res[i] = res[i]+1
    else:
        res[i] = 1
    t = ''
    res = sorted(res.items(),key = lambda a:a[0])
    for key in res:
        if key[1] == 1:
            t = t + '('+str(key[0]) +')'
        else:
            t = t + '(' +str(key[0]) + '**' + str(key[1]) + ')'
    return t