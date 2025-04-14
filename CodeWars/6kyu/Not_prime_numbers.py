# You are given two positive integers a and b (a < b <= 20000). Complete the function which returns a list of all those numbers in the interval [a, b) whose digits are made up of prime numbers (2, 3, 5, 7) but which are not primes themselves.
#
# Be careful about your timing!
#
# Good luck :)
#
# Check my other katas:
#
# Find Nearest square number
#
# Alphabetically ordered
#
# Case-sensitive!
#
# Find your caterer
#
# FundamentalsPerformanceAlgorithms
# Solution
nums: set[int] = set()

def not_prime(n: int) -> bool:
    bound: int = int(n**.5) + 1
    return any(n % d == 0 for d in range(2, bound))

def not_primes(a, b):
    output: list[int] = []
    primes: set[int] = {2, 3, 5, 7}
    for i in range(a, b):
        if i in nums:
            output.append(i)
            continue
        x: int = i
        is_valid: bool = True
        while i:
            if i % 10 not in primes:
                is_valid = False
                break
            i //= 10
        if is_valid:
            if not_prime(x):
                output.append(x)
                nums.add(x)
    return output