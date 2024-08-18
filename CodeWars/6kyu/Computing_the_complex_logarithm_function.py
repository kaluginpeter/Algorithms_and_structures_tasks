# Compute the complex logarithm at any given complex number, accurate to at least 1 in 10^-12. The imaginary part should be inside the interval (−π, π] (i.e if the imaginary part is exactly π, keep it as is).
#
# Note: You shouldn't try to compute the value of this function at the poles. Please return null/NULL/nil/None (C#: throw an ArgumentException, Java: throw an ArithmeticException) if this happens.
#
# MATHEMATICSALGORITHMS
# Solution
from cmath import log as clog
def log(real, imag):
    try:
        lg = clog(complex(real, imag))
        return lg.real, lg.imag
    except:
        pass