import sys


def solution(n: int) -> None:
    """
    Time Complexity O(sqrt(N)log(sqrt(N)))
    Memory Complexity O(sqrt(N))
    """
    factorize: list[str] = []
    while n % 2 == 0:
        factorize.append('2')
        n //= 2
    upper_bound: int = int(n**.5) + 1
    for prime in range(3, upper_bound, 2):
        while n % prime == 0:
            factorize.append(str(prime))
            n //= prime
    if n > 2:
        factorize.append(str(n))
    factorize_n: int = len(factorize)
    for idx in range(factorize_n):
        if idx:
            sys.stdout.write(' ')
        sys.stdout.write(str(factorize[idx]))
    sys.stdout.write('\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    solution(n)