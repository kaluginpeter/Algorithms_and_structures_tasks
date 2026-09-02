# Your mission, should you choose to accept it, is to determine the predecessor of a given Fibonacci number n in the Fibonacci sequence.

# The Fibonacci sequence is defined by the following properties:

# fib(0) == 0
# fib(1) == 1
# fib(n) == fib(n - 1) + fib(n - 2)
# The first numbers in the Fibonacci sequence are:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# As you can see, we don't handle negative numbers, so 0 has no predecessor. Furthermore, the number 1 has 2 possible predecessors, namely 0 and 1.

# If there are multiple possible predecessors, take the smaller one. If there is no predecessor, return None.

# You should expect the following random tests:

# 4 test cases with n <= fib(2**18)
# 4 test cases with n <= fib(2**22)
# 4 test cases with n <= fib(2**26)
# This means that you should be prepared to handle numbers with up to 46_589_786 bits.

# MathematicsNumber Theory