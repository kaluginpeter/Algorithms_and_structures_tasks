# First order Chebyshew polynomials are defined by:
#
# T{0}( v ) = 1
# T{1}( v ) = v
# T{n+1}( v ) = 2 * v * T{n}( v ) - T{n-1}( v )
# Calculate T{n}( v ) for given values of v and n.
#
# You don't have to round your results but you should expect large values.
#
# ALGORITHMS
# Solution
from functools import lru_cache
@lru_cache(maxsize=None)
def chebyshev(n,v):
    if n == 0:
        return 1
    if n == 1:
        return v
    return 2 * v * chebyshev(n-1, v) - chebyshev(n-2, v)