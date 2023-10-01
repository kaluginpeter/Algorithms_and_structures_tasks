# Add two logs with base X, with the value of A and B. Example log A + log B where the base is X.
#
# ALGORITHMS
# Solution
import math
def logs(x, a, b):
    return (math.log(a) / math.log(x)) + (math.log(b) / math.log(x))