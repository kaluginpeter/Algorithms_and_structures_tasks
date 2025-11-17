# We need prime numbers and we need them now!
#
# Write a method that takes a maximum bound and returns all primes up to and including the maximum bound.
#
# For example,
#
# 11 => [2, 3, 5, 7, 11]
# MathematicsAlgorithms
# Solution
seen: list[bool] = [False] * (10**5)
i: int = 2
while i * i <= 10**5:
    if seen[i]:
        i += 1
        continue
    for j in range(i + i, 10**5, i): seen[j] = True
    i += 1
dp: list[int] = [prime for prime in range(2, 10**5) if not seen[prime]]
def prime(n):
    left: int = 0
    right: int = len(dp) - 1
    while left <= right:
        middle: int = left + ((right - left) >> 1)
        if dp[middle] > n: right = middle - 1;
        else: left = middle + 1
    return dp[:max(0, left)]