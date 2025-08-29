# A. In the Dream
# time limit per test1 second
# memory limit per test256 megabytes
# Two football teams, the RiOI team and the KDOI team, are about to have a football match. A football match consists of two halves — the first half and the second half. At the beginning of the match, both teams have a score of 0
# .
#
# As a fan of both teams, Aquawave knows that the two teams have similar levels, so neither team will score three consecutive goals in the same half.
#
# Aquawave had a dream the night before the match, in which:
#
# The score at the end of the first half was a:b
# , where a
#  is the score of the RiOI team, and b
#  is the score of the KDOI team;
# And, the score at the end of the second half was c:d
# , where c
#  is the score of the RiOI team, and d
#  is the score of the KDOI team.
# You have to determine whether Aquawave's dream can come true according to the above information.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤1000
# ). The description of the test cases follows.
#
# The only line of each test case contains four integers a
# , b
# , c
# , and d
#  (0≤a≤c≤100
# , 0≤b≤d≤100
# ) — the score at the end of the first half and the score at the end of the second half.
#
# Output
# For each test case, print "YES" if Aquawave's dream can come true. Otherwise, print "NO".
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 11
# 1 4 1 4
# 4 1 4 1
# 1 4 2 5
# 0 100 0 100
# 1 4 2 9
# 3 1 13 5
# 8 11 17 36
# 19 41 30 50
# 20 38 30 60
# 0 0 0 0
# 100 100 100 100
# OutputCopy
# YES
# YES
# YES
# NO
# NO
# YES
# NO
# NO
# YES
# YES
# YES
# Note
# We will use R
#  to represent the RiOI team's goal, and K
#  to represent the KDOI team's goal.
#
# In the first test case, the only goal order is:
#
# First half: KKRKK
# . At the end of the first half, the score is 1:4
# ;
# Second half: No goals. At the end of the second half, the score is still 1:4
# .
# In the second test case, the only goal order is:
#
# First half: RRKRR
# . At the end of the first half, the score is 4:1
# ;
# Second half: No goals. At the end of the second half, the score is still 4:1
# .
# In the third test case, one possible goal order is:
#
# First half: KKRKK
# . At the end of the first half, the score is 1:4
# ;
# Second half: KR
# . At the end of the second half, the score is 2:5
# .
# In the fourth test case, at the end of the first half, the KDOI team has scored 100
#  goals, while the RiOI team did not score any goals. Thus, in Aquawave's dream, the KDOI team scored 100
#  consecutive goals in the first half, which is impossible.
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int x1, y1, x2, y2;
    std::cin >> x1 >> y1 >> x2 >> y2;
    std::cout << ((std::min(x1, y1) * 2 + 2 >= std::max(x1, y1)) && (std::min(x2 - x1, y2 - y1) * 2 + 2 >= std::max(x2 - x1, y2 - y1)) ? "YES" : "NO") << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write('{}\n'.format(['NO', 'YES'][(min(a, b) * 2 + 2 >= max(a, b)) and (min(c - a, d - b) * 2 + 2 >= max(c - a, d - b))]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()