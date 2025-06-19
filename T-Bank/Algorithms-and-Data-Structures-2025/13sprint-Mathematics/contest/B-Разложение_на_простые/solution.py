import sys


def solution() -> None:
    """
    Time Complexity O(sqrtN)
    Memory Complexity O(sqrtN)
    """
    n: int = int(sys.stdin.readline().rstrip())
    output: list[tuple[int, int]] = []
    amount: int = 0
    while n % 2 == 0:
        n //= 2
        amount += 1
    if amount: output.append((2, amount))
    bound: int = int(n**.5) + 1
    for d in range(3, bound, 2):
        amount: int = 0
        while n % d == 0:
            amount += 1
            n //= d
        if amount: output.append((d, amount))
    if n > 2: output.append((n, 1))
    for i in range(len(output)):
        if output[i][1] != 1:
            sys.stdout.write('{}^{}'.format(*output[i]))
        else: sys.stdout.write('{}'.format(output[i][0]))
        if i + 1 != len(output): sys.stdout.write('*')
    sys.stdout.write('\n')


if __name__ == '__main__':
    solution()