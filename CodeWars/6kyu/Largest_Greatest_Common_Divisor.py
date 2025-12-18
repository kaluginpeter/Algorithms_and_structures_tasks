# You are given positive integers,
# a
# a and
# b
# b
# (
# a
# <
# b
# )
# (a<b).
#
# Find a positive integer
# k
# k such that
# gcd
# (
# a
# +
# k
# ,
# b
# +
# k
# )
# gcd(a+k,b+k) is maximized.
#
# If there are multiple values of
# k
# k that satisfy the condition above, return the smallest one.
#
# Here
# gcd
# (
# x
# ,
# y
# )
# gcd(x,y) means the greatest common divisor of
# x
# x and
# y
# y.
#
# C
# o
# n
# s
# t
# r
# a
# i
# n
# t
# s
# Constraints
#
# 1
# ≤
# a
# <
# b
# ≤
# 1
# 0
# 18
# 1≤a<b≤10
# 18
#
# Algebra
# Solution
long long get_k(long long a, long long b) {
    long long d = b - a;
    long long k = (d - a % d) % d;
    return k == 0 ? d : k;
}