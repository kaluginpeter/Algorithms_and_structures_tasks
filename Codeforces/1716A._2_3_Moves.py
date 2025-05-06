# A. 2-3 Moves
# time limit per test1 second
# memory limit per test256 megabytes
# You are standing at the point 0
#  on a coordinate line. Your goal is to reach the point n
# . In one minute, you can move by 2
#  or by 3
#  to the left or to the right (i. e., if your current coordinate is x
# , it can become x−3
# , x−2
# , x+2
#  or x+3
# ). Note that the new coordinate can become negative.
#
# Your task is to find the minimum number of minutes required to get from the point 0
#  to the point n
# .
#
# You have to answer t
#  independent test cases.
#
# Input
# The first line of the input contains one integer t
#  (1≤t≤104
# ) — the number of test cases. Then t
#  lines describing the test cases follow.
#
# The i
# -th of these lines contains one integer n
#  (1≤n≤109
# ) — the goal of the i
# -th test case.
#
# Output
# For each test case, print one integer — the minimum number of minutes required to get from the point 0
#  to the point n
#  for the corresponding test case.
#
# Example
# InputCopy
# 4
# 1
# 3
# 4
# 12
# OutputCopy
# 2
# 1
# 2
# 4
# Solution
# C++ O(1) O(1) Greedy
#include <iostream>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        if (n == 1) {
            std::cout << 2 << '\n';
            continue;
        }
        int moves = n / 3;
        if (n % 3 != 0) ++moves;
        std::cout << moves << '\n';
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        if n == 1:
            sys.stdout.write('2\n')
            continue
        moves: int = n // 3
        if n % 3 != 0: moves += 1
        sys.stdout.write('{}\n'.format(moves))


if __name__ == '__main__':
    solution()