# A. Chat room
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word s. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word s.
#
# Input
# The first and only line contains the word s, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.
#
# Output
# If Vasya managed to say hello, print "YES", otherwise print "NO".
#
# Examples
# inputCopy
# ahhellllloou
# outputCopy
# YES
# inputCopy
# hlelo
# outputCopy
# NO
# Solution O(N) O(1)
import sys


def solution(n: str) -> str:
    letters = ['h', 'e', 'l', 'l', 'o']
    for char in n:
        if char == letters[0]:
            letters.pop(0)
            if not letters:
                return 'YES'
    return 'NO' if letters else 'YES'


if __name__ == '__main__':
    n = sys.stdin.readline().rstrip()
    sys.stdout.write(solution(n))