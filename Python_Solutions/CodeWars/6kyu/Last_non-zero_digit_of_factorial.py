# Your task is to find the last non-zero digit of
# �
# !
# n! (factorial).
#
# �
# !
# =
# 1
# ×
# 2
# ×
# 3
# ×
# ⋯
# ×
# �
# n!=1×2×3×⋯×n
#
# Example:
# If
# �
# =
# 12
# n=12, your function should return
# 6
# 6 since
# 12
# !
# =
# 479001600
# 12!=479001600
#
# Input
# Non-negative integer n
# Range: 0 - 2.5E6
#
# Output
# Last non-zero digit of
# �
# !
# n!
#
# Note
# Calculating the whole factorial will timeout.
#
# MATHEMATICSALGORITHMS
# Solution
def last_digit(n):
    if n < 10: return [1, 1, 2, 6, 4, 2, 2, 4, 2, 8][n]
    return (4 if int(str(n)[-2]) % 2 else 6) * last_digit(n // 5) * last_digit(n % 10) % 10