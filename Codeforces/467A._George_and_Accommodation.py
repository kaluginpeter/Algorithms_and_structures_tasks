# A. George and Accommodation
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# George has recently entered the BSUCP (Berland State University for Cool Programmers). George has a friend Alex who has also entered the university. Now they are moving into a dormitory.
#
# George and Alex want to live in the same room. The dormitory has n rooms in total. At the moment the i-th room has pi people living in it and the room can accommodate qi people in total (pi ≤ qi). Your task is to count how many rooms has free place for both George and Alex.
#
# Input
# The first line contains a single integer n (1 ≤ n ≤ 100) — the number of rooms.
#
# The i-th of the next n lines contains two integers pi and qi (0 ≤ pi ≤ qi ≤ 100) — the number of people who already live in the i-th room and the room's capacity.
#
# Output
# Print a single integer — the number of rooms where George and Alex can move in.
#
# Examples
# inputCopy
# 3
# 1 1
# 2 2
# 3 3
# outputCopy
# 0
# inputCopy
# 3
# 1 10
# 0 10
# 10 10
# outputCopy
# 2
# Solution O(N) O(1)
import sys


def solution(n: int) -> int:
    total: int = 0
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        total += y - x >= 2
    return total


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(solution(n)))