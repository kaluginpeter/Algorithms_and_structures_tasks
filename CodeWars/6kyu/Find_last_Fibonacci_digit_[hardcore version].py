# Just like in the "father" kata, you will have to return the last digit of the
# nth element in the Fibonacci sequence (starting with 1,1, to be extra clear, not with 0,1 or other numbers).
#
# You will just get much bigger numbers, so good luck bruteforcing your way through it ;)
#
# last_fib_digit(1) == 1
# last_fib_digit(2) == 1
# last_fib_digit(3) == 2
# last_fib_digit(1000) == 5
# last_fib_digit(1000000) == 5
# ALGORITHMS
# Solution
def last_fib_digit(n):
    return int('011235831459437077415617853819099875279651673033695493257291'[n % 60])