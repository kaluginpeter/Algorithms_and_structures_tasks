import sys

MOD: int = 1_000_000_007

def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    n: int = int(sys.stdin.readline().rstrip())
    if n <= 1:
        sys.stdout.write('1\n')
        return
    a: int = 1
    b: int = 1
    for _ in range(2, n + 1):
        a, b = b, (a % MOD + b % MOD) % MOD
    sys.stdout.write(f'{b}\n')


if __name__ == '__main__':
    solution()