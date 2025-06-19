import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    n: int = int(sys.stdin.readline().rstrip())
    if n <= 1:
        sys.stdout.write('1\n')
        return
    MOD: int = 10
    count2: int = 0
    count5: int = 0
    output: int = 1
    for d in range(2, n + 1):
        num: int = d
        while num & 1 == 0:
            num //= 2
            count2 += 1
        while num % 5 == 0:
            num //= 5
            count5 += 1
        output = (output * num) % MOD
    extra2: int = count2 - count5
    for i in range(extra2): output = (output * 2) % 10
    sys.stdout.write('{}\n'.format(output))
    

if __name__ == '__main__':
    solution()