# Little context
# In a mathematical framework called Zermelo-Fraenkel set theory (ZFC, for short), every piece of mathematics is defined through sets. The most simple item to define this way are non-negative integers. This is the task for this kata.
#
# Task
# Given a non-negative integer n, return its ZFC definition as a string (see formatting below).
#
# Definition and Output Formatting
# The term "cardinality" means the size of the set.
# In set theory, non-negative integers are also called cardinal numbers. Any cardinal number
# n
# n can be represented as a set, containing all cardinal numbers less than
# n
# n and having a cardinality of
# n
# n. The most simple case is
# 0
# 0: which set has the cardinality of
# 0
# 0? An empty set. So, by ZFC definition,
# 0
# →
# {
# }
# 0→{}. Then comes
# 1
# 1. It can be defined as
# {
# 0
# }
# {0} but we already know that
# 0
# →
# {
# }
# 0→{}, so technically,
# 1
# →
# {
# {
# }
# }
# 1→{{}}. And the same process continues for next cardinal numbers:
#
# 0
# →
# {
# }
# 0→{}
#
# 1
# →
# {
# {
# }
# }
# 1→{{}}
#
# 2
# →
# {
# {
# }
# ,
# {
# {
# }
# }
# }
# 2→{{},{{}}}
#
# 3
# →
# {
# {
# }
# ,
# {
# {
# }
# }
# ,
# {
# {
# }
# ,
# {
# {
# }
# }
# }
# }
# 3→{{},{{}},{{},{{}}}}
#
# ⋮
#
# For the output formatting, each of the curly brackets
# {
# }
# {} must be in a string. There must be no spaces in the string, and the numbers represented in the set must be in ascending order. Examples of formatting below:
#
# 0  ->  "{}"
# 1  ->  "{{}}"
# 2  ->  "{{},{{}}}"
# 3  ->  "{{},{{}},{{},{{}}}}"
# ...
# Input constraints
# 0
# ≤
# n
# ≤
# 25
# 0≤n≤25
#
# Good luck!
#
# Set Theory
# Solution
memo: dict[int, str] = {}
memo[0] = '{}'
for i in range(1, 25 + 1):
    memo[i] = '{' + ','.join(memo[j] for j in range(i)) + '}'

def zfc_definition(n: int) -> str:
    return memo[n]