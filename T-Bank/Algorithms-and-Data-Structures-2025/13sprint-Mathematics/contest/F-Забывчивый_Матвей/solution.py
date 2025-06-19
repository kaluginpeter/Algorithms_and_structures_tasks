import sys


def power(x: int, y: int, p: int) -> int:
    output: int = 1
    x = x % p
    while y > 0:
        if y & 1: output = (output * x) % p
        y = y >> 1
        x = (x * x) % p
    return output;


def mod_inverse(n: int, mod: int) -> int:
    return power(n, mod - 2, mod);


def solution() -> None:
    """
    Time Complexity O(logN)
    Memory Complexity O(1)
    """
    n, m, k, MOD = map(int, sys.stdin.readline().rstrip().split())
    m_pow_n: int = power(m, n, MOD)
    k_inverse: int = mod_inverse(k, MOD)
    final_time: int = (m_pow_n * k_inverse) % MOD
    sys.stdout.write('{}\n'.format(final_time))
    

if __name__ == '__main__':
    solution()