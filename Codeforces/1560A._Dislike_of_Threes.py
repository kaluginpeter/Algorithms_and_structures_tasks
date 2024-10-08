# A. Dislike of Threes
# time limit per test1 second
# memory limit per test256 megabytes
# Polycarp doesn't like integers that are divisible by 3
#  or end with the digit 3
#  in their decimal representation. Integers that meet both conditions are disliked by Polycarp, too.
#
# Polycarp starts to write out the positive (greater than 0
# ) integers which he likes: 1,2,4,5,7,8,10,11,14,16,…
# . Output the k
# -th element of this sequence (the elements are numbered from 1
# ).
#
# Input
# The first line contains one integer t
#  (1≤t≤100
# ) — the number of test cases. Then t
#  test cases follow.
#
# Each test case consists of one line containing one integer k
#  (1≤k≤1000
# ).
#
# Output
# For each test case, output in a separate line one integer x
#  — the k
# -th element of the sequence that was written out by Polycarp.
#
# Example
# inputCopy
# 10
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 1000
# outputCopy
# 1
# 2
# 4
# 5
# 7
# 8
# 10
# 11
# 14
# 1666
# Solution O(N) O(N)
import sys
from typing import List


def solution(t: int) -> None:
    order: List[int] = [1]
    for _ in range(t):
        x: int = int(sys.stdin.readline().rstrip())
        while x > len(order):
            for num in range(order[-1] + 1, order[-1] + x + 1):
                if num % 3 != 0 and num % 10 != 3:
                    order.append(num)
        print(order[x - 1])


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
