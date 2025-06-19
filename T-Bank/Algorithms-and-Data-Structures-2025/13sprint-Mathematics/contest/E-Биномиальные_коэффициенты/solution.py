import sys

MOD: int = 1000000007
MAX: int = 1000000

fact: list[int] = [0] * (MAX + 1)
inv_fact: list[int] = [0] * (MAX + 1)

def power(x: int, y: int, p: int) -> int:
    output: int = 1
    x = x % p
    while y > 0:
        if y & 1: output = (output * x) % p
        y = y >> 1
        x = (x * x) % p
    return output;


def precompute() -> None:
    fact[0] = 1;
    for i in range(1, MAX + 1): fact[i] = (fact[i - 1] * i) % MOD
    inv_fact[MAX] = power(fact[MAX], MOD - 2, MOD)
    for i in range(MAX - 1, -1, -1): inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

def binomial_coefficient(n: int, k: int) -> int:
    if k < 0 or k > n: return 0
    return (fact[n] * inv_fact[k] % MOD) * inv_fact[n - k] % MOD


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n, k = map(int, sys.stdin.readline().rstrip().split())
    precompute()
    sys.stdout.write('{}\n'.format(binomial_coefficient(n, k)))
    

if __name__ == '__main__':
    solution()