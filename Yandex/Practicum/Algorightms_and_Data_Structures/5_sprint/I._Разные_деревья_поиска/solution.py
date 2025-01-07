import math
import sys

def solution() -> None:
    """
    Time Complexity O(1)
    Memory Complexity O(1)
    """
    n: int = int(sys.stdin.readline().rstrip())
    catalan_number: int = math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))
    sys.stdout.write(f'{catalan_number}\n')


if __name__ == '__main__':
    solution()