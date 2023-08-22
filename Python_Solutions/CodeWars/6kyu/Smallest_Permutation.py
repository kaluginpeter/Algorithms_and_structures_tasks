# Given a number, find the permutation with the smallest absolute value (no leading zeros).
#
# -20 => -20
# -32 => -23
# 0 => 0
# 10 => 10
# 29394 => 23499
# The input will always be an integer.
#
# FUNDAMENTALS
# Solution
def min_permutation(n):
    if n == 0: return n
    flag, count = True if n < 0 else False, 0
    out = ''.join(sorted(str(n)))
    if not flag:
        while out.startswith('0'):
            out = out[1:]
            count += 1
        out = int(out[0] + '0' * count + out[1:])
    if flag:
        out = out[1:]
        while out.startswith('0'):
            out = out[1:]
            count += 1
        out = int('-' + out[0] + '0' * count + out[1:])
    return out