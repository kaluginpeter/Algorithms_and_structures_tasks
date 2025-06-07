# C. Cherry Bomb
# time limit per test2 seconds
# memory limit per test256 megabytes
# Two integer arrays a
#  and b
#  of size n
#  are complementary if there exists an integer x
#  such that ai+bi=x
#  over all 1≤i≤n
# . For example, the arrays a=[2,1,4]
#  and b=[3,4,1]
#  are complementary, since ai+bi=5
#  over all 1≤i≤3
# . However, the arrays a=[1,3]
#  and b=[2,1]
#  are not complementary.
#
# Cow the Nerd thinks everybody is interested in math, so he gave Cherry Bomb two integer arrays a
#  and b
# . It is known that a
#  and b
#  both contain n
#  non-negative integers not greater than k
# .
#
# Unfortunately, Cherry Bomb has lost some elements in b
# . Lost elements in b
#  are denoted with −1
# . Help Cherry Bomb count the number of possible arrays b
#  such that:
#
# a
#  and b
#  are complementary.
# All lost elements are replaced with non-negative integers no more than k
# .
# Input
# The first line of the input contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
#  and k
#  (1≤n≤2⋅105
# , 0≤k≤109
# ) — the size of the arrays and the maximum possible value of their elements.
#
# The second line contains n
#  integers a1,a2,...,an
#  (0≤ai≤k
# ).
#
# The third line contains n
#  integers b1,b2,...,bn
#  (−1≤bi≤k
# ). If bi=−1
# , then this element is missing.
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# Output exactly one integer, the number of ways Cherry Bomb can fill in the missing elements from b
#  such that a
#  and b
#  are complementary.
#
# Example
# InputCopy
# 7
# 3 10
# 1 3 2
# -1 -1 1
# 5 1
# 0 1 0 0 1
# -1 0 1 0 -1
# 5 1
# 0 1 0 0 1
# -1 1 -1 1 -1
# 5 10
# 1 3 2 5 4
# -1 -1 -1 -1 -1
# 5 4
# 1 3 2 1 3
# 1 -1 -1 1 -1
# 5 4
# 1 3 2 1 3
# 2 -1 -1 2 0
# 5 5
# 5 0 5 4 3
# 5 -1 -1 -1 -1
# OutputCopy
# 1
# 0
# 0
# 7
# 0
# 1
# 0
# Note
# In the first example, the only way to fill in the missing elements in b
#  such that a
#  and b
#  are complementary is if b=[2,0,1]
# .
#
# In the second example, there is no way to fill in the missing elements of b
#  such that a
#  and b
#  are complementary.
#
# In the fourth example, some b
#  arrays that are complementary to a
#  are: [4,2,3,0,1],[7,5,6,3,4],
#  and [9,7,8,5,6]
# .
# Solution
# C++ O(N) O(1) Greedy Math
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n, k;
        std::scanf("%d %d", &n, &k);
        std::vector<int> a(n, 0), b(n, 0);
        for (int j = 0; j < n; ++j) std::scanf("%d", &a[j]);
        for (int j = 0; j < n; ++j) std::scanf("%d", &b[j]);
        int prevX = -1;
        bool wasOther = false;
        for (int j = 0; j < n; ++j) {
            if (b[j] != -1) {
                wasOther = true;
                if (prevX == -1) {
                    prevX = a[j] + b[j];
                }
                if (a[j] + b[j] != prevX) {
                    prevX = -2;
                    break;
                }
            }
        }
        if (prevX == -2) {
            std::printf("0\n");
            continue;
        }
        // 'x' can be determined, he is in 'prevX' if b is not entire in '-1', in that case
        // 'prevX' is equal to '-1'
        if (prevX != -1 && (*std::max_element(a.begin(), a.end()) > prevX || (prevX - *std::min_element(a.begin(), a.end())) > k)) {
            std::printf("0\n");
            continue;
        }
        std::printf("%d\n", (!wasOther? std::max(0, 1 + *std::min_element(a.begin(), a.end()) + k - *std::max_element(a.begin(), a.end())) : 1));
    }
}


int main() {
    solution();
}

# Python O(N) O(1) Greedy Math
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().rstrip().split())
        a: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        b: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        prev_x: int = -1
        was_other: bool = False
        for j in range(n):
            if b[j] != -1:
                was_other = True
                if prev_x == -1: prev_x = a[j] + b[j]
                if a[j] + b[j] != prev_x:
                    prev_x = -2
                    break
        if prev_x == -2:
            sys.stdout.write('0\n')
            continue
        if prev_x != -1 and (max(a) > prev_x or (prev_x - min(a)) > k):
            sys.stdout.write('0\n')
            continue
        sys.stdout.write('{}\n'.format([max(0, 1 + (min(a) + k - max(a))), 1][was_other]))


if __name__ == '__main__':
    solution()