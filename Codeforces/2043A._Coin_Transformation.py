# A. Coin Transformation
# time limit per test2 seconds
# memory limit per test512 megabytes
# Initially, you have a coin with value n
# . You can perform the following operation any number of times (possibly zero):
#
# transform one coin with value x
# , where x
#  is greater than 3
#  (x>3
# ), into two coins with value ⌊x4⌋
# .
# What is the maximum number of coins you can have after performing this operation any number of times?
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# Each test case consists of one line containing one integer n
#  (1≤n≤1018
# ).
#
# Output
# For each test case, print one integer — the maximum number of coins you can have after performing the operation any number of times.
#
# Example
# InputCopy
# 4
# 1
# 5
# 16
# 1000000000000000000
# OutputCopy
# 1
# 2
# 4
# 536870912
# Note
# In the first example, you have a coin of value 1
# , and you can't do anything with it. So, the answer is 1
# .
#
# In the second example, you can transform a coin of value 5
#  into two coins with value 1
# .
#
# In the third example, you can transform a coin of value 16
#  into two coins with value 4
# . Each of the resulting coins can be transformed into two coins with value 1
# .
# Solution
# C++ O(log4(N)) O(1) Math
#include <iostream>


void solution() {
    long long n;
    std::cin >> n;
    int power = 0;
    while (n > 3) {
        n /= 4;
        ++power;
    }
    long long output = 1;
    while (power > 0) {
        output *= 2;
        --power;
    }
    std::cout << output << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(log4(N)) O(1) Math
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    power: int = 0
    while n > 3:
        power += 1
        n //= 4
    sys.stdout.write('{}\n'.format(pow(2, power)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()