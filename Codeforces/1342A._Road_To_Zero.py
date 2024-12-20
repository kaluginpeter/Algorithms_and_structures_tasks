# A. Road To Zero
# time limit per test1 second
# memory limit per test256 megabytes
# You are given two integers x
#  and y
# . You can perform two types of operations:
#
# Pay a
#  dollars and increase or decrease any of these integers by 1
# . For example, if x=0
#  and y=7
#  there are four possible outcomes after this operation:
# x=0
# , y=6
# ;
# x=0
# , y=8
# ;
# x=−1
# , y=7
# ;
# x=1
# , y=7
# .
#
# Pay b
#  dollars and increase or decrease both integers by 1
# . For example, if x=0
#  and y=7
#  there are two possible outcomes after this operation:
# x=−1
# , y=6
# ;
# x=1
# , y=8
# .
# Your goal is to make both given integers equal zero simultaneously, i.e. x=y=0
# . There are no other requirements. In particular, it is possible to move from x=1
# , y=0
#  to x=y=0
# .
#
# Calculate the minimum amount of dollars you have to spend on it.
#
# Input
# The first line contains one integer t
#  (1≤t≤100
# ) — the number of testcases.
#
# The first line of each test case contains two integers x
#  and y
#  (0≤x,y≤109
# ).
#
# The second line of each test case contains two integers a
#  and b
#  (1≤a,b≤109
# ).
#
# Output
# For each test case print one integer — the minimum amount of dollars you have to spend.
#
# Example
# InputCopy
# 2
# 1 3
# 391 555
# 0 0
# 9 4
# OutputCopy
# 1337
# 0
# Note
# In the first test case you can perform the following sequence of operations: first, second, first. This way you spend 391+555+391=1337
#  dollars.
#
# In the second test case both integers are equal to zero initially, so you dont' have to spend money.
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution(int& t) {
    for (int i = 0; i < t; ++i) {
        int x, y;
        std::cin >> x >> y;
        long long a, b;
        std::cin >> a >> b;
        long long cost = 0;
        if ((x > 0 && y > 0) || (x < 0 && y < 0)) {
            long long diff = std::min(std::abs(x), std::abs(y));
            if (b <= a * 2) {
                cost += diff * b;
                x = std::abs(x) - diff;
                y = std::abs(y) - diff;
            }
        }
        cost += std::abs(x) * a;
        cost += std::abs(y) * a;
        std::cout << cost << "\n";
    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}

# Python O(1) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        a, b = map(int, sys.stdin.readline().rstrip().split())
        cost: int = 0
        if (x > 0 and y > 0) or (x < 0 and y < 0):
            diff: int = min(abs(x), abs(y))
            if b <= a * 2:
                cost += b * diff
                x = abs(x) - diff
                y = abs(y) - diff
        cost += x * a
        cost += y * a
        sys.stdout.write(str(cost) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)