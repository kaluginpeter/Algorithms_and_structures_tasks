# A. Soccer
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Dima loves watching soccer. In such a game, the score on the scoreboard is represented as x
#  : y
# , where x
#  is the number of goals of the first team, and y
#  is the number of goals of the second team. At any given time, only one team can score a goal, so the score x
#  : y
#  can change to either (x+1)
#  : y
# , or x
#  : (y+1)
# .
#
# While watching a soccer game, Dima was distracted by very important matters, and after some time, he returned to watching the game. Dima remembers the score right before he was distracted, and the score right after he returned. Given these two scores, he wonders the following question. Is it possible that, while Dima was not watching the game, the teams never had an equal score?
#
# It is guaranteed that at neither of the two time points Dima remembers the teams had equal scores. However, it is possible that the score did not change during his absence.
#
# Help Dima and answer the question!
#
# Input
# Each test consists of several test cases. The first line contains an integer t
#  (1≤t≤104
# ) — the number of test cases. Then follows the description of the test cases.
#
# The first line of each test case contains two integers x1,y1
#  (0≤x1,y1≤109
# , x1≠y1
# ) — the score before Dima was distracted.
#
# The second line of each test case contains two integers x2,y2
#  (x1≤x2≤109
# , y1≤y2≤109
# , x2≠y2
# ) — the score when Dima returned.
#
# Output
# For each test case, output "YES" without quotes if it is possible, that the teams never had a tie while Dima was away, otherwise output "NO" without quotes.
#
# You can output each letter in any case (for example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as a positive answer).
#
# Example
# inputCopy
# 6
# 1 0
# 5 0
# 1 2
# 3 2
# 1 2
# 4 5
# 1 2
# 4 3
# 1 2
# 1 2
# 998244353 0
# 1000000000 999999999
# outputCopy
# YES
# NO
# YES
# NO
# YES
# YES
# Note
# In the first test case, the score before Dima left was 1
#  : 0
# . When he leaves, the first team scores several goals in a row until the score becomes 5
#  : 0
# , so the answer is YES.
#
# In the second test case, the score could only change as follows:
#
# 1
#  : 2
# 2
#  : 2
# 3
#  : 2
# In this scenario, there is a moment when the teams have an equal score, so the answer is NO.
#
# In the third test case, one of the possible developments is:
#
# 1
#  : 2
# 1
#  : 3
# 2
#  : 3
# 2
#  : 4
# 2
#  : 5
# 3
#  : 5
# 4
#  : 5
# In this scenario, there was no time when the score was equal, so the answer is YES.
# Solution O(1) O(1)
import sys


def solution(t: int) -> None:
    for _ in range(t):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        xn, yn = map(int, sys.stdin.readline().rstrip().split())
        if x == y and xn != yn:
            print('YES')
        elif x > y and xn > yn:
            print('YES')
        elif y > x and yn > xn:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
