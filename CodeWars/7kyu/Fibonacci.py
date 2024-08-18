# Create function fib that returns n'th element of Fibonacci sequence (classic programming task).
#
# FUNDAMENTALSALGORITHMS
# Solution
def fibonacci(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a,b = b, a+b
    return a