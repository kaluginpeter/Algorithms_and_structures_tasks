# A. IQ test
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given n numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given n numbers finds one that is different in evenness.
#
# Input
# The first line contains integer n (3 ≤ n ≤ 100) — amount of numbers in the task. The second line contains n space-separated natural numbers, not exceeding 100. It is guaranteed, that exactly one of these numbers differs from the others in evenness.
#
# Output
# Output index of number that differs from the others in evenness. Numbers are numbered from 1 in the input order.
#
# Examples
# inputCopy
# 5
# 2 4 7 8 10
# outputCopy
# 3
# inputCopy
# 4
# 1 2 1 1
# outputCopy
# 2
# Solution Bit Manipulation O(N) O(1)
import sys


def solution(n: int, numbers: list) -> str:
    eveness: int = (numbers[0] & 1) + (numbers[1] & 1) + (numbers[2] & 1)
    odd: bool = eveness >= 2
    for idx in range(n):
        if bool(numbers[idx] & 1) != odd: return str(idx + 1)


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    numbers: list = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(solution(n, numbers))