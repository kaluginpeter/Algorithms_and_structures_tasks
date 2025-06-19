import sys


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    sieve: list[bool] = [False] * (n + 1)
    prime_numbers: list[int] = []
    for d in range(2, n + 1):
        if not sieve[d]:
            prime_numbers.append(d)
            for next_d in range(d, n + 1, d): sieve[next_d] = True
    seen: set[int] = set()
    x = y = -1
    for prime in prime_numbers:
        seen.add(prime)
        if n - prime in seen:
            x, y = n - prime, prime
    sys.stdout.write('{} {}\n'.format(x, y))


if __name__ == '__main__':
    solution()