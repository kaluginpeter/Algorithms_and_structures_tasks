# Given a mathematical equation that has *,+,-,/, reverse it as follows:
#
# solve("100*b/y") = "y/b*100"
# solve("a+b-c/d*30") = "30*d/c-b+a"
# More examples in test cases.
#
# Good luck!
#
# Please also try:
#
# Simple time difference
#
# Simple remove duplicates
#
# ALGORITHMS
# Solution
import re
def solve(eq):
    return ''.join(reversed(re.split(r'(\W+)', eq)))