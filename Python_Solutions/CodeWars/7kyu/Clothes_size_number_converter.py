# Description
# You have clothes international size as text (xs, s, xxl).
# Your goal is to return European number size as an number from that size
#
# Notice that there is arbitrary amount of modifiers (x), excluding m size and input can be any string
#
# Linearity
# Base size for medium (m) is 38
# (then, small (s), is 36 and large (l) is 40)
#
# As you can see scale is linear, modifier x continues that by adding or subtracting 2 from resulting size
#
# Invalid cases
# Function should handle wrong/invalid sizes
#
# Valid input has any base size (s/m/l) and any amount of modifiers (x) before base size (like xxl).
# Notice that you cannot apply modifier for m size, consider that case as invalid!
# Anything else is disallowed and should be considered as invalid (None for Python).
#
# Invalid examples: xxx, sss, xm, other string
#
# Valid Examples
# xs: 34
# s: 36
# m: 38
# l: 40
# xl: 42
#
# STRINGSFUNDAMENTALS
# Solution
def size_to_number(size):
    if len(size) == 1:
        return 38 if size == 'm' else 36 if size == 's' else 40 if size == 'l' else None
    if len(set(size)) == 2 and 'x' in size and ('s' in size or 'l' in size):
        if 'l' in size and size.index('l') < size.index('x'): return
        if 's' in size and size.index('s') < size.index('x'): return
        acc: int = size.count('x') * 2
        return 36 - acc if 's' in size else 40 + acc