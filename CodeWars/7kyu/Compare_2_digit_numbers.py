# You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers, and return the result in %.
#
# Example:
#
# compare(13,14)=50%;
# compare(23,22)=50%;
# compare(15,51)=100%;
# compare(12,34)=0%.
# FUNDAMENTALSMATHEMATICS
# Solution
def compare(a, b):
    fir, sec = sorted(str(a)), sorted(str(b))
    return '100%' if fir == sec else '50%' if fir[0] in sec or fir[1] in sec else '0%'