# Numbers ending with zeros are boring.
#
# They might be fun in your world, but not here.
#
# Get rid of them. Only the ending ones.
#
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway
#
# FUNDAMENTALS
# Solution
def no_boring_zeros(n):
    while str(n).endswith('0'):
        n = str(n)[:-1]
    return int(n) if n else 0