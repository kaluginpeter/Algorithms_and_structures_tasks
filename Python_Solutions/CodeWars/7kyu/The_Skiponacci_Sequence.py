# Your task is to generate the Fibonacci sequence to n places, with each alternating value as "skip". For example:
#
# "1 skip 2 skip 5 skip 13 skip 34"
#
# Return the result as a string
#
# You can presume that n is always a positive integer between (and including) 1 and 64.
#
# PUZZLESALGORITHMS
# Solution
def skiponacci(n):
    l = []
    a, b = 0, 1
    for i in range(n):
        a, b = a + b, a
        l.append('skip' if i % 2 else str(a))
    return ' '.join(l)