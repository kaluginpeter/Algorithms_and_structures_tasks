# A. Anton and Letters
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Recently, Anton has found a set. The set consists of small English letters. Anton carefully wrote out all the letters from the set in one line, separated by a comma. He also added an opening curved bracket at the beginning of the line and a closing curved bracket at the end of the line.
#
# Unfortunately, from time to time Anton would forget writing some letter and write it again. He asks you to count the total number of distinct letters in his set.
#
# Input
# The first and the single line contains the set of letters. The length of the line doesn't exceed 1000. It is guaranteed that the line starts from an opening curved bracket and ends with a closing curved bracket. Between them, small English letters are listed, separated by a comma. Each comma is followed by a space.
#
# Output
# Print a single number — the number of distinct letters in Anton's set.
#
# Examples
# inputCopy
# {a, b, c}
# outputCopy
# 3
# inputCopy
# {b, a, b, a}
# outputCopy
# 2
# inputCopy
# {}
# outputCopy
# 0
# Solution O(N) O(N)
import sys


def solution(n: str) -> str:
    return str(len(set([char for char in n if char not in '{} ,'])))


if __name__ == '__main__':
    n: str = sys.stdin.readline().rstrip()
    sys.stdout.write(solution(n))