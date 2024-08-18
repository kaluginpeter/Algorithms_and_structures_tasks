1703A. YES or YES?
# A. YES or YES?
# time limit per test1 second
# memory limit per test256 megabytes
# There is a string s
#  of length 3
# , consisting of uppercase and lowercase English letters. Check if it is equal to "YES" (without quotes), where each letter can be in any case. For example, "yES", "Yes", "yes" are all allowable.
#
# Input
# The first line of the input contains an integer t
#  (1≤t≤103
# ) — the number of testcases.
#
# The description of each test consists of one line containing one string s
#  consisting of three characters. Each character of s
#  is either an uppercase or lowercase English letter.
#
# Output
# For each test case, output "YES" (without quotes) if s
#  satisfies the condition, and "NO" (without quotes) otherwise.
#
# You can output "YES" and "NO" in any case (for example, strings "yES", "yes" and "Yes" will be recognized as a positive response).
#
# Example
# inputCopy
# 10
# YES
# yES
# yes
# Yes
# YeS
# Noo
# orZ
# yEz
# Yas
# XES
# outputCopy
# YES
# YES
# YES
# YES
# YES
# NO
# NO
# NO
# NO
# NO
# Note
# The first five test cases contain the strings "YES", "yES", "yes", "Yes", "YeS". All of these are equal to "YES", where each character is either uppercase or lowercase.
# Solution String O(N) O(N)
import sys


def solution(t: int) -> None:
    for _ in range(t):
        word: str = sys.stdin.readline().rstrip()
        print(['NO', 'YES'][word.lower() == 'yes'])


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
