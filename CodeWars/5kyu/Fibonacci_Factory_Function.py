# Create a factory function genfib that returns a function fib that always returns the next Fibonacci number on each invocation ( it should return 0 when being called the first time ).
#
# Example:
#
# fib = genfib()
# fib() # returns 0
# fib() # returns 1
# fib() # returns 1
# fib() # returns 2
# MathematicsAlgorithms
# Solution
def genfib():
    a, b = 0, 1
    def fib():
        nonlocal a, b
        output: int = a
        a, b = b, a + b
        return output
    return fib