# This is the SUPER performance version of This kata.
#
# You task is exactly the same as that kata. But this time, you should output result % 998244353, or otherwise the result would be too large.
#
# Data range
# sometimes
#   n <= 80000
#   m <= 100000
# while sometimes
#   n <= 3000
#   m <= 2^200
# There are 150 random tests. You will need more than just a naive linear algorithm for this task :D
#
# PerformanceAlgorithmsMathematics
# Solution
MOD = 998244353

def height(n: int, m: int) -> int:
    m %= MOD
    inv: list[int] = [0] * (n + 1)
    prev: int = 1
    output: int = 0
    for i in range(1, n+1):
        inv[i] = -(MOD // i) * inv[MOD % i] % MOD if i > 1 else 1
        prev = prev * (m - i + 1) * inv[i] % MOD
        output = (output + prev) % MOD
    return output