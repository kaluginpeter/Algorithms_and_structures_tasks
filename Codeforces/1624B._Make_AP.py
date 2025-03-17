# B. Make AP
# time limit per test2 seconds
# memory limit per test256 megabytes
# Polycarp has 3
#  positive integers a
# , b
#  and c
# . He can perform the following operation exactly once.
#
# Choose a positive integer m
#  and multiply exactly one of the integers a
# , b
#  or c
#  by m
# .
# Can Polycarp make it so that after performing the operation, the sequence of three numbers a
# , b
# , c
#  (in this order) forms an arithmetic progression? Note that you cannot change the order of a
# , b
#  and c
# .
#
# Formally, a sequence x1,x2,…,xn
#  is called an arithmetic progression (AP) if there exists a number d
#  (called "common difference") such that xi+1=xi+d
#  for all i
#  from 1
#  to n−1
# . In this problem, n=3
# .
#
# For example, the following sequences are AP: [5,10,15]
# , [3,2,1]
# , [1,1,1]
# , and [13,10,7]
# . The following sequences are not AP: [1,2,4]
# , [0,1,0]
#  and [1,3,2]
# .
#
# You need to answer t
#  independent test cases.
#
# Input
# The first line contains the number t
#  (1≤t≤104
# ) — the number of test cases.
#
# Each of the following t
#  lines contains 3
#  integers a
# , b
# , c
#  (1≤a,b,c≤108
# ).
#
# Output
# For each test case print "YES" (without quotes) if Polycarp can choose a positive integer m
#  and multiply exactly one of the integers a
# , b
#  or c
#  by m
#  to make [a,b,c]
#  be an arithmetic progression. Print "NO" (without quotes) otherwise.
#
# You can print YES and NO in any (upper or lower) case (for example, the strings yEs, yes, Yes and YES will be recognized as a positive answer).
#
# Example
# InputCopy
# 11
# 10 5 30
# 30 5 10
# 1 2 3
# 1 6 3
# 2 6 3
# 1 1 1
# 1 1 2
# 1 1 3
# 1 100000000 1
# 2 1 1
# 1 2 2
# OutputCopy
# YES
# YES
# YES
# YES
# NO
# YES
# NO
# YES
# YES
# NO
# YES
# Note
# In the first and second test cases, you can choose the number m=4
#  and multiply the second number (b=5
# ) by 4
# .
#
# In the first test case the resulting sequence will be [10,20,30]
# . This is an AP with a difference d=10
# .
#
# In the second test case the resulting sequence will be [30,20,10]
# . This is an AP with a difference d=−10
# .
#
# In the third test case, you can choose m=1
#  and multiply any number by 1
# . The resulting sequence will be [1,2,3]
# . This is an AP with a difference d=1
# .
#
# In the fourth test case, you can choose m=9
#  and multiply the first number (a=1
# ) by 9
# . The resulting sequence will be [9,6,3]
# . This is an AP with a difference d=−3
# .
#
# In the fifth test case, it is impossible to make an AP.
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        long long a, b, c;
        std::scanf("%lld %lld %lld", &a, &b, &c);
        // a case
        bool isValid = false;
        long long x = b - (c - b);
        if (x >= a && x % a == 0 && (c - b == b - x)) isValid = true;
        // b case
        x = a + (c - a) / 2;
        if (x >= b && x % b == 0 && (x - a == c - x)) isValid = true;
        // c case
        x = b + (b - a);
        if (x >= c && x % c == 0 && (b - a == x - b)) isValid = true;

        // a case
        x = b + (b - c);
        if (x >= a && x % a == 0 && (a - b == b - c)) isValid = true;
        // b case
        x = a - (a - c) / 2;
        if (x >= b && x % b == 0 && (a - x == x - c)) isValid = true;
        // c case
        x = b - (a - b);
        if (x >= c && x % c == 0 && (a - b == b - x)) isValid = true;
        std::cout << (isValid? "YES" : "NO") << "\n";
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        #  a case
        is_valid: bool = False
        x: int = b - (c - b)
        if x >= a and x % a == 0 and (c - b == b - x): is_valid = True
        #  b case
        x = a + (c - a) // 2
        if x >= b and x % b == 0 and (x - a == c - x): is_valid = True
        #  c case
        x = b + (b - a)
        if x >= c and x % c == 0 and (b - a == x - b): is_valid = True

        #  a case
        x = b + (b - c)
        if x >= a and x % a == 0 and (a - b == b - c): is_valid = True
        #  b case
        x = a - (a - c) / 2
        if x >= b and x % b == 0 and (a - x == x - c): is_valid = True
        #  c case
        x = b - (a - b)
        if x >= c and x % c == 0 and (a - b == b - x): is_valid = True
        sys.stdout.write('{}\n'.format(['NO', 'YES'][is_valid]))


if __name__ == '__main__':
    solution()