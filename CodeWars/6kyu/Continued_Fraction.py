# In this kata, you will have to return the continued fractionwiki of a fraction.
#
# For example, if the numerator is 311 and the denominator is 144, then you would have to return [2, 6, 3, 1, 5], because:
#
# 311
# /
# 144
# =
# 2
# +
# 1
# 6
# +
# 1
# 3
# +
# 1
# 1
# +
# 1
# 5
# 311/144=2+
# 6+
# 3+
# 1+
# 5
# 1
# ​
#
# 1
# ​
#
# 1
# ​
#
# 1
# ​
#
# If the numerator is 0, you should return [].
# Solution
def continued_fraction(nu: int, de:int) -> list[int]:
    ans: list[int] = list()
    while nu != 0 and de != 0:
        n: int = nu // de
        ans.append(n)
        x: int = max(nu - (de * n), de)
        y: int = min(nu - (de * n), de)
        nu, de = x, y
    return ans