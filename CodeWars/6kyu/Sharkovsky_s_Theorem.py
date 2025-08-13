# Sharkovsky's Theorem involves the following ordering of the natural numbers:
#
# 3
# ≺
# 5
# ≺
# 7
# ≺
# 9
# ≺
# .
# .
# .
# ≺
# 2
# ⋅
# 3
# ≺
# 2
# ⋅
# 5
# ≺
# 2
# ⋅
# 7
# ≺
# 2
# ⋅
# 9
# ≺
# .
# .
# .
# ≺
# 2
# n
# ⋅
# 3
# ≺
# 2
# n
# ⋅
# 5
# ≺
# 2
# n
# ⋅
# 7
# ≺
# 2
# n
# ⋅
# 9
# ≺
# .
# .
# .
# ≺
# 2
# n
# +
# 1
# ⋅
# 3
# ≺
# 2
# n
# +
# 1
# ⋅
# 5
# ≺
# 2
# n
# +
# 1
# ⋅
# 7
# ≺
# 2
# n
# +
# 1
# ⋅
# 9
# ≺
# .
# .
# .
# ≺
# 2
# n
# ≺
# 2
# n
# −
# 1
# ≺
# 2
# n
# −
# 2
# ≺
# 2
# n
# −
# 3
# ≺
# .
# .
# .
# ≺
# 8
# ≺
# 4
# ≺
# 2
# ≺
# 1
# 3≺5≺7≺9≺...
# ≺2⋅3≺2⋅5≺2⋅7≺2⋅9≺...
# ≺2
# n
#  ⋅3≺2
# n
#  ⋅5≺2
# n
#  ⋅7≺2
# n
#  ⋅9≺...
# ≺2
# n+1
#  ⋅3≺2
# n+1
#  ⋅5≺2
# n+1
#  ⋅7≺2
# n+1
#  ⋅9≺...
# ≺2
# n
#  ≺2
# n−1
#  ≺2
# n−2
#  ≺2
# n−3
#  ≺...
# ≺8≺4≺2≺1
# Your task is to complete the function which returns true if
# a
# ≺
# b
# a≺b according to this ordering, and false otherwise.
#
# You may assume both
# a
# a and
# b
# b are non-zero positive integers.
#
# MathematicsAlgorithms
# Solution
def is_power_two(x):
    return x != 0 and (x & (x - 1)) == 0

def sharkovsky(a, b):
    if a == b: return False
    a_power = is_power_two(a)
    b_power = is_power_two(b)
    if not a_power and not b_power:
        exp_a = 0
        temp_a = a
        while temp_a % 2 == 0:
            temp_a //= 2
            exp_a += 1
        exp_b = 0
        temp_b = b
        while temp_b % 2 == 0:
            temp_b //= 2
            exp_b += 1
        if exp_a < exp_b: return True
        elif exp_a > exp_b: return False
        return temp_a < temp_b
    elif a_power and b_power:return a > b
    if not a_power:return True
    return False