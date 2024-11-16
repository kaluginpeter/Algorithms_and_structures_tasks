import sys


def solution(x_length: int, x: list[int], k: int) -> None:
    """
    Time Complexity O(N), where N is the length of place values of the largest number
    Memory Complexity O(N), where N is the length of place values of the largest number
    """
    output: list[int] = []
    additional: int = 0
    for idx in range(x_length - 1, -1, -1):
        sum_digits: int = x[idx] + k % 10 + additional
        additional = sum_digits // 10
        output.append(sum_digits % 10)
        k //= 10
    while k:
        sum_digits: int = k % 10 + additional
        additional = sum_digits // 10
        output.append(sum_digits % 10)
        k //= 10
    if additional:
        output.append(additional)
    n: int = len(output)
    for idx in range(n - 1, -1, -1):
        sys.stdout.write(str(output[idx]))
        if idx:
            sys.stdout.write(' ')
    sys.stdout.write('\n')


if __name__ == '__main__':
    x_length: int = int(sys.stdin.readline().rstrip())
    x: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    k: int = int(sys.stdin.readline().rstrip())
    solution(x_length, x, k)
