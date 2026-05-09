# Binomial Expansion
# (
# a
# +
# b
# )
# n
# =
# a
# n
# +
# (
# n
# 1
# )
# a
# n
# −
# 1
# b
# 1
# +
# (
# n
# 2
# )
# a
# n
# −
# 2
# b
# 2
# +
# …
# +
# (
# n
# n
# −
# 1
# )
# a
# 1
# b
# n
# −
# 1
# +
# b
# n
# (a+b)
# n
#  =a
# n
#  +(
# n
# 1
# ​
#  )a
# n−1
#  b
# 1
#  +(
# n
# 2
# ​
#  )a
# n−2
#  b
# 2
#  +…+(
# n
# n−1
# ​
#  )a
# 1
#  b
# n−1
#  +b
# n
#
#
# Task
# Given a string, indicating an expression, with 2 terms, raised to a positive integer's power and an integer, indicating the power of the variable (
# n
# n in
# x
# n
# x
# n
#  ) in the expansion. Find the coefficient of
# x
# n
# x
# n
#  , if it exists in the expansion. Otherwise, return
# 0
# 0.
#
# Input formatting
# The string expression will be given in the form
# (
# a
# x
# n
# +
# b
# x
# m
# )
# k
# (ax
# n
#  +bx
# m
#  )
# k
#  , where
# a
# ,
# b
# ,
# n
# ,
# m
# ,
# k
# a,b,n,m,k are all integers,
# a
# ≠
# 0
# ,
# b
# ≠
# 0
# ,
# k
# >
# 0
# a
# 
# =0,b
# 
# =0,k>0. If
# x
# 0
# x
# 0
#   occurs, the term becomes a constant.
#
# Examples
# get_coefficient("(5x - 4)^3", 2)
# Outputs
# −
# 300
# :
# (
# 5
# x
# −
# 4
# )
# 3
# =
# 125
# x
# 3
# −
# 300
# x
# 2
# +
# 240
# x
# −
# 64.
# −300:(5x−4)
# 3
#  =125x
# 3
#  −300x
# 2
#  +240x−64.
#
# get_coefficient("(x + 5x^2)^4", 7)
# Outputs
# 500
# :
# (
# x
# +
# 5
# x
# 2
# )
# 4
# =
# x
# 4
# +
# 20
# x
# 5
# +
# 150
# x
# 6
# +
# 500
# x
# 7
# +
# 625
# x
# 8
# .
# 500:(x+5x
# 2
#  )
# 4
#  =x
# 4
#  +20x
# 5
#  +150x
# 6
#  +500x
# 7
#  +625x
# 8
#  .
#
# get_coefficient("(7x - 8x^-2)^2", 4)
# get_coefficient("(7x - 8x^-2)^2", -6)
# Both output
# 0
# :
# (
# 7
# x
# −
# 8
# x
# −
# 2
# )
# 2
# =
# (
# 7
# x
# −
# 8
# x
# 2
# )
# 2
# =
# 49
# x
# 2
# −
# 112
# x
# +
# 64
# x
# 4
# .
# 0:(7x−8x
# −2
#  )
# 2
#  =(7x−
# x
# 2
#
# 8
# ​
#  )
# 2
#  =49x
# 2
#  −
# x
# 112
# ​
#  +
# x
# 4
#
# 64
# ​
#  .
#
# MathematicsDiscrete Mathematics
# Solution
from math import comb
import re


TERM_RE = re.compile(r'''
([+-]?\d*)
x?
(?:\^([+-]?\d+))?
''', re.X)


def parse_term(term):
    term = term.replace(" ", "")
    if "x" not in term: return int(term), 0
    coef_part, exp_part = TERM_RE.fullmatch(term).groups()
    if coef_part in ("", "+"): coef = 1
    elif coef_part == "-": coef = -1
    else: coef = int(coef_part)
    exp = 1 if exp_part is None else int(exp_part)
    return coef, exp


def get_coefficient(binom: str, x_power: int) -> int | float:
    expr, k = binom.rsplit("^", 1)
    k = int(k)
    expr = expr.strip()[1:-1].replace(" ", "")
    split_idx = None
    for i in range(1, len(expr)):
        if expr[i] in "+-" and expr[i - 1] != "^":
            split_idx = i
            break
    t1 = expr[:split_idx]
    t2 = expr[split_idx:]
    a, n = parse_term(t1)
    b, m = parse_term(t2)
    ans = 0
    for i in range(k + 1):
        power = (k - i) * n + i * m
        if power == x_power:
            ans += (
                comb(k, i)
                * (a ** (k - i))
                * (b ** i)
            )
    return ans